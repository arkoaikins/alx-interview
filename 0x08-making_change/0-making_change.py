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

    if total <= 0:
        return 0

    # Sort the coins in ascending order
    coins.sort()

    # Initialize an array to store the minimum
    # number of coins needed for each amount
    change = [float("inf")] * (total + 1)
    change[0] = 0  # No coins needed for a total of 0

    # Iterate through each coin denomination
    for coin in coins:
        # Iterate through all possible amounts starting from the coin value
        for amount in range(coin, total + 1):
            # Check if using the current coin
            # leads to a smaller number of coins needed
            if change[amount - coin] + 1 < change[amount]:
                change[amount] = change[amount - coin] + 1

    # Return the minimum number of coins
    # needed for the total, or -1 if impossible
    return change[total] if change[total] != float("inf") else -1
