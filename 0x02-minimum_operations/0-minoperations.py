#!/usr/bin/python3
"""
write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """calculates the fewest number of operations needed """
    if n <= 1:
        return 0
    fact = 2
    operation = 0
    while fact <= n:
        if n % fact == 0:
            operation += fact
            n //= fact
        else:
            fact += 1
    return operation
