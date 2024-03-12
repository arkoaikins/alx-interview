#!/usr/bin/python3
"""
solve the prime game challenge
"""


def is_prime(n):
    """Function to check for prime number"""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_primes(n):
    """Function to retrieve prime numbers up to n"""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Function to determine the winner of the Prime Game"""
    maria = 0
    ben = 0

    for n in nums:
        primes = get_primes(n)
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
