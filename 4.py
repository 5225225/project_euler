#!/usr/bin/env python
import itertools
import util

print(max(
    [x*y for x, y in
        itertools.product(range(100, 999), repeat=2) if
        util.is_palindrome(x*y)]
))
