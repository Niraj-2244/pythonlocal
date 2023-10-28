import random
from words import words #make works py file and words variable to store json files.
import string


def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the last
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    words = get_valid_word()