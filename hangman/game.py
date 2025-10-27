from data.words import words
from .words import choose_secret_word as choose


def init_state(secret: str, max_tries: int=17):
    return {
        "secret": secret,
        "display": ["_"] * len(secret),
        "guessed": set(),
        "count_guesses": 0,
        "max_tries": max_tries
    }


def validate_guess(ch: str, guessed: set[str]):
    message = "character is valid"
    is_valid = True
    if len(ch) > 1:
        message = "pleas provide a single char"
        is_valid = False
    elif ch in guessed:
        is_valid = False
        message = "Char is used - provide another one"
    elif not ch.isalpha():
        is_valid = False
        message = "Use only alphanumeric characters"

    return (is_valid, message)


def apply_guess(state: dict, ch: str):
    validation_tupple = validate_guess(ch, state["guessed"])
    if validation_tupple[0]:
        state["guessed"].add(ch)
    return validation_tupple[0]


def update_display(state: dict, ch: str):
    for index, char in enumerate(state["secret"]):
        if char == ch:
            state["display"][index] = char
    return state["display"]


def is_won(state: dict):
    return "_" in state["display"]


def is_lost(state: dict):
    return state["count_guesses"] == state["max_tries"]


def render_display(state: dict):
    return init_state(choose(words))["display"]


def render_summary(state: dict):
    return f"The word is {state["secret"]} \nThe letters that was guess: \n {state["guessed"]} \nYou geuss {state["count_guesses"]} out of {state["max_tries"]}"
