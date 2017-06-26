#!/bin/python
# fibonacci.py
''' fib function test pull request'''
def fibonacci(avery):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < avery:
        yield first
        first, second = second, first + second
