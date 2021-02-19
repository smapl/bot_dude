import datetime


now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

week_number = datetime.date(year, month, day).isocalendar()[1]
print()