import math


def site(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


x1, y1, x2, y2, x3, y3 = map(int, input().split(' '))
a = site(x1, y1, x2, y2)
b = site(x3, y3, x2, y2)
c = site(x1, y1, x3, y3)
print(f"P: {a+b+c}")
p = (a+b+c)/2
print(f"S: {math.sqrt(p*(p-a)*(p-b)*(p-c))}")
