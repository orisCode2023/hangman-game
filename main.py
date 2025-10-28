from data.words import words
from hangman.words import choose_secret_word as choose
from hangman.game import *
from hangman.io import *

def play(words: list[str]):
    # while len(words) != 0:
        game_info = init_state(choose(words))
        print(game_info)
        while is_won(game_info) and not is_lost(game_info):
            print(render_display(game_info))
            guess = prompt_guess()
            apply = apply_guess(game_info, guess)
            print(apply)
            update = update_display(game_info, guess)
            print(update)
            print_status(game_info)
        print_result(game_info)

            
        

if __name__ == "__main__":
    play(words)