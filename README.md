<a href="https://codecov.io/github/jalvaradosegura/date-operations" >
    <img src="https://codecov.io/github/jalvaradosegura/date-operations/branch/main/graph/badge.svg?token=TO89NFDQ79"/>
</a>

---

# date-operations
🗓 Easy to use functions for common date operations

---

## Installation

```console
pip install date-operations
```

## Usage
### Days between 2 dates
Get the amount of days between 2 dates:

```py
from date_operations import days_between

days_between("2023-01-01", "2023-01-02")  # 1
days_between("01 01 2023", "01/01/2024")  # 365

# You can omit the day:
days_between("jan-2023", "01/02/2023")  # 31
```

### Months between 2 dates
Get the amount of full months between 2 dates:

```py
from date_operations import months_between

months_between("01 05 2023", "31 05 2023")  # 0
months_between("01-05-2023", "01-06-2023")  # 1
months_between("10/05/2022", "10/05/2023")  # 12
months_between("10-may-2022", "09-may-2023")  # 11

# You can omit the day:
months_between("05-2023", "06-2023")  # 1
```

### Months started between 2 dates
Get the amount of months started between 2 dates:

```py
from date_operations import months_started_between

months_started_between("31 05 2023", "01 06 2023")  # 1
months_started_between("01-05-2023", "01-06-2023")  # 1
months_started_between("31/12/2022", "01/01/2023")  # 1
```

### Years between 2 dates
Get the amount of full years between 2 dates:

```py
from date_operations import years_between

years_between("15 01 2022", "15 01 2023")  # 1
years_between("15-01-2022", "14-01-2023")  # 0
years_between("31/12/2022", "01/01/2023")  # 0

# You can omit the day:
years_between("05/2023", "06/2023")  # 0
years_between("05/2023", "01/2024")  # 0
years_between("05/2023", "05/2024")  # 1
```

### Years started between 2 dates
Get the amount of years started between 2 dates:

```py
from date_operations import years_started_between

years_started_between("31 12 2022", "01 01 2023")  # 1
years_started_between("01-01-2023", "31-12-2023")  # 0
years_started_between("31/12/2022", "01/01/2024")  # 2
```

### Date formats
Date formats are inferred given [this priority list](https://github.com/jalvaradosegura/date-operations/blob/main/date_operations/settings.py). If the format of your date is not within the list you can add it or explicitly indicate the format of a given date. The formats added to the list are given priority.

```py
from date_operations import months_between

months_between("01-01", "01-02", format_1="%d-%m", format_2="%d-%m")  # 1
months_between("01-01", "01-02", extra_formats=["%d-%m"])  # 1
```
> The same parameters are used for all the functions.
