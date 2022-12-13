class GameBoard:
    __board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

    @classmethod
    def get_board(cls):
        return cls.__board

    @classmethod
    def display_board(cls):
        print("\n                   |     |")
        print(
            f"                {cls.__board[1]}  |  {cls.__board[2]}  |  {cls.__board[3]}"
        )
        print("              _____|_____|_____")
        print("                   |     |")
        print(
            f"                {cls.__board[4]}  |  {cls.__board[5]}  |  {cls.__board[6]}"
        )
        print("              _____|_____|_____")
        print("                   |     |")
        print(
            f"                {cls.__board[7]}  |  {cls.__board[8]}  |  {cls.__board[9]}"
        )
        print("                   |     |")
        print("            ")

    @classmethod
    def is_cell_taken(cls, cell):
        return cls.__board[cell] != " "

    @classmethod
    def update_board(cls, cell, current_mark):
        cls.__board[cell] = current_mark

    @classmethod
    def is_board_full(cls):
        return " " not in cls.__board.values()

    @classmethod
    def clear_board(cls):
        for key in cls.__board:
            cls.__board[key] = " "
