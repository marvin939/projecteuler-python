"""
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?


My approach / version B:
- Find the smallest number C that is divisible the prime numbers between A and B
  eg. if A and B are 1 and 10 respectively, then prime numbers are [2, 3, 5, 7]
  and C is 210.
  
- This product is a factor of the number we're trying to find (smallest positive
  number divisible the numbers between 1 (A) to 20 (B).
  eg. 2520 = C * M, where M = 12, letting M be the multiplier for C

- Let M start from 1.

- Using C and M, we use a loop to increment M to get to our objective and by
  doing a more thorough search (ie. instead of dividing the product of C and M
  by an array of primes between A and B, we just divide by all the numbers
  between A and B).
  
- ???

- Profit

Note: My approach is only faster for numbers between 1 and 24. For greater, it
will take more than 1 minute.

"""

from math import sqrt

# Controls
# --------
MIN_RANGE = 1
MAX_RANGE = 20


# Functions
# ---------
def isDivisibleByRange(num, m, n):
    div = m
    while div <= n:
        if num % div != 0:
            return False
        div += 1
    return True


def isDivisibleByNumbers(num, numbers):
    for div in numbers:
        if num % div != 0:
            return False
        
    return True


assert isDivisibleByNumbers(2520, [2, 3, 5, 7])
assert isDivisibleByNumbers(232792560, [2, 3, 5, 7, 11, 13, 17, 19])

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
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


def primesBetween(a, b):
    primes = []
    while a <= b:
        if isPrime(a):
            primes += [a]
        a += 1
    return primes



# Finding factor using primes
# ---------------------------
primes = primesBetween(MIN_RANGE, MAX_RANGE)
print('primes between {} and {}: {}'.format(MIN_RANGE, MAX_RANGE, primes))

factor = MAX_RANGE
while not isDivisibleByNumbers(factor, primes):
    factor += MAX_RANGE
    # increment by big steps to make searching faster.
    # ie. if the number is divisible by the range, then it's also divisble by
    # the biggest number from the range

print('{} is divisible by the numbers {}'.format(factor, primes))

# Thorough search
# ---------------

mult = 1
while not isDivisibleByRange(factor * mult, MIN_RANGE, MAX_RANGE):
    mult += 1
print('multiplier:', mult)

print('{} is divisible by the range of numbers {} to {}'.format(
    factor * mult, MIN_RANGE, MAX_RANGE))
