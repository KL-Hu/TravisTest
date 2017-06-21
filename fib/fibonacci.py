#!/bin/python
# fibonacci.py
'''This is fib function'''
def fibonacci(min):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < min:
        yield first
        first, second = second, first + second
