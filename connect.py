# Import connect and other files
import os
from helper import Player, get_name, print_frame, select, clear, color, delay_print
from game import play_game
from random import randint
from time import sleep

# Small dictionary of colors
colors = {
    1 : color.RED,
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
    delay_print("2: YELLOW", edit=[color.YELLOW])
    selection = select("Choose: ")

    # Create the new players
    player1 = Player(colors[selection], name1)
    player2 = Player(colors[(selection % 2) + 1], name2)

    # Create dictionary of the players
    players = {
        1 : player1,
        2: player2
    }

    # Ask for who to go first
    print_frame()
    delay_print("Who should go first?\n")
    delay_print(f"1: {player1._name}\n", edit=[player1._color])
    delay_print(f"2: {player2._name}\n", edit=[player2._color])
    delay_print("3: Random")
    
    # Get the user input
    first = select("Choose: ", select=[1,2,3])

    # Check if input is 3
    if first == 3:
        first = randint(1,2)

    # Tell the user who is going first
    print_frame()
    delay_print(f"{players[first]._name} is going first", edit=[players[first]._color])
    sleep(1)
    print_frame()

    # Start the game
    play_game(players, first)




# Run code
if __name__ == "__main__":
    main()
