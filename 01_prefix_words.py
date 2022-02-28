import unittest

question_01 = """
Given a query string s and a list of all possible words, return all words that have s as a prefix.

Example 1:

Input:
s = “de”
words = [“dog”, “deal”, “deer”]

Output:
[“deal”, “deer”]

Explanation:
Only deal and deer begin with de.

Example 2:

Input:
s = “b”
words = [“banana”, “binary”, “carrot”, “bit”, “boar”]

Output:
[“banana”, “binary”, “bit”, “boar”]

Explanation:
All these words start with b, except for “carrot”.
"""

# Implement the below function and run the program


def prefix_words(prefix, words):
   pass
   l=[]
   for word in words:
      flag=True
      for i in range(len(prefix)):
         if word[i]!=prefix[i]:
            flag=False
      if flag==True:
         l.append(word)
   return l
