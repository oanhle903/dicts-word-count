"""Count words in file."""

import sys

import string

filename = sys.argv[1]

def tokenize(filename):
    """Return a list of words from the file at filename. For example:
    >>> tokenize("test.txt")
    ['As', 'I', 'was', 'going', 'to', 'St.', 'Ives', ..., 'many', 'were', 'Ives?']
    """

    tokens = []

    with open(filename) as file:
        for line in file:
            # create a list of words
            # line = ['a', 'b', 'c']
            line = line.rstrip().split(" ")
            for word in line:
                word = word.lower()
                word = word.translate(str.maketrans('','', string.punctuation))
                tokens.append(word)

        return tokens


def count_words(filename):
    """Take in a list of strings and return a dictionary of each string and 
    the number of times it appears in the list. For example:
    >>> count_words(["apple", "berry", "cherry", "apple"])
    {'apple': 2, 'berry': 1, 'cherry': 1}"""
    
    word_counts = {}
    words_list = tokenize(filename)

    for word in words_list:
       word_counts[word] = word_counts.get(word, 0) + 1 

    return word_counts


def print_word_counts(filename):
    """Take in a dictionary of word counts and print each key and value from the dictionary.
    >>> print_word_counts({'apple': 2, 'berry': 1, 'cherry': 1})
    apple 2
    berry 1
    cherry 1
    """
    words = count_words(filename)
    
    for word, occur in words.items():
        print(f'{word}: {occur}')

print_word_counts('test.txt')


 
