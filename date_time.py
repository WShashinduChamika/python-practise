import datetime

b_day = datetime.date(1999,11,5)
print(b_day)

today = datetime.date.today()
print(today)

print(b_day.strftime("%A, %B %d, %Y"))

age = today - b_day
print(age)

print(today.weekday())

print(today.isoweekday())

print(today.isoformat())

t = datetime.time(9, 30, 45, 10000)

print(t)

print(t.hour)

d = datetime.datetime.today()
print(d)

t_delta = datetime.timedelta(days=20)
t_delta2 = datetime.timedelta(hours=20)
print(today + t_delta)
print(today - t_delta2)