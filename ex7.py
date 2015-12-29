"""
divmode(a, b) Return the quotient and remainder of a/b.
For integers, result is the same as (a // b, a % b).

Examples

  >>> divmod(3, 2)
  (1, 1)
  >>> divmod(8, -2)
  (-4, 0)
  >>> exponent(8, 2)
  3
  >>> exponent(25, 5)
  2
"""

def exponent(num, base):
    exp = 0
    while divmod(num, base)[0]:
        num = divmod(num, base)[0]
        exp = exp + 1
    return exp

print exponent(8,2)
