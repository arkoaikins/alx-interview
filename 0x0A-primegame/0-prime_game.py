#!/usr/bin/python3
from sympy import sieve

"""
solve the prime game challenge
"""


def isWinner(x, nums, cache={}):
    """
      This function determines the winner of a prime number removal game.

    Args:
        x: The number of rounds played.
        nums: A list of integers representing the
        starting set of numbers for each round.

    Returns:
        A string indicating the winner ("Maria" or "Ben") or
        None if the winner cannot be determined.
    """
    if x in cache:
        return cache[x]

    winners = []

    for n in nums:
        primes = list(sieve.primerange(2, n + 1))
        maria_turn = True

        while primes:
            maria_can_move = not primes[0] % 2
            ben_can_move = not primes[-1] % 2
            if maria_turn:
                if maria_can_move:
                    primes.pop(0)
                else:
                    break
            else:
                if ben_can_move:
                    primes.pop()
                else:
                    break
            maria_turn = not maria_turn

        if maria_turn:
            winners.append("Maria")
        else:
            winners.append("Ben")

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        result = "Maria"
    elif ben_wins > maria_wins:
        result = "Ben"
    else:
        result = None

    cache[x] = result
    return result
