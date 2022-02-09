import datetime

now = datetime.datetime.now()

for x in range(0, 1000):
    d = {}
    for k in range(0, 2000):
        a = []
        for i in range(99, -1, -1):
            a.append(i)
        d[k] = a

print(datetime.datetime.now() - now)
