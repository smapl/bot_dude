import datetime


now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

now_new = datetime.date(year, month, day)
any_date = datetime.date(2021, 2, 19)
print(now_new == any_date)