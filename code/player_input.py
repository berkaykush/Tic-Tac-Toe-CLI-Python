def check_the_mark_of_first_player():
    while True:
        chosen_mark = input("Player 1: Do you want to be 'O' or 'X' ?: ").strip()

        if chosen_mark.upper() in (marks := ["X", "O"]):
            chosen_mark = chosen_mark.upper()
            marks.remove(chosen_mark)

            return {"Player 1": chosen_mark, "Player 2": marks[0]}

        print(f"Sorry '{chosen_mark}' is not a valid command.\n")


def check_user_input_cell(current_turn):
    while True:
        user_input = input(
            f"{current_turn}: Please enter a valid cell number (1-9): "
        ).strip()

        if user_input.isdigit():
            if (input_num := int(user_input)) >= 1 and input_num <= 9:
                return input_num

            print("Sorry you are out of acceptable range (1-9).\n")

        else:
            print(f"Sorry '{user_input}' is not a digit.\n")


def check_user_continuation_response():
    while True:
        user_input = input("\nDo you want to continue playing? (Y/N): ").strip()

        if user_input.upper() in ["Y", "N"]:
            return user_input.upper()

        print(f"Sorry '{user_input}' is not a valid command.\n")
