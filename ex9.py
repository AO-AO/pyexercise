"""
Write a function called censor that takes two strings, 
text and word, 
as input. 
It should return the text with the word you chose replaced with asterisks.
"""

def censor(text, word):
    lenth_wd = len(word)
    rpl_wd = "*" * lenth_wd
    result = ""
    i = 0
    while i < len(text):
        if i + lenth_wd <= len(text):
            if text[i : i + lenth_wd] == word:
                result = result + rpl_wd
                i = i + lenth_wd
            else:
                result = result + text[i]
                i = i + 1
        else:
            result = result + text[i]
            i = i + 1
    return result


result = censor("this hack is wack hack", "hack")
print result
