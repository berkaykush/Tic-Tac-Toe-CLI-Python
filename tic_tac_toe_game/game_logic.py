from random import randrange
from time import sleep
import os

from player_input import check_the_mark_of_first_player
from player_input import check_user_input_cell, check_user_continuation_response

from game_board import GameBoard

from win_rules import is_win


def display_welcome_message():
    print('\nWELCOME TO TIC TAC TOE!')
    print('The player 1 needs to select their mark (O or X) mark.')
    print('The second player will automatically get what is left.')
    print('The game will decide who to go first.')
    print('Choose a cell to put your mark.')
    print('There are 9 cells to choose from.')
    print('Chosen cell cannot be chosen again.')
    print('The game will continue until someone wins.')
    print('After the game ends, press \'y\' to continue playing, otherwise press \'n\'.')
    print('LET\'S PLAY!\n')


def display_introduction_board():
    print('''
                   |     |
                1  |  2  |  3
              _____|_____|_____
                   |     |
                4  |  5  |  6
              _____|_____|_____
                   |     |
                7  |  8  |  9
                   |     |
            ''')


def pick_the_starting_player():
    sleep(0.5)

    if randrange(0, 2):
        print('Player 1 will go first.')
        return 'Player 1'

    print('Player 2 will go first.')
    return 'Player 2'


def swap_turns(current_turn):
    if current_turn == 'Player 1':
        return 'Player 2'

    return 'Player 1'


def playing(player_marks, current_turn):
    while True:
        chosen_cell = check_user_input_cell(current_turn)

        if not GameBoard.is_cell_taken(chosen_cell):
            GameBoard.update_board(
                chosen_cell, player_marks[current_turn])
        else:
            print(
                'Sorry the cell is already taken. Please select another spot.\n')
            continue

        GameBoard.display_board()

        if is_win():
            print('CONGRATULATIONS!!!')
            print(f'{current_turn} has won the game!!!')
            break

        if GameBoard.is_board_full():
            print('TIE GAME!!!')
            break

        current_turn = swap_turns(current_turn)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        display_welcome_message()
        player_marks = check_the_mark_of_first_player()

        current_turn = pick_the_starting_player()
        display_introduction_board()

        playing(player_marks, current_turn)

        if check_user_continuation_response() == 'N':
            print('\nGOODBYE!!!')
            break

        GameBoard.clear_board()
        clear_terminal()


if __name__ == '__main__':
    main()
