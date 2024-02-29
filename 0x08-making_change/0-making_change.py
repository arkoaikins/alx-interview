#!/usr/bin/python3
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

    # Initialize an array to store the
    # minimum number of coins needed for each amount
    change = [float("inf")] * (total + 1)
    change[0] = 0  # No coins needed for a total of 0

    # Iterate through each coin denomination
    for coin in coins:
        # Iterate through all possible amounts up to the total
        for amount in range(coin, total + 1):
            # Update the minimum number of coins needed for the current amount
            change[amount] = min(change[amount], change[amount - coin] + 1)

    # Return the minimum number of coins needed
    # for the total, or -1 if impossible
    return change[total] if change[total] != float("inf") else -1
