<a href="https://codecov.io/github/jalvaradosegura/date-operations" >
    <img src="https://codecov.io/github/jalvaradosegura/date-operations/branch/main/graph/badge.svg?token=TO89NFDQ79"/> 
</a>

---

# date-operations

---

## Usage
### Get days, months or years between 2 dates
With these functions you get the amount of days, months or years between 2 days. In the case of months and years, there needs to be a full month or year between the dates in order to make it count:

```py
from date_operations import (
    days_between,
    months_between,
    years_between,
)

days_between("2023-01-01", "2023-01-02")  # 1

months_between("2023-01-01", "2023-02-01")  # 1
months_between("2023-01-31", "2023-02-01")  # 0

years_between("2023-01-01", "2024-01-01")  # 1
years_between("2023-12-31", "2024-01-01")  # 0
```

### Get months or years started between 2 dates
If you need to know how many months or years have started between 2 dates (not caring about full months or years), these are the functions to use:

```py
from date_operations import (
    months_started_between,
    years_started_between,
)

months_started_between("2023-01-01", "2023-02-01")  # 1
months_started_between("2023-01-31", "2023-02-01")  # 1

years_started_between("2023-01-01", "2024-01-01")  # 1
years_started_between("2023-12-31", "2024-01-01")  # 1
```
