import math
POW = 5

pows = {}
pows10s = {}

for i in range(10):
    pows[i] = i**POW

for i in range(10):
    pows10s[i] = 10**i

def clog10(n):
    if n < 10:
        return 1
    elif n < 100:
        return 2
    elif n < 1000:
        return 3
    elif n < 10000:
        return 4
    elif n < 100000:
        return 5
    elif n < 1000000:
        return 6
    elif n < 10000000:
        return 7


def check(n):
#    return sum(pows[int(x)] for x in str(n)) == n
    return sum(
        [
            ((x % pows10s[n] - (x % pows10s[n-1]))//pows10s[n-1])**5 
            for n in range(1, 1 + clog10(x))
        ]
    ) == x


s = 0
x = 2
lim = (pows[9])*clog10(x)

while lim > x:
    if check(x):
        s += x
    x += 1

    if x >= lim:
        lim = (pows[9])*clog10(x)

print(s)
