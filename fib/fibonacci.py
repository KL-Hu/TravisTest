#!/bin/python
# fibonacci.py
'''This is fib function c'''
def fibonacci(webhook):
    ''' calculate fibonacci series '''
    first, second = 0, 1
    while first < webhook:
        yield first
        first, second = second, first + second
