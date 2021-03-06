import math


def fib(up_to=None):
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        if up_to is None:
            yield a
        else:
            if a <= up_to:
                yield a
            else:
                break


def factors(x):
    factors = []
    while True:
        for y in range(2, int(math.sqrt(x)) + 1):
            if x % y == 0:
                x = x // y
                factors.append(y)
                break
        else:
            factors.append(x)
            return factors


def is_palindrome(x):
    return str(x) == str(x)[::-1]
