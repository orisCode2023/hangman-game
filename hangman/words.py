import random
from data.words import words

def choose_secret_word(words: list[str]):
    # print(len(words))
    choose =  random.choice(words)
    words.pop(words.index(choose))
    # print(len(words))
    return choose

# print(choose_secret_word(words))

