#!/bin/python
# fibonacci.py
def fibonacci(max):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < max:
        yield first
        first, second = second, first + second