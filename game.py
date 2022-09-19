# Import external files
from helper import Board

# Create the game
def play_game(players: dict, first: int):
    
    # Create the board
    board = Board(players)
    board.print_board(True)