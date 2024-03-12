#!/usr/bin/python3
"""
solve the prime game challenge
"""


def isWinner(x, nums):
    """
    This function determines the winner of a prime number removal game.

    Args:
      x: The number of rounds played.
      nums: A list of integers representing the starting set of numbers
      for each round.

    Returns:
     A string indicating the winner ("Maria" or "Ben") or None if the winner
     cannot be determined.
    """
    winners = []

    for n in nums:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        # Sieve of Eratosthenes to find all prime numbers up to n
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        maria_turn = True
        while True:
            maria_can_move = False
            ben_can_move = False

            # Check if Maria can make a move
            for i in range(2, n + 1):
                if primes[i]:
                    maria_can_move = True
                    primes[i] = False
                    for j in range(i * i, n + 1, i):
                        primes[j] = False
                    break

            # Check if Ben can make a move
            for i in range(2, n + 1):
                if primes[i]:
                    ben_can_move = True
                    primes[i] = False
                    for j in range(i * i, n + 1, i):
                        primes[j] = False
                    break

            if not maria_can_move or not ben_can_move:
                break

        if maria_can_move:
            winners.append("Maria")
        else:
            winners.append("Ben")

    # Count the number of wins for each player
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
