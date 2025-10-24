"""
AI player implementation using minimax algorithm for Tic-Tac-Toe.
"""

from game_logic import TicTacToe


class AIPlayer:
    """AI player that uses minimax algorithm to find optimal moves."""
    
    def __init__(self, difficulty="hard"):
        """
        Initialize AI player.
        
        Args:
            difficulty: 'easy', 'medium', or 'hard'
        """
        self.difficulty = difficulty
    
    def get_best_move(self, game):
        """
        Get the best move for the current game state.
        
        Args:
            game: TicTacToe game instance
            
        Returns:
            int: Best position to play (0-8)
        """
        if self.difficulty == "hard":
            return self._minimax_move(game)
        else:
            # For easy/medium, just pick first available move
            available = game.get_available_moves()
            return available[0] if available else None
    
    def _minimax_move(self, game):
        """
        Find the best move using minimax algorithm.
        
        Args:
            game: TicTacToe game instance
            
        Returns:
            int: Best position to play
        """
        best_score = float('-inf')
        best_move = None
        ai_player = game.current_player
        
        for move in game.get_available_moves():
            # Create a copy to simulate the move
            test_game = TicTacToe()
            test_game.board = game.get_board_copy()
            test_game.current_player = game.current_player
            test_game.winner = game.winner
            test_game.game_over = game.game_over
            
            # Make the move
            test_game.make_move(move)
            
            # Get score for this move
            score = self._minimax(test_game, False, ai_player)
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def _minimax(self, game, is_maximizing, ai_player):
        """
        Minimax algorithm implementation.
        
        Args:
            game: TicTacToe game instance
            is_maximizing: True if maximizing player's turn
            ai_player: The AI player's symbol ('X' or 'O')
            
        Returns:
            int: Score for the current game state
        """
        # Check terminal states
        if game.game_over:
            if game.winner == ai_player:
                return 10
            elif game.winner:
                return -10
            else:
                return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for move in game.get_available_moves():
                test_game = TicTacToe()
                test_game.board = game.get_board_copy()
                test_game.current_player = game.current_player
                test_game.winner = game.winner
                test_game.game_over = game.game_over
                
                test_game.make_move(move)
                score = self._minimax(test_game, False, ai_player)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in game.get_available_moves():
                test_game = TicTacToe()
                test_game.board = game.get_board_copy()
                test_game.current_player = game.current_player
                test_game.winner = game.winner
                test_game.game_over = game.game_over
                
                test_game.make_move(move)
                score = self._minimax(test_game, True, ai_player)
                best_score = min(score, best_score)
            return best_score
