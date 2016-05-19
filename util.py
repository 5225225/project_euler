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
