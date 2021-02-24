from datetime import datetime, date, time

a = time(13, 47)
b = time(12, 11)

res = (datetime.combine(date.today(), a) - datetime.combine(date.today(), b)).seconds
print()