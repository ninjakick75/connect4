# Import external files
from helper import Board, print_frame, select, delay_print, color, clear, string_centre
from time import sleep

# Create the game
def set_game(players: dict, turn: int):

    # Create the board
    board = Board(players)

    # Run the game
    while True:
        turn = play_game(board, turn)

        # Ask user to play another game
        print_frame()

        delay_print("Do you want to play the next round?\n")
        delay_print("1: YES\n", edit=[color.GREEN])
        delay_print("2: NO\n", edit=[color.RED])
        choice = select("Choose: ")

        # If the input is two break
        if choice == 2:
            break

        # Reset the board
        board.reset()

    # Once finished with game, suspencefully print the winner
    print_frame()
    board.print_winner()


# Play the game
def play_game(board: Board, turn: int):

    # Remember who went first
    first = turn

    # Tell the user who is going first
    print_frame()
    delay_print(
        f"{board.players[turn].name} is going first", edit=[board.players[turn].color]
    )
    sleep(1)
    print_frame()

    # Print the board in a cool way
    board.print_board(True)

    # Start the game
    while True:

        # Get a valid list of numbers to use for columns
        valid = board.get_valid()

        # If there is no winner and can not move
        if valid == []:

            # Tell the user that it is a tie
            delay_print(string_centre("Tie!") + "\n", edit=[color.BLUE], delay=0.02)

            # Add tie to statistics
            board.add_winner(0)

            # Delay
            sleep(1)

            # return who will go next
            return ((first) % 2) + 1

        # Ask user for what column they want
        delay_print(
            f"{board.players[turn].name}'s turn: ",
            end="",
            edit=[board.players[turn].color],
        )

        # Get the user input
        column = select(
            txt=board.players[turn].color
            + f"{board.players[turn].name}'s turn: "
            + color.END,
            nl=False,
            prompt1_nothing=True,
            select=valid,
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
            delay_print(
                string_centre(f"{board.players[turn].name} won!") + "\n",
                edit=[color.GREEN + color.BOLD],
                delay=0.02,
            )

            sleep(1)

            # Break the while loop
            return ((turn) % 2) + 1

        # Change the turn
        turn = ((turn) % 2) + 1
