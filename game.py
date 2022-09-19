# Import external files
from helper import Board, print_frame, select, delay_print, color, clear

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

    # Start the game
    while True:
        # Ask user for what column they want
        delay_print(
            f"{board.players[turn].name}'s turn: ",
            end="",
            edit=[board.players[turn].color],
        )

        # Get a valid list of numbers to use for columns
        valid = board.get_valid()

        # Get the user input
        column = select(
            txt=board.players[turn].color
            + f"{board.players[turn].name}'s turn: "
            + color.END,
            nl=False,
            prompt1_nothing=True,
            select=valid
        )

        # Insert into the column
        board.insert(column, turn)

        # Change the turn
        turn = ((turn) % 2) + 1

        # Print the board
        clear()
        print_frame()
        board.print_board()
