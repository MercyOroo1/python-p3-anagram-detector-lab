# your code goes here!
 

class Anagram:
    def __init__(self, anagram):
        self.anagram = anagram
    def match (self, words):
       sorted_word = sorted(self.anagram)
       return [word for word in words if sorted(word)== sorted_word]

