"""
Pygame GUI implementation for Tic-Tac-Toe game.
"""

import pygame
import sys
from game_logic import TicTacToe
from ai_player import AIPlayer


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
LIGHT_BLUE = (173, 216, 230)

# Game settings
WIDTH = 600
HEIGHT = 700
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4


class TicTacToeGUI:
    """GUI for Tic-Tac-Toe game using pygame."""
    
    def __init__(self):
        """Initialize the GUI."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 48)
        
        self.game = TicTacToe()
        self.ai = AIPlayer(difficulty="hard")
        self.game_mode = None  # Will be set by mode selection
        self.ai_thinking = False
        
    def draw_board(self):
        """Draw the game board lines."""
        self.screen.fill(WHITE)
        
        # Draw vertical lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, BLACK, 
                           (i * SQUARE_SIZE, 0), 
                           (i * SQUARE_SIZE, WIDTH), 
                           LINE_WIDTH)
        
        # Draw horizontal lines
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, BLACK, 
                           (0, i * SQUARE_SIZE), 
                           (WIDTH, i * SQUARE_SIZE), 
                           LINE_WIDTH)
    
    def draw_figures(self):
        """Draw X's and O's on the board."""
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                pos = row * 3 + col
                if self.game.board[pos] == "X":
                    self.draw_x(row, col)
                elif self.game.board[pos] == "O":
                    self.draw_o(row, col)
    
    def draw_x(self, row, col):
        """Draw an X at the specified position."""
        start_x = col * SQUARE_SIZE + SPACE
        start_y = row * SQUARE_SIZE + SPACE
        end_x = col * SQUARE_SIZE + SQUARE_SIZE - SPACE
        end_y = row * SQUARE_SIZE + SQUARE_SIZE - SPACE
        
        pygame.draw.line(self.screen, RED, (start_x, start_y), 
                        (end_x, end_y), CROSS_WIDTH)
        pygame.draw.line(self.screen, RED, (start_x, end_y), 
                        (end_x, start_y), CROSS_WIDTH)
    
    def draw_o(self, row, col):
        """Draw an O at the specified position."""
        center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(self.screen, BLUE, (center_x, center_y), 
                          CIRCLE_RADIUS, CIRCLE_WIDTH)
    
    def draw_status(self):
        """Draw the game status bar."""
        status_y = WIDTH + 10
        pygame.draw.rect(self.screen, LIGHT_BLUE, (0, WIDTH, WIDTH, HEIGHT - WIDTH))
        
        if self.game.game_over:
            if self.game.winner:
                text = f"Player {self.game.winner} wins!"
            else:
                text = "It's a tie!"
        else:
            text = f"Player {self.game.current_player}'s turn"
        
        text_surface = self.large_font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, status_y + 30))
        self.screen.blit(text_surface, text_rect)
        
        # Draw buttons
        self.draw_button("Restart", WIDTH // 2 - 160, status_y + 70, 140, 50)
        self.draw_button("Main Menu", WIDTH // 2 + 20, status_y + 70, 140, 50)
    
    def draw_button(self, text, x, y, width, height):
        """Draw a button."""
        mouse_pos = pygame.mouse.get_pos()
        color = GREEN if (x <= mouse_pos[0] <= x + width and 
                         y <= mouse_pos[1] <= y + height) else GRAY
        
        pygame.draw.rect(self.screen, color, (x, y, width, height))
        pygame.draw.rect(self.screen, BLACK, (x, y, width, height), 3)
        
        text_surface = self.font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(text_surface, text_rect)
    
    def draw_menu(self):
        """Draw the main menu."""
        self.screen.fill(WHITE)
        
        title = self.large_font.render("TIC-TAC-TOE", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        self.draw_button("Player vs Player", WIDTH // 2 - 120, 250, 240, 60)
        self.draw_button("Player vs Computer", WIDTH // 2 - 120, 350, 240, 60)
        self.draw_button("Quit", WIDTH // 2 - 120, 450, 240, 60)
    
    def get_clicked_position(self, mouse_pos):
        """Convert mouse position to board position."""
        x, y = mouse_pos
        if y >= WIDTH:  # Click is in status bar
            return None
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row * 3 + col
    
    def handle_click(self, mouse_pos):
        """Handle mouse click on the board."""
        if self.game_mode is None:
            # Main menu click
            return self.handle_menu_click(mouse_pos)
        
        # Check button clicks
        status_y = WIDTH + 10
        # Restart button
        if (WIDTH // 2 - 160 <= mouse_pos[0] <= WIDTH // 2 - 20 and
            status_y + 70 <= mouse_pos[1] <= status_y + 120):
            self.game.reset()
            self.ai_thinking = False
            return
        
        # Main menu button
        if (WIDTH // 2 + 20 <= mouse_pos[0] <= WIDTH // 2 + 160 and
            status_y + 70 <= mouse_pos[1] <= status_y + 120):
            self.game_mode = None
            self.game.reset()
            self.ai_thinking = False
            return
        
        # Board click
        if not self.game.game_over and not self.ai_thinking:
            position = self.get_clicked_position(mouse_pos)
            if position is not None:
                if self.game.make_move(position):
                    # If playing against AI and game not over, AI makes move
                    if (self.game_mode == "ai" and not self.game.game_over):
                        self.ai_thinking = True
    
    def handle_menu_click(self, mouse_pos):
        """Handle click on main menu."""
        x, y = mouse_pos
        
        # Player vs Player button
        if (WIDTH // 2 - 120 <= x <= WIDTH // 2 + 120 and 250 <= y <= 310):
            self.game_mode = "pvp"
            self.game.reset()
        
        # Player vs Computer button
        elif (WIDTH // 2 - 120 <= x <= WIDTH // 2 + 120 and 350 <= y <= 410):
            self.game_mode = "ai"
            self.game.reset()
        
        # Quit button
        elif (WIDTH // 2 - 120 <= x <= WIDTH // 2 + 120 and 450 <= y <= 510):
            return False
        
        return True
    
    def ai_move(self):
        """Make AI move."""
        if self.ai_thinking:
            move = self.ai.get_best_move(self.game)
            if move is not None:
                self.game.make_move(move)
            self.ai_thinking = False
    
    def run(self):
        """Main game loop."""
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    result = self.handle_click(pygame.mouse.get_pos())
                    if result is False:
                        running = False
            
            # AI makes move if it's their turn
            if self.game_mode == "ai" and self.ai_thinking:
                pygame.time.wait(500)  # Small delay for better UX
                self.ai_move()
            
            # Draw everything
            if self.game_mode is None:
                self.draw_menu()
            else:
                self.draw_board()
                self.draw_figures()
                self.draw_status()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
