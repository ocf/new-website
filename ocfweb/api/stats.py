from typing import List
from typing import Tuple

from django.http import HttpRequest
from django.http import JsonResponse
from ocflib.lab.stats import humanize_bytes

from ocfweb.stats.mirrors import bandwidth_semester
from ocfweb.stats.summary import desktop_profiles
from ocfweb.stats.summary import printers
from ocfweb.stats.summary import staff_in_lab
from ocfweb.stats.summary import users_in_lab_count
# These endpoints are for ocfstatic stats


def get_num_users_in_lab(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        users_in_lab_count(),
        safe=False,
    )


def get_staff_in_lab(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        staff_in_lab(),
        safe=False,
    )


def get_printers_summary(request: HttpRequest) -> JsonResponse:
    response = JsonResponse(
        printers(),
        safe=False,
    )
    return response


def get_desktop_usage(request: HttpRequest) -> JsonResponse:
    """
    Copy desktop usage from Django API by grabbing class attributes that
    can't be serialized to JSON
    """

    responseList = []
    for profile in desktop_profiles():
        minutes_idle = profile.minutes_idle
        minutes_busy = profile.minutes_busy
        responseList.append({
            'hostname': profile.hostname,
            'minutes_idle': int(minutes_idle),
            'minutes_busy': int(minutes_busy),
            'percent': int(100 * minutes_busy / max(1, (minutes_idle + minutes_busy))),
        })

    response = JsonResponse(
        responseList,
        safe=False,
    )
    return response


def get_mirrors_showcase(request: HttpRequest) -> JsonResponse:
    """ Return bandwidth for a few mirrors that we showcase on stats page
    In human-readable form, sorted with biggest bandwidth first
    """

    mirrors_showcase = ['ubuntu', 'debian', 'archlinux']

    total, by_dist = bandwidth_semester(humanize=False)
    mirrors_showcase_data: List[Tuple[str, int]] = []

    for m in mirrors_showcase:
        bw_sum = 0
        for dist, bw in by_dist:
            if dist.startswith(m):
                bw_sum += bw
        mirrors_showcase_data.append((m, bw_sum))

    mirrors_showcase_data.sort(key=lambda m: m[1], reverse=True)
    response = JsonResponse(
        [(b[0], humanize_bytes(b[1])) for b in mirrors_showcase_data],
        safe=False,
    )

    return response
