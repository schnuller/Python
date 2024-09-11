import datetime as dt

now = dt.datetime.now()


year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()

hour = 17
minute = 0

td = dt.datetime(year(now), month(now), day(now), hour, minute, 0)
#td = dt.datetime(year(now), month(now), day(now), dt.datetime.time(hour=17, minute=0), 0)

u = lambda x, y: x - dt.timedelta(minutes=y)
o = lambda x, y: x + dt.timedelta(minutes=y)


print(u(td, 20), o(td, 20), t(now))

if now > u(td,20) and now < o(td,20):
    print("yes")