#!/usr/bin/python3
"""Making Change."""


def makeChange(coins, total):
    """makeChange function

    Arguments:
        coins {list} -- list of the coins 
        total {int} -- total amount to make change for

    Returns:
        [type] -- [description]
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each total amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all the coins and calculate the minimum number of coins for each amount
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
