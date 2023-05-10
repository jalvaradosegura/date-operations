from datetime import datetime

from dateutil.relativedelta import relativedelta


def days_between(date_1: str, date_2: str) -> int:
    return abs(
        datetime.strptime(date_1, "%Y-%m-%d") - datetime.strptime(date_2, "%Y-%m-%d")
    ).days


def months_between(date_1: str, date_2: str) -> int:
    delta = relativedelta(
        datetime.strptime(date_1, "%Y-%m-%d"), datetime.strptime(date_2, "%Y-%m-%d")
    )
    return abs(delta.months + (12 * delta.years))


def months_started_between(date_1: str, date_2: str) -> int:
    months_started = (
        datetime.strptime(date_1, "%Y-%m-%d").month
        - datetime.strptime(date_2, "%Y-%m-%d").month
    )
    years_started = (
        datetime.strptime(date_1, "%Y-%m-%d").year
        - datetime.strptime(date_2, "%Y-%m-%d").year
    )
    return abs(years_started * 12 + months_started)


def years_between(date_1: str, date_2: str) -> int:
    delta = relativedelta(
        datetime.strptime(date_1, "%Y-%m-%d"), datetime.strptime(date_2, "%Y-%m-%d")
    )
    return abs(delta.years)


def years_started_between(date_1: str, date_2: str) -> int:
    years_started = (
        datetime.strptime(date_1, "%Y-%m-%d").year
        - datetime.strptime(date_2, "%Y-%m-%d").year
    )
    return abs(years_started)
