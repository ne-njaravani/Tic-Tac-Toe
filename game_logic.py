"""
Core game logic for Tic-Tac-Toe game.
This module contains the game engine that can be used by both CLI and GUI.
"""


class TicTacToe:
    """Tic-Tac-Toe game engine."""
    
    def __init__(self):
        """Initialize the game board and state."""
        self.board = ["-"] * 9
        self.current_player = "X"
        self.winner = None
        self.game_over = False
    
    def reset(self):
        """Reset the game to initial state."""
        self.board = ["-"] * 9
        self.current_player = "X"
        self.winner = None
        self.game_over = False
    
    def make_move(self, position):
        """
        Make a move at the specified position.
        
        Args:
            position: Position on board (0-8)
            
        Returns:
            bool: True if move was valid, False otherwise
        """
        if position < 0 or position > 8:
            return False
        
        if self.board[position] != "-" or self.game_over:
            return False
        
        self.board[position] = self.current_player
        self.check_game_over()
        
        if not self.game_over:
            self.switch_player()
        
        return True
    
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_game_over(self):
        """Check if the game is over and set winner if applicable."""
        winner = self.check_winner()
        if winner:
            self.winner = winner
            self.game_over = True
        elif self.is_board_full():
            self.game_over = True
    
    def check_winner(self):
        """
        Check if there's a winner.
        
        Returns:
            str: 'X' or 'O' if there's a winner, None otherwise
        """
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "-":
                return self.board[i]
        
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "-":
                return self.board[i]
        
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "-":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != "-":
            return self.board[2]
        
        return None
    
    def is_board_full(self):
        """Check if the board is full."""
        return "-" not in self.board
    
    def get_available_moves(self):
        """
        Get list of available positions.
        
        Returns:
            list: List of available positions (0-8)
        """
        return [i for i in range(9) if self.board[i] == "-"]
    
    def get_board_copy(self):
        """Return a copy of the current board."""
        return self.board.copy()
