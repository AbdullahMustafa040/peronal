import numpy as np
import pandas as pd
import spacy
import codecs, sys
import random
from collections import Counter
import pickle

class RomanTokenizer:
    def __init__(self, dictionary_path='/content/dictionary.pkl'):
        self.unlp = spacy.blank('ur')
        self.dictionary = self.loadFromPickle(dictionary_path)

    def loadFromPickle(self, filepath):
        with open(filepath, 'rb') as f:
            return pickle.load(f)

    def roman_tokenizer(self, sentence):
        # Lowering
        sentence = sentence.lower()

        # Default Parameters
        tokens = []
        punctuation = '''!()%\n٪-;۔،:\n\/'"\,“./؟_ء'''

        sentence = self.unlp(sentence)

        # Iterating Word By Word
        for word in sentence:
            word = str(word)
            # Iterating Index By Index
            for index in word:
                if index in punctuation:
                    word = word.replace(index, '')

            # Removing Any Remaining Special Characters
            if word != "\n" and word != "\r" and word != " " and word != '' and word != " \r" and word != '‘' and word != '’':
                tokens.append(word)

        bi_tokens = []
        for i in range(len(tokens)):
            if i + 1 < len(tokens):
                a = tokens[i]
                b = tokens[i + 1]

                if a + ' ' + b in self.dictionary:
                    index = tokens.index(a)
                    tokens.remove(a)
                    tokens.remove(b)
                    tokens.insert(index, a + ' ' + b)

        return tokens

if __name__ == "__main__":
    # Example paragraph
    paragraph = "kuch nahi hota..meri ma ka hai ausman card unko 2 baar hard atek ayaa tha ilaaj ke liy pase nahi the doctor ny bola is card se sarkar pase nahi milte"

    # Create an instance of RomanTokenizer
    tokenizer = RomanTokenizer()

    # Tokenize the paragraph
    tokens = tokenizer.roman_tokenizer(paragraph)

    # Print the tokens
    print("Tokens:", tokens)
