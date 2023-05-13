from datetime import datetime
from functools import wraps
from typing import Callable, List, Optional

from dateutil.relativedelta import relativedelta

from .settings import date_format_list


def guess_date_format(func: Callable[[str, str, str, str, Optional[List[str]]], int]):
    @wraps(func)
    def _wrapper(
        date_1: str,
        date_2: str,
        format_1: Optional[str] = None,
        format_2: Optional[str] = None,
        extra_formats: Optional[List[str]] = None,
    ) -> int:
        if format_1 is None:
            format_1 = _guess_date_format(date_1, extra_formats)

            if format_1 is None:
                raise ValueError(
                    f"Couldn't guess the date format for date_1: {date_1}."
                )

        if format_2 is None:
            format_2 = _guess_date_format(date_2, extra_formats)

            if format_2 is None:
                raise ValueError(
                    f"Couldn't guess the date format for date_2: {date_2}."
                )

        return func(date_1, date_2, format_1, format_2, extra_formats)

    return _wrapper


@guess_date_format
def days_between(
    date_1: str,
    date_2: str,
    format_1: str,
    format_2: str,
    extra_formats: Optional[List[str]] = None,
) -> int:
    return abs(
        datetime.strptime(date_1, format_1) - datetime.strptime(date_2, format_2)
    ).days


@guess_date_format
def months_between(
    date_1: str,
    date_2: str,
    format_1: str,
    format_2: str,
    extra_formats: Optional[List[str]] = None,
) -> int:
    delta = relativedelta(
        datetime.strptime(date_1, format_1), datetime.strptime(date_2, format_2)
    )
    return abs(delta.months + (12 * delta.years))


@guess_date_format
def months_started_between(
    date_1: str,
    date_2: str,
    format_1: str,
    format_2: str,
    extra_formats: Optional[List[str]] = None,
) -> int:
    months_started = (
        datetime.strptime(date_1, format_1).month
        - datetime.strptime(date_2, format_2).month
    )
    years_started = (
        datetime.strptime(date_1, format_1).year
        - datetime.strptime(date_2, format_2).year
    )
    return abs(years_started * 12 + months_started)


@guess_date_format
def years_between(
    date_1: str,
    date_2: str,
    format_1: str,
    format_2: str,
    extra_formats: Optional[List[str]] = None,
) -> int:
    delta = relativedelta(
        datetime.strptime(date_1, format_1), datetime.strptime(date_2, format_2)
    )
    return abs(delta.years)


@guess_date_format
def years_started_between(
    date_1: str,
    date_2: str,
    format_1: str,
    format_2: str,
    extra_formats: Optional[List[str]] = None,
) -> int:
    years_started = (
        datetime.strptime(date_1, format_1).year
        - datetime.strptime(date_2, format_2).year
    )
    return abs(years_started)


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
