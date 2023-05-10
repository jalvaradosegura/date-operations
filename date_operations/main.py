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


def years_between(date_1: str, date_2: str) -> int:
    delta = relativedelta(
        datetime.strptime(date_1, "%Y-%m-%d"), datetime.strptime(date_2, "%Y-%m-%d")
    )
    return abs(delta.years)
