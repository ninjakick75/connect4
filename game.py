# Import external files
from helper import Player, get_name, print_frame, select, clear, color, delay_print, Board

# Create the game
def play_game(players: dict, first: int):
    
    # Create the board
    board = Board(players)
    board.print_board(True)