#!/usr/bin/env python
import util

for index, item in enumerate(util.fib(), start=1):
    if item >= 10**999:
        print(index)
        break
