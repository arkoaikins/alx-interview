#!/usr/bin/python3
def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primes[p]]

    def play_game(n):
        primes = sieve_of_eratosthenes(n)
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

        return "Maria" if maria_turn else "Ben"

    wins = [play_game(n) for n in nums]
    maria_wins = wins.count("Maria")
    ben_wins = wins.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None