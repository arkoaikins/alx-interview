#!/usr/bin/python3
from sympy import sieve


def isWinner(x, nums, cache={}):
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
