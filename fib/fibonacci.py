#!/bin/python
# fibonacci.py
'''This is fib function'''
def fibonacci(maxx):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < maxx:
        yield first
        first, second = second, first + second
