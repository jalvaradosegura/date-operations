from datetime import datetime
from typing import List, Optional

from dateutil.relativedelta import relativedelta

from .settings import date_format_list


def days_between(
    date_1: str,
    date_2: str,
    format_1: Optional[str] = None,
    format_2: Optional[str] = None,
    extra_formats: Optional[List[str]] = None,
) -> int:
    return abs(
        _to_datetime(date_1, format_1, extra_formats)
        - _to_datetime(date_2, format_2, extra_formats)
    ).days


def months_between(
    date_1: str,
    date_2: str,
    format_1: Optional[str] = None,
    format_2: Optional[str] = None,
    extra_formats: Optional[List[str]] = None,
) -> int:
    delta = relativedelta(
        _to_datetime(date_1, format_1, extra_formats),
        _to_datetime(date_2, format_2, extra_formats),
    )
    return abs(delta.months + (12 * delta.years))


def months_started_between(
    date_1: str,
    date_2: str,
    format_1: Optional[str] = None,
    format_2: Optional[str] = None,
    extra_formats: Optional[List[str]] = None,
) -> int:
    ddate_1 = _to_datetime(date_1, format_1, extra_formats)
    ddate_2 = _to_datetime(date_2, format_2, extra_formats)
    months_started = ddate_1.month - ddate_2.month
    years_started = ddate_1.year - ddate_2.year
    return abs(years_started * 12 + months_started)


def years_between(
    date_1: str,
    date_2: str,
    format_1: Optional[str] = None,
    format_2: Optional[str] = None,
    extra_formats: Optional[List[str]] = None,
) -> int:
    delta = relativedelta(
        _to_datetime(date_1, format_1, extra_formats),
        _to_datetime(date_2, format_2, extra_formats),
    )
    return abs(delta.years)


def years_started_between(
    date_1: str,
    date_2: str,
    format_1: Optional[str] = None,
    format_2: Optional[str] = None,
    extra_formats: Optional[List[str]] = None,
) -> int:
    years_started = (
        _to_datetime(date_1, format_1, extra_formats).year
        - _to_datetime(date_2, format_2, extra_formats).year
    )
    return abs(years_started)


def _to_datetime(
    date: str, _format: Optional[str], extra_formats: Optional[List[str]]
) -> datetime:
    if _format is None:
        _format = _guess_date_format(date, _format)

    if _format is None:
        raise ValueError(f"Couldn't guess the date format for date: {date}.")

    return datetime.strptime(date, _format)


def _guess_date_format(
    date: str, extra_formats: Optional[List[str]] = None
) -> Optional[str]:
    if extra_formats is None:
        extra_formats = []

    date_formats = extra_formats + date_format_list

    for date_format in date_formats:
        try:
            datetime.strptime(date, date_format)
        except ValueError:
            pass
        else:
            return date_format

    return None
