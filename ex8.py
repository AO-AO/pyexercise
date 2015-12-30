"""
Define a function called anti_vowel that takes one string, 
text, as input and returns the text with all of the vowels removed.
For example: anti_vowel("Hey You!") should return "Hy Y!".
"""


def anti_vowel(text):
    result = ""
    lenth = len(text)
    for i in xrange(0, lenth):
        if i == 0:
            result = result + text[i]
        elif i == lenth - 1:
            result = result + text[i]
        elif text[i] == ' ':
            result = result + text[i]
        elif text[i - 1] == ' ' or text[i + 1] == ' ':
            result = result + text[i]
    return result

result = anti_vowel("ni hao sunasdlfk kekendfa!")
print result