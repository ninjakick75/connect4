# Import connect and other files
import os
from helper import Player, get_name, print_frame, select, clear, color, delay_print

# Small dictionary of colors
colors = {
    1 : color.RED
    2: color.YELLOW
}


# Main function
def main():

    # Clear the terminal
    clear()

    # Print the connect four
    print_frame(delay=0.01)

    # Ask user for each player's name
    name1 = get_name(1)
    print_frame()
    name2 = get_name(2)
    print_frame()

    # Ask user to choose their color
    delay_print(f"{name1}, choose your color:\n")
    delay_print("1: RED\n", edit=[color.RED])
    delay_print("2: YELLOW\n", edit=[color.YELLOW])
    selection = select("Choose: ")



# Run code
if __name__ == "__main__":
    main()
