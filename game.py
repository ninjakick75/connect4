# Import external files
from helper import Board, print_frame, select, delay_print, color, clear, string_centre
from time import sleep

# Create the game
def set_game(players: dict, first: int):

    # Create the board
    board = Board(players)

    # Run the game
    play_game(board, first)


# Play the game
def play_game(board: Board, turn: int):

    # Tell the user who is going first
    print_frame()
    delay_print(f"{board.players[turn].name} is going first", edit=[board.players[turn].color])
    sleep(1)
    print_frame()

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
        winner = board.insert(column, turn)

        # Print the board
        clear()
        print_frame()
        board.print_board()

        # Check if winner
        if winner:

            # Add winner to statistics
            board.add_winner(turn)

            # Print the winner
            print()
            delay_print(string_centre(f"{board.players[turn].name} won!") + "\n", edit=[color.GREEN + color.BOLD])

            # Break the while loop
            break
            

        # Change the turn
        turn = ((turn) % 2) + 1
