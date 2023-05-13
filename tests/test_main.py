from typing import List, Optional, Tuple

import pytest

from date_operations import (
    days_between,
    months_between,
    months_started_between,
    years_between,
    years_started_between,
)
from date_operations.main import _guess_date_format


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023-01-01", "2023-01-11"), 10],
        [("2023-01-01", "2023-01-01"), 0],
        [("2023-01-01", "2023-02-01"), 31],
        [("2023-01-01", "2024-01-01"), 365],
    ],
)
def test_days_between(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert days_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023 01 01", "20230111"), 10],
        [("2023/01/01", "01-01-2023"), 0],
        [("01/01/2023", "01-feb-2023"), 31],
        [("01 jan 2023", "01/jan/2024"), 365],
    ],
)
def test_days_between_guess_formats(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert days_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023-01-01", "2023-02-01"), 1],
        [("2023-02-01", "2023-01-01"), 1],
        [("2023-01-01", "2023-01-01"), 0],
        [("2023-01-01", "2024-01-01"), 12],
        [("2023-01-31", "2023-02-01"), 0],
    ],
)
def test_months_between(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert months_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023 01 01", "20230201"), 1],
        [("2023/02/01", "01-01-2023"), 1],
        [("2023-01", "2023-01"), 0],
        [("01-2023", "jan-2024"), 12],
        [("jan/2023", "feb 2023"), 1],
    ],
)
def test_months_between_guess_format(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert months_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023-01-31", "2023-02-01"), 1],
        [("2023-02-01", "2023-01-01"), 1],
        [("2023-12-31", "2024-01-01"), 1],
        [("2024-01-01", "2023-12-31"), 1],
        [("2023-01-01", "2023-02-01"), 1],
        [("2023-02-01", "2023-01-01"), 1],
        [("2023-01-01", "2023-01-01"), 0],
        [("2023-01-01", "2024-01-01"), 12],
    ],
)
def test_months_started_between(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert months_started_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023-01-31", "2023/02/01"), 1],
        [("2023 02 01", "01-2023"), 1],
        [("20231231", "jan 2024"), 1],
    ],
)
def test_months_started_between_guess_format(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert months_started_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023-01-01", "2024-01-01"), 1],
        [("2023-01-01", "2022-01-01"), 1],
        [("2023-01-01", "2023-01-01"), 0],
        [("2023-01-01", "2030-01-01"), 7],
        [("2023-12-31", "2024-01-01"), 0],
    ],
)
def test_years_between(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert years_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023/01/01", "2024 01 01"), 1],
        [("20230101", "2022-01"), 1],
        [("2023-01", "202301"), 0],
        [("2023-01-01", "2030-01"), 7],
        [("2023-12", "2024-01"), 0],
        [("2023-12", "2024-12"), 1],
    ],
)
def test_years_between_guess_format(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert years_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023-12-31", "2024-01-01"), 1],
        [("2023-01-01", "2022-12-31"), 1],
        [("2023-01-01", "2030-01-01"), 7],
        [("2023-01-01", "2024-01-01"), 1],
        [("2023-01-01", "2022-01-01"), 1],
        [("2023-01-01", "2023-01-01"), 0],
        [("2023-01-01", "2030-01-01"), 7],
    ],
)
def test_years_started_between(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert years_started_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "dates, result",
    [
        [("2023-12", "2024-01"), 1],
        [("2023 01 01", "2022/12/31"), 1],
        [("jan-2023", "01-01-2030"), 7],
    ],
)
def test_years_started_between_guess_format(dates: Tuple[str, str], result: int):
    date_1, date_2 = dates
    assert years_started_between(date_1, date_2) == result


@pytest.mark.parametrize(
    "date, date_format",
    [
        ["10-10-2010", "%d-%m-%Y"],
        ["10/10/2010", "%d/%m/%Y"],
        ["10 10 2010", "%d %m %Y"],
        ["10102010", "%d%m%Y"],
        ["2010-10-10", "%Y-%m-%d"],
        ["2010/10/10", "%Y/%m/%d"],
        ["10-2010", "%m-%Y"],
        ["10/2010", "%m/%Y"],
        ["10 2010", "%m %Y"],
        ["102010", "%m%Y"],
        ["2010-10", "%Y-%m"],
        ["2010/10", "%Y/%m"],
        ["2010 10", "%Y %m"],
        ["201010", "%Y%m"],
        ["10-oct-2010", "%d-%b-%Y"],
        ["10/oct/2010", "%d/%b/%Y"],
        ["10 oct 2010", "%d %b %Y"],
        ["10oct2010", "%d%b%Y"],
        ["oct-2010", "%b-%Y"],
        ["oct/2010", "%b/%Y"],
        ["oct 2010", "%b %Y"],
        ["oct2010", "%b%Y"],
        ["unknown", None],
    ],
)
def test_guess_date_format(date: str, date_format: Optional[str]):
    assert _guess_date_format(date) == date_format


@pytest.mark.parametrize(
    "date, date_format, extra_formats",
    [
        ["2010 10 10", "%Y %m %d", ["%Y %m %d"]],
        ["20101010", "%Y%m%d", ["%Y%m%d"]],
        ["10 10 2010", "%m %d %Y", ["%m %d %Y"]],
        ["10102010", "%m%d%Y", ["%m%d%Y"]],
        ["10-10-2010", "%m-%d-%Y", ["%m-%d-%Y"]],
        ["10/10/2010", "%m/%d/%Y", ["%m/%d/%Y"]],
    ],
)
def test_guess_date_format_with_extra_formats(
    date: str, date_format: str, extra_formats: List[str]
):
    assert _guess_date_format(date, extra_formats) == date_format


def test_guess_date_format_decorator_no_guess_date_1():
    date_1 = "invalid-date"
    date_2 = "2023-01-11"

    with pytest.raises(
        ValueError,
        match=f"Couldn't guess the date format for date_1: {date_1}.",
    ):
        days_between(date_1, date_2)


def test_guess_date_format_decorator_no_guess_date_2():
    date_1 = "2023-01-11"
    date_2 = "invalid-date"

    with pytest.raises(
        ValueError,
        match=f"Couldn't guess the date format for date_2: {date_2}.",
    ):
        days_between(date_1, date_2)
