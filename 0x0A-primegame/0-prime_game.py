#!/usr/bin/python3
'''Prime Number Game.'''


def find_primes(limit):
    '''Generate a list of prime numbers up to a given limit'''
    primes = []
    sieve = [True] * (limit + 1)
    for potentialPrime in range(2, limit + 1):
        if sieve[potentialPrime]:
            primes.append(potentialPrime)
            for m in range(potentialPrime, limit + 1, potentialPrime):
                sieve[m] = False
    return primes


def isWinner(numRounds, roundValues):
    '''
    Determine the victoriouso
    '''
    if not numRounds or not roundValues:
        return None
    mariapts = benspts = 0
    for ee in range(numRounds):
        primes = find_primes(roundValues[ee])
        if len(primes) % 2 == 0:
            benspts += 1
        else:
            mariapts += 1
    if mariapts > benspts:
        return "Maria"
    elif benspts > mariapts:
        return "Ben"
    return None
