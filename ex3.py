"""
Examples

  >>> ord('a')
  97
  >>> chr(ord('a)-32)        # convert 'a' to 'A' by subtracting 32 from ASCII code
  'A'
  >>> ord('2')
  50
  >>> ord(1)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: ord() expected string of length 1, but int found
  >>> capitalize('how are you?')
  'How Are You?'
  
  """


# Write a function that capitalizes the first character of each word.
def capitalize(phrase):
    result = ""
    for i in xrange(0, len(phrase)):
        if i == 0:
            result = result + chr(ord(phrase[i]) - 32)
        elif phrase[i-1] == ' ':
            result = result + chr(ord(phrase[i]) - 32)
        else:
            result = result + phrase[i]
    return result


phrase = capitalize("yuan dan fang jia san tian")
print phrase