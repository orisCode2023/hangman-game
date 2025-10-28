from data.words import words
from .words import choose_secret_word as choose
from .game import *


def prompt_guess():
    return input("Enter a one character ")


def print_status(state: dict):
    print(f"{state["display"]} \nThe guess list {state["guessed"]} \n" 
          f"Number of guess {state["count_guesses"]} out of {state["max_tries"]}")


def print_result(state: dict):
    if is_won(state) == False:
        print("Congratulation")
        print(render_summary(state))
    else:
        print("Sorry, Maybe Next Time")


