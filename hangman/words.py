import random
from data.words import words

def choose_secret_word(words: list[str]):
    return random.choice(words)

# function to keep all the choice in a list to make the game not repeat the words
# and then to run the main loop