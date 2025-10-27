from data.words import words
from hangman.words import choose_secret_word as choose
from hangman.game import *
from hangman.io import *

def play(words: list[str], max_tries: int = 17):
    game_info = init_state(choose(words))
    print(game_info)
    for word in words:
        word = game_info["secret"]
        print(word)
        while is_won or is_lost:
            print(render_display(game_info))
            guess = prompt_guess()
            print(apply_guess(game_info, guess))
            print(update_display(game_info, guess))
            print_status(game_info)
        print_result(game_info)

            
        

if __name__ == "__main__":
    play(words)