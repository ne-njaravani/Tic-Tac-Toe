# ---- Global Variables ----
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

game_still_going = True
winner = None
current_player = "X"


def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def play_game():
    # Display the initial board
    display_board()

    while game_still_going:
        # Handle a single turn of an arbitrary
        handle_turn(current_player)

        # Check if game has ended
        check_end_of_game()

        # Flip to the other player
        flip_player()

    # Game ended
    if winner == 'X' or winner == 'O':
        print(f"{winner} won!")
    elif winner is None:
        print("Tie")


# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(f"{player}'s turn.")
    position = input("Make your move. \nChoose a position from 1-9: ")
    valid = False

    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input.\nChoose a position from 1-9")
            display_board()

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Invalid move. Space is already occupied.")
            display_board()

    board[position] = player

    display_board()


def check_end_of_game():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return


# board
# Display board
# Play Game
# Check Win
# Check rows
# Check columns
# Check diagonals
# Check tie
# flip player

play_game()
