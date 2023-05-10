from typing import Tuple

import pytest

from date_operations import (
    days_between,
    months_between,
    months_started_between,
    years_between,
    years_started_between,
)


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
