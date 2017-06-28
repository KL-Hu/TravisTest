''' Unitest for fib '''
#!/bin/python
# fibonacci_test.py
from nose.tools import assert_equal
from fib.fibonacci import fibonacci

def test_fib():
    ''' Test function for fib() pull request 091'''
    myfib = fibonacci(100)
    series = []
    test_case = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in myfib:
        series.append(i)
    assert_equal(series, test_case)