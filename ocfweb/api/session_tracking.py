import json
from enum import Enum
from functools import partial
from ipaddress import ip_address

from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from ipware.ip import get_real_ip
from ocflib.infra.hosts import hosts_by_filter
from ocflib.infra.net import is_ocf_ip
from ocflib.lab.stats import get_connection

from ocfweb.caching import cache
from ocfweb.caching import periodic

CLEANUP_TIMEOUT = 3

State = Enum('State', ['active', 'cleanup'])

get_connection = partial(
    get_connection,
    user=settings.OCFSTATS_USER,
    password=settings.OCFSTATS_PASSWORD,
    db=settings.OCFSTATS_DB,
)


@require_POST
@csrf_exempt
def log_session(request):
    """Primary API endpoint for session tracking.

    Desktops have a cronjob that calls this endpoint: https://git.io/vpIKX
    """

    remote_ip = get_real_ip(request)

    if not is_ocf_ip(ip_address(remote_ip)):
        return HttpResponse('Not Authorized', status=401)

    try:
        host = _get_desktops().get(remote_ip)

        if not host:
            raise ValueError('IP {} does not belong to a desktop'.format(remote_ip))

        body = json.loads(request.body.decode('utf-8'))
        state = State[body.get('state')]  # triggers KeyError
        user = body.get('user')

        if not user:
            # could also check LDAP, but that would result in
            # thousands of extra requests per day to firestorm
            raise ValueError('No user specified')

        if state is State.cleanup:
            _close_sessions(host)
        elif state is State.active and _session_exists(host, user):
            _refresh_session(host, user)
        else:
            _new_session(host, user)

        return HttpResponse(status=204)

    except (KeyError, ValueError) as e:
        return HttpResponseBadRequest(e)


def _new_session(host, user):
    """Register new session in when a user logs into a desktop."""

    _close_sessions(host)

    with get_connection() as c:
        c.execute(
            'INSERT INTO `session` (`host`, `user`, `start`, `last_update`) '
            'VALUES (%s, %s, NOW(), NOW())', (host, user),
        )


def _session_exists(host, user):
    """Returns whether an open session already exists for a given host and user."""

    with get_connection() as c:
        c.execute(
            'SELECT COUNT(*) AS `count` FROM `session` '
            'WHERE `host` = %s AND `user` = %s AND `end` IS NULL', (host, user),
        )

        return c.fetchone()['count'] > 0


def _refresh_session(host, user):
    """Keep a session around if the user is still logged in."""

    with get_connection() as c:
        c.execute(
            'UPDATE `session` SET `last_update` = NOW() '
            'WHERE `host` = %s AND `user` = %s AND `end` IS NULL', (host, user),
        )


def _close_sessions(host):
    """Close all sessions for a particular host."""

    with get_connection() as c:
        c.execute(
            'UPDATE `session` SET `end` = NOW(), `last_update` = NOW() '
            'WHERE `host` = %s AND `end` IS NULL', (host,),
        )


@periodic(60)
def _cleanup_sessions():
    """Periodically clean up sessions that don't die naturally.

    For example, if a desktop crashes or is reset.
    """

    with get_connection() as c:
        c.execute(
            'UPDATE `session` SET `end` = `last_update` WHERE '
            '`end` IS NULL AND `last_update` < '
            ' ADDDATE(NOW(), -{} MINUTE)'.format(CLEANUP_TIMEOUT),
        )


@cache()
def _get_desktops():
    """Return IP address to fqdn mapping for OCF desktops from LDAP."""

    return {e['ipHostNumber'][0]: e['cn'][0] + '.ocf.berkeley.edu'
            for e in hosts_by_filter('(type=desktop)')}