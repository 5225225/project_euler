#!/usr/bin/env python
import util
print(sum([x for x in util.fib(4000000) if x % 2 == 0]))
