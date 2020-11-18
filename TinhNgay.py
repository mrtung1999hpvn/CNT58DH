import datetime
d, m, y = map(int, input().split())
d = str((datetime.date(y, m, d) - datetime.date(y, 1, 1)))
print(int(d.split(' ')[0])+1)
