#!/usr/bin/python3
'''Prime Number Game'''

def find_primes(limit):
    '''Generate a list of prime numbers up to a given limit'''
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num, limit + 1, num):
                sieve[multiple] = False
    return primes

def determine_winner(rounds, numbers):
    '''Determine the winner of the prime number game'''
    if not rounds or not numbers:
        return None

    maria_score = 0
    ben_score = 0

    for round_idx in range(rounds):
        prime_list = find_primes(numbers[round_idx])
        if len(prime_list) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
