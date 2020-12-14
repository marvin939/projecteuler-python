"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


LIMIT = 100

# sum of squares for 1 to LIMIT
sumOfSquares = 0
for x in range(LIMIT + 1):
    sumOfSquares += x ** 2
print('Sum of squares:', sumOfSquares)

# square of sums for 1 to LIMIT
squareOfSum = 0
for x in range(LIMIT + 1):
    squareOfSum += x
squareOfSum *= squareOfSum
print('Square of sum:', squareOfSum)

# different of sum of squares and square of sums
print('Difference:', squareOfSum - sumOfSquares)
