import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()

                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, '')

                words = text.split()

                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()

        all_words = self.get_all_words()

        positions = {}

        for file_name, words in all_words.items():
            if word in words:
                positions[file_name] = words.index(word) + 1

        return positions

    def count(self, word):
        word = word.lower()

        all_words = self.get_all_words()

        counts = {}

        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)

        return counts


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))