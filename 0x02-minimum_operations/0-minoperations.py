#!/usr/bin/python3
"""
Minimum Operations
This module contains a method that calculates the fewest number of operations
needed to result in exactly n 'H' characters in a text file. The operations
allowed are "Copy All" and "Paste". The goal is to find the minimum number of
these operations required to achieve exactly n 'H' characters.

Prototype: def minOperations(n)
Returns: an integer representing the minimum number of operations
If n is impossible to achieve, the method returns 0.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to obtain exactly
    n 'H' characters in a text file.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed to achieve n 'H' characters,
         or 0 if it's impossible to achieve n.
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
