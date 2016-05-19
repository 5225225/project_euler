import itertools


def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

print(max([x*y for x, y in itertools.product(range(100, 999), repeat=2) if is_palindrome(x*y)]))
