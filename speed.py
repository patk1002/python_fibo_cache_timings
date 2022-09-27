#! /usr/bin/env python
"""
Timings for the number of Fibonacci iterations given as sys.argv[1].
Some code from he Single Most Useful Decorator in Python
  at https://www.youtube.com/watch?v=DnKxKFXB4NQ
Some code from Timeit in Python with Examples
  at https://www.geeksforgeeks.org/timeit-python-examples/
"""

from functools import lru_cache
import sys
import timeit

@lru_cache(maxsize=0)
def fib0(n):
    if n <=1:
        return n 
    return fib0(n-1) + fib0(n-2)

@lru_cache(maxsize=1)
def fib1(n):
    if n <=1:
        return n 
    return fib1(n-1) + fib1(n-2)

@lru_cache(maxsize=2)
def fib2(n):
    if n <=1:
        return n 
    return fib2(n-1) + fib2(n-2)

setup_code0 = "from __main__ import fib0"
setup_code1 = "from __main__ import fib1"
setup_code2 = "from __main__ import fib2"

testcode0 = "for i in range(n+1):\n    print(i, fib0(i))"
testcode1 = "for i in range(n+1):\n    print(i, fib1(i))"
testcode2 = "for i in range(n+1):\n    print(i, fib2(i))"

def time_fib0(n, title, setup_code):
    print(
        n,
        title,
        timeit.timeit(
            setup = setup_code,
            stmt = f"n={n}\n{testcode0}",
            number=1,
        )
    )
def time_fib1(n, title, setup_code):
    print(
        n,
        title,
        timeit.timeit(
            setup = setup_code,
            stmt = f"n={n}\n{testcode1}",
            number=1,
        )
    )
def time_fib2(n, title, setup_code):
    print(
        n,
        title,
        timeit.timeit(
            setup = setup_code,
            stmt = f"n={n}\n{testcode2}",
            number=1,
        )
    )

def main() -> None:
    if len(sys.argv) == 2:
        n = sys.argv[1]
    else:
        print("Give a postitive integer on the command line for the number of iterations.")
        sys.exit()
    time_fib0(n, "Fibonacci iterations with lru_cache = 0 timing:", setup_code0)
    time_fib1(n, "Fibonacci iterations with lru_cache = 1 timing:", setup_code1)
    time_fib2(n, "Fibonacci iterations with lru_cache = 2 timing:", setup_code2)
    print()


if __name__ == "__main__":
    print("Beginning of main program...")
    main()
