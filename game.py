# Import external files
from helper import Board, select, delay_print, color

# Create the game
def set_game(players: dict, first: int):
    
    # Create the board
    board = Board(players)

    # Run the game
    play_game(board, first)


# Play the game
def play_game(board: Board, turn: int):

    # Print the board in a cool way
    board.print_board(True)

    # Ask user for what column they want
    delay_print(f"{board.players[turn].name}'s turn: ", end="", edit=[board.players[turn].color])
    column = select(txt=board.players[turn].color + f"{board.players[turn].name}'s turn: " + color.END, nl=False, prompt1_nothing=True)