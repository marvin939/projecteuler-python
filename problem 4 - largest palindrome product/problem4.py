"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Ans: 906609 by 999 and 999
"""

NUM_DIGITS = 5
#MIN_RANGE = 10 ** (NUM_DIGITS - 1)
MIN_RANGE = int(9 * (10 ** (NUM_DIGITS - 1)))   # begin somewhere in middle
MAX_RANGE = 10 ** NUM_DIGITS


def isPalindrome(number):
    numberStr = str(number)
    numDigits = len(numberStr)
    numDigitsHalf = int(numDigits / 2)
    for i in range(numDigitsHalf):
        if numberStr[i] != numberStr[numDigits - 1 - i]:
            return False

    return True

assert isPalindrome(9009) == True
assert isPalindrome(1234321) == True
assert isPalindrome(123) == False


largestPalindromeProduct = 0
xOfLargest = 0
yOfLargest = 0

for x in range(MIN_RANGE, MAX_RANGE):
    for y in range(MIN_RANGE, MAX_RANGE):
        product = x * y
        if isPalindrome(product):
            #print('{} * {} = {} is a palindrome product.'.format(x, y, product))
            if largestPalindromeProduct < product:
                largestPalindromeProduct = product
                xOfLargest = x
                yOfLargest = y
print('The largest palindrome product of {} digits is {} by {} and {}.'.format(
    NUM_DIGITS, largestPalindromeProduct, xOfLargest, yOfLargest))
                  
