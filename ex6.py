"""
len(s) Return the length (the number of items) of a sequnce (string, tuple or list) or a mapping (dictionary).

Examples

  >>> len('python')                 # string
  6
  >>> len([])                       # empty list
  0
  >>> len((1, 2, 3, 4))             # tuple
  4
  >>> len({'a':1, 'b':2, 'c':3})    # dictionary
  3
  >>> totSize('abc', (1,), [1,2,3])
"""
# def sum(x,y):
#     return len(x) + len(y)

# def totSize(*args):
#     return reduce(sum, args)
def totSize(*args):
    total = 0
    for item in args:
        total = total + len(item)
    return total

print totSize("abc", [1,2,3])