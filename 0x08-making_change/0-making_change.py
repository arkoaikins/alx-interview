#!/usr/bin/python3
"""
This function returns the fewest number
of coins needed to make a given total.
"""


def makeChange(coins, total):
    """
    This function returns the fewest number
    of coins needed to make a given total.

    Args:
        coins: A list of coin denominations.
        total: The target amount to make change for.

    Returns:
        The minimum number of coins needed
        to make the total, or -1 if it's impossible.
    """

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the fewest number of coins needed for each total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the fewest number of coins needed for the given total
    return dp[total] if dp[total] != float("inf") else -1
