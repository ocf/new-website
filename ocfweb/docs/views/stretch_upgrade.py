from collections import namedtuple

from django.shortcuts import render
from ocflib.misc.validators import host_exists

from ocfweb.caching import cache
from ocfweb.docs.views.servers import Host


class ThingToUpgrade(namedtuple(
    'ThingToUpgrade', (
        'host',
        'status',
        'comments',
        'has_dev',
    ),
)):
    NEEDS_UPGRADE = 1
    BLOCKED = 2
    UPGRADED = 3

    @classmethod
    def from_hostname(cls, hostname, status=NEEDS_UPGRADE, comments=None):
        has_dev = host_exists('dev-' + hostname + '.ocf.berkeley.edu')
        return cls(
            host=Host.from_ldap(hostname),
            status=status,
            has_dev=has_dev,
            comments=comments,
        )


@cache()
def _get_servers():
    return (
        # login servers
        ThingToUpgrade.from_hostname(
            'death',
            comments='same time as all login servers',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'tsunami',
            comments='same time as all login servers',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'vampires',
            comments='same time as all login servers',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'firestorm',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'anthrax',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'maelstrom',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'supernova',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'biohazard',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'dementors',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'flood',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'pestilence',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'thunder',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'whiteout',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname('reaper', status=ThingToUpgrade.UPGRADED),
        ThingToUpgrade.from_hostname('democracy', status=ThingToUpgrade.UPGRADED),
        ThingToUpgrade.from_hostname(
            'zombies',
            status=ThingToUpgrade.UPGRADED,
            comments='in-place (not well puppeted)',
        ),
        ThingToUpgrade.from_hostname(
            'lightning',
            status=ThingToUpgrade.UPGRADED,
            comments="Made a new host and rsync'd across certs, private share, and environments",
        ),
        ThingToUpgrade.from_hostname(
            'fallingrocks',
            status=ThingToUpgrade.UPGRADED,
            comments='rebuilt, with the old /opt/mirrors drive mounted in-place',
        ),
        ThingToUpgrade.from_hostname('tornado', status=ThingToUpgrade.UPGRADED),

        # mesos servers
        ThingToUpgrade.from_hostname(
            'whirlwind',
            status=ThingToUpgrade.UPGRADED,
            comments='Marathon packages are currently manually built and installed, for testing Marathon on stretch',
        ),
        ThingToUpgrade.from_hostname(
            'pileup',
            status=ThingToUpgrade.UPGRADED,
            comments='No official Marathon packages yet, but manually-built ones work',
        ),
        ThingToUpgrade.from_hostname(
            'monsoon',
            status=ThingToUpgrade.UPGRADED,
            comments='No official Marathon packages yet, but manually-built ones work',
        ),

        # raspberry pi
        ThingToUpgrade.from_hostname(
            'overheat',
            status=ThingToUpgrade.UPGRADED,
            comments='not puppeted, still needs ocflib and a wrapper around the LED sign',
        ),

        # physical servers
        ThingToUpgrade.from_hostname(
            'riptide',
            status=ThingToUpgrade.UPGRADED,
            comments='it was made this way',
        ),
        ThingToUpgrade.from_hostname(
            'jaws',
            status=ThingToUpgrade.UPGRADED,
            comments='in-place, too hard to move stuff around',
        ),
        ThingToUpgrade.from_hostname(
            'pandemic',
            status=ThingToUpgrade.UPGRADED,
            comments='Upgraded when installing new drives',
        ),
        ThingToUpgrade.from_hostname(
            'hal',
            status=ThingToUpgrade.UPGRADED,
            comments='Upgraded when installing new drives',
        ),
    )


def stretch_upgrade(doc, request):
    return render(
        request,
        'docs/stretch_upgrade.html',
        {
            'title': doc.title,
            'servers': _get_servers(),
            'blocked': ThingToUpgrade.BLOCKED,
            'upgraded': ThingToUpgrade.UPGRADED,
        },
    )
