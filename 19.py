from datetime import date, timedelta
from dateutil.relativedelta import relativedelta # extension to datetime module

START = date(1901, 1, 1)
END = date(2000, 12, 31)

num_sundays = 0
cur = START
while (cur < END):
    if (6 == cur.weekday()):
        num_sundays += 1
    cur += relativedelta(months=1)

print num_sundays
