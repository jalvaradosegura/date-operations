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
    """
    Returns the number of days between two dates.

    This function tries to guess the format of the dates automatically based on a
    list of formats. You can also explicitly provide the format for each date.

    Moreover, you can indicate extra formats that are added to the list of formats.
    These extra formats are given more priority than the default ones.

    In addition, the function considers a special case where the input dates are missing
    the "day" but have the "year" and the "month". In this case, the function considers
    the dates as the first day of the month.
    """
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
    """
    Returns the number of full months between two dates.

    Full months in this case means:
    - months_between("01 05 2023", "31 05 2023")  # 0
    - months_between("01-05-2023", "01-06-2023")  # 1
    - months_between("10/05/2022", "10/05/2023")  # 12
    - months_between("10-may-2022", "09-may-2023")  # 11

    You can omit the day:
    - months_between("05-2023", "06-2023")  # 1

    This function tries to guess the format of the dates automatically based on a
    list of formats. You can also explicitly provide the format for each date.

    Moreover, you can indicate extra formats that are added to the list of formats.
    These extra formats are given more priority than the default ones.
    """
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
    """
    Returns the number of months started between two dates.

    Months started in this case means:
    - months_started_between("31-05-2023", "01-06-2023")  # 1
    - months_started_between("01-05-2023", "01-06-2023")  # 1
    - months_started_between("31-12-2022", "01-01-2023")  # 1

    You can omit the day and in that case this function behaves just like
    `months_between`.

    This function tries to guess the format of the dates automatically based on a
    list of formats. You can also explicitly provide the format for each date.

    Moreover, you can indicate extra formats that are added to the list of formats.
    These extra formats are given more priority than the default ones.
    """
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
    """
    Returns the number of full years between two dates.

    Full years in this case means:
    - years_between("15 01 2022", "15 01 2023")  # 1
    - years_between("15-01-2022", "14-01-2023")  # 0
    - years_between("31/12/2022", "01/01/2023")  # 0

    You can omit the day:
    - years_between("05/2023", "06/2023")  # 0
    - years_between("05/2023", "01/2024")  # 0
    - years_between("05/2023", "05/2024")  # 1

    This function tries to guess the format of the dates automatically based on a
    list of formats. You can also explicitly provide the format for each date.

    Moreover, you can indicate extra formats that are added to the list of formats.
    These extra formats are given more priority than the default ones.
    """
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
    """
    Returns the number of years started between two dates.

    Years started in this case means:
    - years_started_between("31-12-2022", "01-01-2023")  # 1
    - years_started_between("01-01-2023", "31-12-2023")  # 0
    - years_started_between("31-12-2022", "01-01-2024")  # 2

    You can omit the day:
    - years_started_between("12-2022", "01-2024")  # 2

    This function tries to guess the format of the dates automatically based on a
    list of formats. You can also explicitly provide the format for each date.

    Moreover, you can indicate extra formats that are added to the list of formats.
    These extra formats are given more priority than the default ones.
    """
    years_started = (
        _to_datetime(date_1, format_1, extra_formats).year
        - _to_datetime(date_2, format_2, extra_formats).year
    )
    return abs(years_started)


def _to_datetime(
    date: str, _format: Optional[str], extra_formats: Optional[List[str]]
) -> datetime:
    if _format is None:
        _format = _guess_date_format(date, extra_formats)

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
