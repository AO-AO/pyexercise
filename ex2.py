"""
Examples

  >>> chr(97)             # ASCII code 97-122 corresponds to 'a-z'
  'a'
  >>> chr(90)             # ASCII code 65-90 corresponds to 'A-Z'
  'Z'
  >>> chr(48)             # ASCII code 48-57 corresponds to '0-9'
  '0'
  >>> chr(256)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: chr() arg not in range(256)
  >>> toString([112, 121, 115, 99, 104, 111, 111, 108, 115])
  'pyschools'
  """

# Write a function that returns a string of characters based on a list of ASCII codes.
def toString(alist): 
    m_string = ""
    for i in xrange(0, len(alist)):
        m_string = m_string + chr(alist[i])
    return m_string
        