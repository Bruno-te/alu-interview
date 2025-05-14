#!/usr/bin/python3
"""
Module for calculating the fewest number of operations
needed to result in exactly n 'H' characters in a text file.
Only 'Copy All' and 'Paste' operations are allowed.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to get n 'H' characters.

    Args:
        n (int): The target number of 'H' characters

    Returns:
        int: Minimum number of operations, or 0 if n is less than 2
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

