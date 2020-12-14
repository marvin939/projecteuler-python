"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt

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

N = 10001
num = 3         # start at 3; the 2nd prime number
primeCount = 2
lastPrime = None

while primeCount <= N:
    if isPrime(num):
        primeCount += 1
        lastPrime = num
    num += 2

print('prime 10001: ', lastPrime)
