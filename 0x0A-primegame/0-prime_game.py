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
        dp = [False] * (n + 1)
        dp[0] = dp[1] = False

        # Precompute a list of primes up to n
        primes = sieveOfEratosthenes(n)

        # Dynamic programming approach
        for i in range(2, n + 1):
            for prime in primes:
                if prime > i:
                    break
                if not dp[i - prime]:
                    dp[i] = True
                    break

        if dp[n]:
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


def sieveOfEratosthenes(n):
    """
    Sieve of Eratosthenes to find all prime numbers up to n
    """
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return primes
