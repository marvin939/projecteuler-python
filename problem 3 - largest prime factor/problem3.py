"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

INPUT = 600851475143
"""
Note: two of the largest natural number factors of a number is itself and the
number less than or equal to its square root - this is used to make search for
primes and factors faster.
"""


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


def getFactors(num):
    sqrtNum = sqrt(num)   
    x = 2
    factors = [1]       # 1 is a factor num

    while x <= sqrtNum:
        if (num % x == 0):
            factors += [x]
        
        x += 1    
    factors += [num]    # num is a factor of num
    
    return factors


"""
x = 2
while x < INPUT:
    if isPrime(x):
        print(x, 'is a prime')
    x += 1
"""

print('Factors of {}:'.format(INPUT))
inputFactors = getFactors(INPUT)
print(inputFactors)


primeFactors = []
for f in inputFactors:
    if isPrime(f):
        primeFactors += [f]

print('Prime factors of {}:'.format(INPUT))
print(primeFactors)
