# Import packages
import os
import sys
from time import sleep


class Player:

    # Constructor class
    def __init__(self, color, name):
        self.name = name
        self.win = 0
        self.lose = 0
        self.color = color


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
def delay_print(text, delay=0.05, end="\n", edit=[""]):

    # Get length of the edit
    length = len(edit)

    # Print
    for i, char in enumerate(text):
        sys.stdout.write(edit[(i % length) - 1] + char + color.END)
        sys.stdout.flush()
        sleep(delay)

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
    if name == "": name = f"Player {player}"

    # Return the name
    return name.title().strip()


# Get the user input of either 1 or 2
def select(txt, select=[1,2]):
    print()
    while True:
        try:
            number = int(input(txt).strip())
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
