from collections import namedtuple
from typing import Any
from typing import Optional
from typing import Tuple

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from ocflib.misc.validators import host_exists

from ocfweb.caching import cache
from ocfweb.docs.doc import Document
from ocfweb.docs.views.servers import Host


class ThingToUpgrade(
    namedtuple(
        'ThingToUpgrade', (
            'host',
            'status',
            'comments',
            'has_dev',
        ),
    ),
):
    NEEDS_UPGRADE = 1
    BLOCKED = 2
    UPGRADED = 3

    @classmethod
    def from_hostname(cls: Any, hostname: str, status: int = NEEDS_UPGRADE, comments: Optional[str] = None) -> Any:
        has_dev = host_exists('dev-' + hostname + '.ocf.berkeley.edu')
        return cls(
            host=Host.from_ldap(hostname),
            status=status,
            has_dev=has_dev,
            comments=comments,
        )


@cache()
def _get_servers() -> Tuple[Any, ...]:
    return (
        # login servers
        ThingToUpgrade.from_hostname(
            'death',
            comments='same time as all login servers',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'tsunami',
            comments='same time as all login servers',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'vampires',
            comments='same time as all login servers',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'firestorm',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'anthrax',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'maelstrom',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'supernova',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'biohazard',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'dementors',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'flood',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'pestilence',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'thunder',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'whiteout',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname('reaper', status=ThingToUpgrade.UPGRADED),
        ThingToUpgrade.from_hostname('democracy', status=ThingToUpgrade.NEEDS_UPGRADE),
        ThingToUpgrade.from_hostname(
            'zombies',
            status=ThingToUpgrade.NEEDS_UPGRADE,
            comments='in-place (not well puppeted)',
        ),
        ThingToUpgrade.from_hostname(
            'lightning',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'gridlock',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'lethe',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'pgp',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'segfault',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'monsoon',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'fraud',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),

        # kubernetes servers
        ThingToUpgrade.from_hostname(
            'coup',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'autocrat',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'deadlock',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),

        # raspberry pi
        ThingToUpgrade.from_hostname(
            'overheat',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),

        # physical hosts
        ThingToUpgrade.from_hostname(
            'riptide',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'jaws',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'pandemic',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'hal',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'scurvy',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'dataloss',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'bedbugs',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'corruption',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'fallingrocks',
            status=ThingToUpgrade.NEEDS_UPGRADE,
            comments='dev-fallingrocks is migrated already',
        ),
        ThingToUpgrade.from_hostname(
            'tornado',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'y2k',
            status=ThingToUpgrade.UPGRADED,
        ),
    )


def buster_upgrade(doc: Document, request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'docs/buster_upgrade.html',
        {
            'title': doc.title,
            'servers': _get_servers(),
            'blocked': ThingToUpgrade.BLOCKED,
            'upgraded': ThingToUpgrade.UPGRADED,
        },
    )
