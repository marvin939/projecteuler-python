# Visualisation: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

LIMIT = 500
sieve = [False for x in range(LIMIT - 1)]   # A boolean array of False, size LIMIT - 1
# False = unmarked/prime, True = marked/not prime.

# Sieve algorithm
# Mark even numbers:
for i in range(2, LIMIT - 1, 2):   # index 2 = number 4; step by 2
    sieve[i] = True

for i in range(0, LIMIT - 1):
    # Skip i if sieve at that position has already been marked.
    if sieve[i] == True:
        continue
    # else:
    n = i + 2   # The number to skip by
    # start = i + n
    start = n * n - 2   # optimisation: start from square of n
    for j in range(start, LIMIT - 1, n):
        sieve[j] = True

def printSieve():
    global sieve
    print(', '.join((('T' if b == True else 'F') for b in sieve)))

# Print prime numbers (can freeze on high LIMIT values)
if LIMIT <= 1000:
    print('Prime numbers:')
    primes = []
    for i in range(LIMIT - 1):
        if sieve[i] == False:
            primes += [i + 2]
    print(','.join(('{:4}'.format(x) for x in primes)))
    # Looks good on console that's 80 characters wide

sumOfPrimes = 0
for i, b in enumerate(sieve):
    if b == False:
        n = i + 2
        sumOfPrimes += n
print('Sum of primes below {} = {}'.format(LIMIT, sumOfPrimes))
