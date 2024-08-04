board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]


def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def play_game():
    game_still_going = False
    # Display the initial board
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_end_of_game()

        flip_player()


def handle_turn():
    position = input("Make your move. \nChoose a position from 1-9: ")
    position = int(position) - 1

    board[position] = "X"

def check_end_of_game():
    check_win()
    check_tie()

def check_win():
    # check rows
    # check columns
    # check diagonals
    return

def check_tie():

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