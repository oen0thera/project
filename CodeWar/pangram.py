'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

import string

def is_pangram(s):
    alpha=[i for i in string.ascii_lowercase[:26]]
    spliter=sorted(list(set([i.lower() for i in s if i.lower() in alpha])))
    if spliter==alpha:
      return True
    else:
      return False