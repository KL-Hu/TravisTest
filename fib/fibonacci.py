#!/bin/python
# fibonacci.py
'''This is fib function'''
def fibonacci(max_value):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < max_value:
        yield first
        first, second = second, first + second
