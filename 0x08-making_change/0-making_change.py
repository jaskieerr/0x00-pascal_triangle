#!/usr/bin/python3
'''Change comes from within'''


def makeChange(coins, total):
    '''the change'''
    if total < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        n = total // coin
        total -= n * coin
        count += n
    return count if total == 0 else -1
