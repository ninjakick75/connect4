# Import packages
import os
import sys
from time import sleep


class Player:

    # Constructor class
    def __init__(self, color, name):
        self._name = name
        self._win = 0
        self._color = color

    # If player wins, add a win for them
    def add_win(self):
        self._win += 1

    @property
    def name(self):
        return self._name

    @property
    def win(self):
        return self._win

    @property
    def color(self):
        return self._color



class Board:

    # Constant variables
    COLUMNS = 7
    ROWS = 6

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
        self.players = dict

        # Add the connect four coloum heights
        self._heights = []

        for i in range(self.COLUMNS):
            self._heights.append(0)

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
                    colors.append(self._players[1].color)
                else:
                    string_line += "0"
                    colors.append(self._players[2].color)
                
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
        delay_print(string_centre("---------------", border=" "), delay=0, edit=[color.BLUE])
                



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
        sys.stdout.write(edit[(i % length) - 1] + char + color.END)
        sys.stdout.flush()
        sleep(delay)
        if char != ignore:
            i += 1

    # Print the end argument
    print(end=end)


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
    if nl: print()

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