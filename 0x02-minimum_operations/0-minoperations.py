#!/usr/bin/python3
'''
Calculate the minimum numsult in bla blabla
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations required to a

    Args:
        n: The target number of H characters.

    Returns:
        The fewest number of operationtly n H characters.
        Returns 0 if n cannot be achieved.
    '''
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
