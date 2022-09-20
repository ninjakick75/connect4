# Import packages
import os
import sys
from time import sleep


class Player:

    # Constructor class
    def __init__(self, color, name):
        self._name = name
        self._color = color
        self._win = 0

    # Add a win to the player
    def add_win(self):
        self._win += 1

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def win(self):
        return self._win


class Board:

    # Constant variables
    COLUMNS = 7
    ROWS = 6
    CONNECT = 4

    # Constructor class
    def __init__(self, dict):

        # Create the board with zeros
        self._board = []
        for i in range(self.ROWS):
            list = []
            for j in range(self.COLUMNS):
                list.append(0)

            # Add the list to the board
            self._board.append(list)

        # Add the player dictionary
        self._players = dict

        # Add the connect four coloum heights
        self._heights = []

        for i in range(self.COLUMNS):
            self._heights.append(0)

        # Remember all the winners and losers
        self._scores = []

    # Add a winner
    def add_winner(self, player):

        # Add the number to the winners list
        self._scores.append(player)

    # Print the board centered
    def print_board(self, start=False):

        # Check if start
        if start:
            delay = 0.5
        else:
            delay = 0

        # Declare numbers string
        numbers = " "

        # Print the numbers
        for i in range(self.COLUMNS):

            # Check if it is large
            if self._heights[i] == self.ROWS:
                numbers += "  "

            # Else add the number
            else:
                numbers += f"{i + 1} "

        # Once finished, add the string
        print(string_centre(numbers, border=" "))

        # Delay for suspense
        sleep(start)

        # Iterate through 2d graph
        for i in range(self.ROWS):

            # Create string line
            string_line = "|"

            # Create list of colors
            colors = [color.BLUE]

            # Iterate each row
            for j in range(self.COLUMNS):

                # Write the board
                if self._board[i][j] == 0:
                    string_line += " "
                elif self._board[i][j] == 1:
                    string_line += "0"
                    colors.append(self.players[1].color)
                elif self._board[i][j] == 2:
                    string_line += "0"
                    colors.append(self.players[2].color)
                else:
                    string_line += "0"
                    colors.append(color.GREEN)

                # Add the line
                string_line += "|"
                colors.append(color.BLUE)

            # Center the string
            string_line = string_centre(string_line, border=" ")

            # Print it
            delay_print(string_line, delay=0, edit=colors, ignore=" ")

            # Wait for suspense
            sleep(start)

        # Once finished print the bottom
        delay_print(
            string_centre("---------------", border=" "), delay=0, edit=[color.BLUE]
        )

    # Insert into a column
    def insert(self, column, player):

        # Find where to place it
        place = self.ROWS - self.heights[column - 1] - 1

        # Insert place into board
        self._board[place][column - 1] = player

        # Add one more to the heights
        self._heights[column - 1] += 1

        # Iterate through graph to find winner
        for y in range(self.ROWS):
            for x in range(self.COLUMNS):
                if self.board[y][x] != 0:
                    if self.find_winner(y, x):
                        return True

        # If there is no winner
        return False

    # Reset the board
    def reset(self):

        # Iterate through the entire board
        for x in range(self.COLUMNS):

            # Reset the height
            self._heights[x] = 0

            for y in range(self.ROWS):

                # Reset each tile to zero
                self._board[y][x] = 0

    # Check which columns are available to place a counter
    def get_valid(self):

        # Declare result list
        result = []

        # Iterate through all heights
        for i in range(self.COLUMNS):

            # If heights is not 6
            if self.heights[i] != self.ROWS:
                result.append(i + 1)

        # Return the results once done
        return result

    # Try to find the winner in the array
    def find_winner(self, row, column, path=[0, 0], iterate=1):

        # Iterate through all of the possible ways
        if path == [0, 0]:

            # Iterate through the rows
            for y in range(-1, 2):

                # Iterate through the columns
                for x in range(-1, 2):

                    # If one same tile
                    if y == 0 and x == 0:
                        next
                    else:

                        # Check for sameness
                        try:
                            if self.index_board(row, column) == self.index_board(
                                row + y, column + x
                            ):

                                # See if find winner = true
                                if self.find_winner(
                                    row=row + y,
                                    column=column + x,
                                    path=[y, x],
                                    iterate=iterate + 1,
                                ):

                                    # Change to 3 for winner
                                    self._board[row][column] = 3
                                    return True

                        # If index is out of range
                        except IndexError:
                            pass

        # If there is a path
        else:
            # Check if the block is the same
            try:
                # Find check the path
                if self.index_board(row, column) == self.index_board(
                    row + path[0], column + path[1]
                ):

                    # Check if iterations are enough
                    iterate += 1

                    # If there is a winner
                    if iterate == self.CONNECT:
                        self._board[row][column] = 3
                        self._board[row + path[0]][column + path[1]] = 3
                        return True

                    # Else go to next node
                    if self.find_winner(
                        row=row + path[0],
                        column=column + path[1],
                        path=path,
                        iterate=iterate,
                    ):
                        self._board[row][column] = 3
                        return True

            # If it is out of index
            except IndexError:
                pass

        # If none is found
        return False

    # Get index but if negative, index error
    def index_board(self, y, x):

        # Check if index is negative
        if y < 0 or x < 0:
            raise IndexError
        return self.board[y][x]

    # Print the winner once finished
    def print_winner(self):

        # GOAL: Print winner with suspense
        print("Calculating the winner...")
        sleep(0.5)

        # Iterate through each win and lose and tie
        for i, winner in enumerate(self.scores):

            # Check if it is a tie
            if winner == 0:
                print(color.BLUE + f"Game {i}: Tie" + color.END)

            # If it is not a tie
            else:

                # Add one to the winner
                self.players[winner].add_win()

                # Print the winner and the color
                print(
                    self.players[winner].color
                    + f"Game {i}: {self.players[winner].name}"
                    + color.END
                )

            # Delay for suspense
            sleep(0.5)

        # Once finished declare the winner
        delay_print("The winner is", end="")
        delay_print("......... ", delay=0.25, end="")

        # Check if it is a tie
        if self.players[1].win == self.players[2].win:
            print(color.BLUE + "Tie!" + color.END, end="")

        # Check if player 1 won
        elif self.players[1].win > self.players[2].win:
            print(
                self.players[1].color + f"{self.players[1].name}!" + color.END, end=""
            )

        # If player 2 won
        else:
            print(
                self.players[2].color + f"{self.players[2].name}!  " + color.END
            )

        # Print the scores
        print(
            self.players[1].color
            + f"{self.players[1].win}"
            + color.END
            + "-"
            + self.players[2].color
            + f"{self.players[2].win}"
            + color.END
        )

    @property
    def heights(self):
        return self._heights

    @property
    def board(self):
        return self._board

    @property
    def players(self):
        return self._players

    @property
    def scores(self):
        return self._scores


# Print center text
def string_centre(*strings: str, border="=", sep=" ") -> str:

    # Get the length of the terminal
    size = os.get_terminal_size().columns

    # Combine the strings
    text = f" {' '.join(strings)} "

    # Centre the text
    return text.center(size, border)


# Clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Delay printing text
def delay_print(text, delay=0.05, end="\n", edit=[""], ignore=None):

    # Get length of the edit
    length = len(edit)

    # Print
    i = 0
    for char in text:
        sys.stdout.write(edit[(i % length)] + char + color.END)
        sys.stdout.flush()
        sleep(delay)
        if char != ignore:
            i += 1

    # Print the end argument
    print(end=end)


# Print the connect four framework
def print_frame(delay=0) -> None:

    # Clear the terminal
    clear()

    # Print the logo
    delay_print(
        string_centre("Connect Four") + "\n",
        delay=delay,
        edit=[color.YELLOW + color.BOLD, color.RED + color.BOLD],
    )


# Get the user name
def get_name(player: int) -> str:

    # Get the user input
    name = input(f"Player {player} name: ")

    # Check if name is nothing
    if name == "":
        name = f"Player {player}"

    # Return the name
    return name.title().strip()


# Get the user input of either 1 or 2
def select(txt="", select=[1, 2], nl=True, prompt1_nothing=False):

    # If new line is true
    if nl:
        print()

    # Forever forloop
    while True:
        try:

            # Check if prompt1 is nothing
            if prompt1_nothing == True:
                prompt1_nothing = False
                number = int(input().strip())
            else:
                number = int(input(txt).strip())

            # Check if number is valid
            if number in select:
                return number
            else:
                raise ValueError
        except ValueError:
            print(f"Usage: {select}")


# Color selection
class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[1m"
    END = "\033[0m"
