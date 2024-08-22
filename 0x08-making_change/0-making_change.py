#!/usr/bin/python3
"""0-making_change.py"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given total amount."""
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    index = 0
    sorted_coins = sorted(coins, reverse=True)
    y = len(coins)
    while rem > 0:
        if index >= y:
            return - 1
        if rem - sortef_coins[index] >=0:
            rem -= sorted_coins[index]
            coins_count += 1
        else:
            index += 1

    return coins_count
