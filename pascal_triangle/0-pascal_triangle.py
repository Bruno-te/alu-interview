#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle with n rows.
    Returns a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Start each row with 1
        row = [1]
        # Compute the in-between values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        # End each row with 1
        row.append(1)
        triangle.append(row)

    return triangle

