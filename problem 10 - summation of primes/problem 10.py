'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
from math import sqrt, floor

'''
def isPrime(num):
    if num < 2:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False

    # check odd factors of num
    x = 3
    sqrtNum = sqrt(num)
    while x <= sqrtNum:
        if (num % x == 0):
            return False
        x += 2  # skip evens
    
    return True
'''

# https://projecteuler.net/overview=007
def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True     # 2 and 3 are prime
    elif n % 2 == 0:
        return False    # n is even
    elif n < 9:
        return True     # already excluded 4, 6, 8, so prime: 5, 7
    elif n % 3 == 0:
        return False    # n is divisible by 3
    else:
        r = floor(sqrt(n))  # sqrt(n) rounded to greatest integer r so that
                            # r^2 <= n
        f = 5
        # All primes greater than 3 can be written in the form 6k +/- 1
        # eg. k=1 gives 5 and 7; k=2 gives 11 and 13; k=3 gives 17,19;
        #     k=4 gives 23; k=5 gives 29,31; k=6 gives 37; etc.
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True


LIMIT = 500
sumOfPrimes = 2 + 3     # because 2 and 3 are primes
x = 5
while x <= LIMIT:
    if isPrime(x):
        sumOfPrimes += x
    x += 2

print('sum of primes below {} = {}'.format(LIMIT, sumOfPrimes))
