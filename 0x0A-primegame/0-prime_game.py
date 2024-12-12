#!/usr/bin/python3
"""Prime Number Game."""

def find_primes(limit):
    """Generate a list of prime numbers up to a given limit."""
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num, limit + 1, num):
                sieve[multiple] = False
    return primes

def isWinner(x, nums):
    """Determine the overall winner after x rounds of the prime game."""
    if not x or not nums:
        return None

    maria_score = 0
    ben_score = 0

    for n in nums:
        if n < 2:
            ben_score += 1
            continue

        primes = find_primes(n)
        prime_set = set(primes)
        turn = 0  # 0 for Maria, 1 for Ben

        while primes:
            current_prime = primes.pop(0)
            prime_set.discard(current_prime)
            multiples = range(current_prime, n + 1, current_prime)
            for m in multiples:
                prime_set.discard(m)

            primes = sorted(prime_set)
            turn = 1 - turn

        if turn == 1:  # Maria couldn't play, Ben wins
            ben_score += 1
        else:  # Ben couldn't play, Maria wins
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
