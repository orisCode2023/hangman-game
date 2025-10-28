import random
from data.words import words

def choose_secret_word(words: list[str]):
    already_choose = []
    choose =  random.choice(words)
    while len(already_choose) != len(words):
        if choose in already_choose:
            choose =  random.choice(words)
        else:
            already_choose.append(choose)
            print(already_choose)
            break
    
    return choose

print(choose_secret_word(words))

