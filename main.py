"""
Tic-Tac-Toe Game - Main Entry Point
This file provides a choice between CLI and GUI modes.
"""

import sys


def run_cli_game():
    """Run the text-based CLI version of the game."""
    from game_logic import TicTacToe
    
    game = TicTacToe()
    
    def display_board():
        """Display the board in text format."""
        print("\n")
        for i in range(0, 9, 3):
            print(f" {game.board[i]} | {game.board[i+1]} | {game.board[i+2]} ")
            if i < 6:
                print("-----------")
        print("\n")
    
    print("Welcome to Tic-Tac-Toe (CLI Mode)")
    print("=" * 40)
    
    while not game.game_over:
        display_board()
        print(f"Player {game.current_player}'s turn")
        
        while True:
            try:
                position = input("Choose a position (1-9): ")
                position = int(position) - 1
                
                if position < 0 or position > 8:
                    print("Invalid input. Please choose a number between 1-9.")
                    continue
                
                if game.make_move(position):
                    break
                else:
                    print("That position is already taken. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1-9.")
    
    display_board()
    
    if game.winner:
        print(f"Player {game.winner} wins!")
    else:
        print("It's a tie!")


def run_gui_game():
    """Run the pygame GUI version of the game."""
    try:
        from gui import TicTacToeGUI
        game = TicTacToeGUI()
        game.run()
    except ImportError as e:
        print(f"Error: Could not import GUI module. {e}")
        print("Make sure pygame is installed: pip install pygame")
        sys.exit(1)


def main():
    """Main entry point with mode selection."""
    print("=" * 50)
    print("         TIC-TAC-TOE GAME")
    print("=" * 50)
    print("\nSelect game mode:")
    print("1. GUI Mode (Graphical interface with single-player)")
    print("2. CLI Mode (Text-based, two players)")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            run_gui_game()
            break
        elif choice == "2":
            run_cli_game()
            
            # Ask if they want to play again
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again != 'y':
                break
        elif choice == "3":
            print("Thanks for playing!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
