"""
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isDivisibleByRange(num, m, n):
    div = m
    while div <= n:
        if num % div != 0:
            return False
        div += 1
    return True


for x in range(23, 1, -1):
    MIN_RANGE = 1
    MAX_RANGE = x

    num = MAX_RANGE
    """
    Start with max so we are taking steps of max_range (eg. if MAX is 10, then start
    from 10,20,30,...,10*N) and because we're sure that numbers below the MAX_RANGE
    aren't divisble by the range.
    """

    while not isDivisibleByRange(num, MIN_RANGE, MAX_RANGE):
        num += MAX_RANGE
        # increment by big steps to make searching faster.
        # ie. if the number is divisible by the range, then it's also divisble by
        # the biggest number from the range
        
    print('{} is divisible by the numbers {} to {}'.format(num, MIN_RANGE, MAX_RANGE))
