from game_board import GameBoard


def is_win_condition(condition):
    return len(condition) == 1 and ' ' not in condition


def is_diagonal_win(board):
    condition_1 = {board[1], board[5], board[9]}
    condition_2 = {board[3], board[5], board[7]}

    return is_win_condition(condition_1) or is_win_condition(condition_2)


def is_horizontal_win(board):
    condition_1 = {board[1], board[2], board[3]}
    condition_2 = {board[4], board[5], board[6]}
    condition_3 = {board[7], board[8], board[9]}

    return is_win_condition(condition_1) \
        or is_win_condition(condition_2) or is_win_condition(condition_3)


def is_vertical_win(board):
    condition_1 = {board[1], board[4], board[7]}
    condition_2 = {board[2], board[5], board[8]}
    condition_3 = {board[3], board[6], board[9]}

    return is_win_condition(condition_1) \
        or is_win_condition(condition_2) or is_win_condition(condition_3)


def is_win():
    board = GameBoard.get_board()
    return is_diagonal_win(board) or is_horizontal_win(board) or is_vertical_win(board)
