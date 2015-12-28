"""
range([start,] stop[, step]) Function to create lists containing arithmetic progressions. start is zero if omitted. step has a default value of 1 and must be non-zero. If step is positive, the upper limit is stop-1. If step is negative, the lower limit is stop+1.

Examples

  >>> range(10)                                # only 'stop' is specified. 
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  >>> range(5, 10)                             # 'start', 'stop' are specified.
  [5, 6, 7, 8, 9 ]
  >>> range(1, 10, 2)                          # 'start', 'stop', 'step' are specified.
  [1, 3, 5, 7, 9]
  >>> range(10, 1, -2)                         # with negative 'step'.
  [10, 8, 6, 4, 2]
  >>> createLists(5)
  ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [ -5, -4, -3, -2, -1], [-1, -2, -3, -4, -5])

"""


# Write a function that returns 4 lists given a postive number.
def createLists(num):
    a = range(1, num+1)
    b = range(num, 0, -1)
    c = range(-num, 0)
    d = range(-1, -num-1, -1)
    result = (a, b, c, d)
    print result
