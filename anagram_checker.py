import enchant
from module import dict
class AnagramChecker:
    def __init__(self, dictionary_filepath="sowpods.txt"):
        with open(dictionary_filepath) as file:
            self.dictionary = {line.strip().lower() for line in file}
    def is_anagram(self, word1, word2):
        word_1 = word1.lower()
        word_2 = word2.lower()
        return word_1 != word_2 and sorted(word_1) == sorted(word_2)
    def is_valid_word(self, word):
        return word.strip().lower() in self.dictionary
    def get_anagrams(self, word):
        anagrams = []
        for dict_word in self.dictionary:
            if self.is_anagram(word, dict_word):
                anagrams.append(dict_word)
        return anagrams


