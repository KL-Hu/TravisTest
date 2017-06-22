#!/bin/python
# fibonacci.py
'''This is fib function'''
def fibonacci(webhook_1):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < webhook_1:
        yield first
        first, second = second, first + second
