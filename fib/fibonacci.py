#!/bin/python
# fibonacci.py
'''This is fib function'''
def fibonacci(webhook_a):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < webhook_a:
        yield first
        first, second = second, first + second
