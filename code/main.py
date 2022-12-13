import player_input

from game_board import GameBoard
from game_logic import (
    clear_terminal,
    display_introduction_board,
    display_welcome_message,
    pick_the_starting_player,
    playing,
)


def main():
    while True:
        display_welcome_message()
        player_marks = player_input.check_the_mark_of_first_player()

        current_turn = pick_the_starting_player()
        display_introduction_board()

        playing(player_marks, current_turn)

        if player_input.check_user_continuation_response() == "N":
            print("\nGOODBYE!!!")
            break

        GameBoard.clear_board()
        clear_terminal()


if __name__ == "__main__":
    clear_terminal()
    main()
