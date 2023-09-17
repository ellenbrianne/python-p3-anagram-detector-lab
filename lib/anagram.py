class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        match_display = []
        separated_word = [letter for letter in self.word]
        for str in list:
            individual_word = [letter for letter in str]
            if sorted(separated_word) == sorted(individual_word):
                match_display.append(str)
            else:
                return match_display