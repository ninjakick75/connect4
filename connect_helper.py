# Import packages
import os

class Player:

    # Constructor class
    def __init__(self, color):
        self.win = 0
        self.lose = 0
        self.color = color


# Print center text
def string_centre(*strings : str, border="=", sep=" "):

    # Get the length of the terminal
    size = os.get_terminal_size().columns

    # Combine the strings
    text = f" {' '.join(strings)} "
    
    # Centre the text
    return text.center(size, border)


# Clear the screen
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

