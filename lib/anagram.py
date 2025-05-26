# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    @property
    def word(self):
        return self._word 
    @word.setter
    def word(self, word):
        if not isinstance(word, str):
            raise ValueError("Word must be a string")
        self._word = word
        print("Word saved successfully")
    def match(self, possible_anagrams):
        matches = []
        target = sorted(self.word.lower())

        for newword in possible_anagrams:
            if sorted(newword.lower()) == target:
                matches.append(newword)
        return matches

example1 = Anagram("OOggle")
example1.match(['enlists', 'google', 'inlets', 'banana'])
