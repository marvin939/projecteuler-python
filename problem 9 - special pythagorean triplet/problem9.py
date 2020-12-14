'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import sqrt, floor, ceil
a = 1
b = None
c = None
P = 1000    # Perimeter of right-angled triangle. eg. a + b + c = 1000
            # Must be a valid right-angle triangle perimeter since I'm only
            # allowing natural numbers for a, b and c!!!

satisfied = False
aThirdOfP = floor(P / 3)
while a <= aThirdOfP:
    # ^ condition is narrowed to 1/3 of P because we expect a < b < c
    # and a + b + c = P; a cannot be larger than b and c, but can get somewhat
    # close.
    
    b = floor((P - 2 * a) * P / (2 * (P - a)))
    c = floor(sqrt(a**2 + b**2))

    if a + b + c == P and (a < b < c):
        satisfied = True
        break
    
    a += 1

if satisfied:
    print('pythagorean triplet satisfying a + b + c = {}'
          ' and a < b < c found:'.format(P))
    print('a = {}, b = {}, c = {}'.format(a, b, c))
    print('a * b * c =', a * b * c)
    print('CONDITION SATISFIED!!!')
else:
    print('a = {}, b = {}, c = {}'.format(a, b, c))
    print('a^2 + b^2 = {}, and c^2 = {}'.format(a**2 + b**2, c**2))
    print('a * b * c =', a * b * c)
    print('NOT SATISFIED')
