# Import external files
from helper import Player, get_name, print_frame, select, clear, color, delay_print, Board

# Create the game
def play_game(Player1: Player, Player2: Player, first: int):
    
    # Create the board
    board = Board()
    print(board)