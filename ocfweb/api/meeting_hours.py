from typing import Any
from typing import List

from django.http import HttpRequest
from django.http import JsonResponse
from ocflib.org.meeting_hours import read_current_meetings
from ocflib.org.meeting_hours import read_meeting_list
from ocflib.org.meeting_hours import read_next_meetings

from ocfweb.caching import periodic


def get_meetings_list(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        [item._asdict() for item in _read_meeting_list()],
        safe=False,
    )


def get_next_meetings(request: HttpRequest) -> JsonResponse:
    next_meetings = _read_next_meetings()
    if next_meetings is None:
        return JsonResponse(
            {},
            status=204,
        )

    return JsonResponse(
        [next_meeting._asdict() for next_meeting in next_meetings],
        safe=False,
    )


def get_current_meetings(request: HttpRequest) -> JsonResponse:
    current_meetings = _read_current_meetings()
    if current_meetings is None:
        return JsonResponse(
            {},
            status=204,
        )

    return JsonResponse(
        [current_meeting._asdict() for current_meeting in current_meetings],
        safe=False,
    )


def _read_meeting_list() -> List[Any]:
    return read_meeting_list()


@periodic(5)
def _read_next_meetings() -> List[Any]:
    return read_next_meetings()


@periodic(5)
def _read_current_meetings() -> List[Any]:
    return read_current_meetings()
