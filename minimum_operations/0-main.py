#!/usr/bin/python3
"""
Main file for testing minOperations
"""

minOperations = __import__('0-minoperations').minOperations

test_cases = [21, 19170307, 972, 1, 0, -12, 2147483640]

for n in test_cases:
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

