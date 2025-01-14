'''
STATUS EXAMPLE
- Follow the formats to list the desktop

* For a desktop thats not upgraded yet.
        ThingToUpgrade.from_hostname(
            'death',
            comments='same time as all login servers',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),

* For a desktop that has been upgraded.
        ThingToUpgrade.from_hostname(
            'maelstrom',
            comments="Scanner",
            status=ThingToUpgrade.UPGRADED,
        ),

*  For a desktop that has been blocked from upgrading.
        ThingToUpgrade.from_hostname(
            'venom',
            status=ThingToUpgrade.BLOCKED,
        ),

'''
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
        # Desktops
        ThingToUpgrade.from_hostname(
            'bandit',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'blight',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'bolt',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'callie',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'chaos',
            comments='Scanner',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'cyanide',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'drought',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'fred',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'gabriel',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'hailstorm',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'heatwave',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'lexy',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'madcow',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'maelstrom',
            comments='Scanner',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'misty',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'pickles',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'pumpkin',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'shadow',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'smokey',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'socks',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'spots',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'sunny',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'surge',
            comments='Scanner',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'tabitha',
            status=ThingToUpgrade.UPGRADED,
        ),
        ThingToUpgrade.from_hostname(
            'venom',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
        ThingToUpgrade.from_hostname(
            'volcano',
            comments='Old PC',
            status=ThingToUpgrade.NEEDS_UPGRADE,
        ),
    )


def desktop_upgrade(doc: Document, request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'docs/desktop_upgrade.html',
        {
            'title': doc.title,
            'servers': _get_servers(),
            'blocked': ThingToUpgrade.BLOCKED,
            'upgraded': ThingToUpgrade.UPGRADED,
        },
    )
