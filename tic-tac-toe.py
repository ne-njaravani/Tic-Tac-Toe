# ---- Global Variables ----
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

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
def handle_turn():
    position = input("Make your move. \nChoose a position from 1-9: ")
    position = int(position) - 1

    board[position] = "X"

def check_end_of_game():
    check_for_winner()
    check_for_tie()

def check_for_winner():
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    return

def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return

def check_for_tie():

    return

def flip_player():
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