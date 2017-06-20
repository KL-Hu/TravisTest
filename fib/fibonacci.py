#!/bin/python
# fibonacci.py
'''This is fib function'''
def fibonacci(value):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < value:
        yield first
        first, second = second, first + second
