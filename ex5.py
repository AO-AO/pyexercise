"""
filter(function, iterable) Construct a list from items of iterable for which function returns True.

Examples

  >>> filter(lambda x:x%2==0, range(10))          # generate a list of even integers.
  [0, 2, 4, 6, 8]
  >>> filter(lambda x:x>0, [5, -2, 8, 1, -1])     # return a list of positive integers
  [5, 8, 1]
  >>> def ones(x):
  ...    if '1' in str(x):
  ...       return True
  ...    else:
  ...       return False
  >>> filter(ones, range(30))                      # return a list of integers with digit '1'.
  [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21 ]
  >>> fn1('aBCDefG')                               
  'aef'
  >>> fn2('13a@b24&z')                               
  '1324'
"""


def lowercase(x):
    return x.islower()

def fn1(word):
    return filter(lowercase, word)


def fn2(word):
    return filter(lambda x: x.isdigit(), word)
    