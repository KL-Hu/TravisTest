#!/bin/python
# fibonacci.py
'''This is fib function'''
def fibonacci(max):
    first, second = 0, 1
    while first < max:
        yield first
        first, second = second, first + second
