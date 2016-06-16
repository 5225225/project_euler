import math
POW = 5

pows = {}
pows10s = {}

for i in range(10):
    pows[i] = i**POW

for i in range(10):
    pows10s[i] = 10**i

def check(n):
#    return sum(pows[int(x)] for x in str(n)) == n
    return sum(
        [
            ((x % pows10s[n] - (x % pows10s[n-1]))//pows10s[n-1])**5 
            for n in range(1, 7)
        ]
    ) == x


s = 0
x = 2
lim = (pows[9])*6

while lim > x:
    if check(x):
        s += x
    x += 1

print(s)
