import os
import json
import shutil
import subprocess
import time

# ANSI escape sequence for text formatting
TEXT_BOLD = "\033[1m"
TEXT_RESET = "\033[0m"

# ANSI escape sequences for text colors
TEXT_COLOR_RED = "\033[31m"
TEXT_COLOR_GREEN = "\033[32m"
TEXT_COLOR_YELLOW = "\033[33m"
TEXT_COLOR_MAGENTA = "\033[35m"
TEXT_COLOR_RESET = "\033[0m"

# ANSI escape sequences for background colors
BACKGROUND_COLOR_BLUE = "\033[44m"
BACKGROUND_COLOR_WHITE = "\033[47m"
BACKGROUND_COLOR_RESET = "\033[49m"

# ANSI escape sequences for text colors
TEXT_COLOR_CYAN = "\033[36m"
TEXT_COLOR_RESET = "\033[0m"

# ANSI escape sequences for background colors
BACKGROUND_COLOR_BLACK = "\033[40m"
BACKGROUND_COLOR_RESET = "\033[49m"

# Load the JSON file

with open ("game_data.json", "r") as file:
    data = json.load(file)

# Retrieve the game categories and commands
game_categories = data["categories"]
game_commands = data["commands"]


### old header code
"""
def print_header():
    print("-" * 50)
    print("{:^50}".format("Game Lizard"))
    print("-" * 50)
"""

def print_file_with_delay(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print_with_delay(line)

def print_with_delay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)

def print_with_delay_header(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)
# header, placed in the center

def print_ddate():
    columns, _ = shutil.get_terminal_size()
    print_with_delay("Greetings, Master!\n")
    print_with_delay(os.system('ddate'))
    print_with_delay(os.system('date'))
    print("\n")

# Print the header, make it so it displays in the center
def print_header():
    columns, _ = shutil.get_terminal_size()
    with open("header2.txt", 'r') as file:
        for line in file:
            line = line.rstrip('\n') # remove unneccessary crud
            print(TEXT_COLOR_MAGENTA + f"{line.center(columns)}" + TEXT_COLOR_RESET)

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_categories():
    # Function to display available game categories
    clear_screen()
    print_header()
    print(TEXT_COLOR_MAGENTA + TEXT_BOLD + "Categories:" + TEXT_COLOR_RESET)
    index = 1
    for category in sorted(game_categories.keys()):
        print(TEXT_BOLD + TEXT_COLOR_GREEN + "{}. {}".format(index, category)+ TEXT_RESET)
        index += 1
    print()

def display_games(category):
    # Function to display games in a specific category
    clear_screen()
    print_header()
    print(TEXT_BOLD + TEXT_COLOR_MAGENTA + "Games in the '{}' Category:".format(category) + TEXT_RESET)
    games = sorted(game_categories[category])
    index = 1
    for game in games:
        print(TEXT_BOLD + TEXT_COLOR_GREEN + "{}. {}".format(index, game) + TEXT_RESET)
        index += 1
    print()

def launch_game(game):
    # Function to launch a selected game
    clear_screen()
    print_header()
    print_with_delay(TEXT_BOLD + TEXT_COLOR_MAGENTA + "Launching {}...\n".format(game) + TEXT_RESET)
    if game in game_commands:
        command = game_commands[game]
        os.system(command)
        clear_screen()
        print_header()
        print_with_delay("I hope you had fun playing {}!\n".format(game))
    else:
        clear_screen()
        print_header()
        print_with_delay(TEXT_COLOR_RED + TEXT_BOLD + "The Wizard says: Thou art a Fool! There is no command to launch {}!\n".format(game) + TEXT_RESET)
    input("\nPress Enter to continue...")
    display_categories()


""" Add the following code if you want to have more options for easter eggs, config etc.
def display_options():
    # Function to display additional options
    print("Additional Options:")
    print("a. Edit Game Database")
    print("b. Reload Game Database")
    print("c. PRESS AT THY OWN RISK & PERIL!")
    print()

def handle_option_selection(option):
    # Function to handle the selected option
    clear_screen()
    print_header()
    if option == 'a':
        print("launching vim to edit gmsdata.py")
        time.sleep(2) # Sleep for 2 seconds
        subprocess.run(["nvim", "gmsdata.py"])
    elif option == 'b':
        print("You selected Option b.")
        subprocess.run(["python3", "gmsdata.py"])
    elif option == 'c':
        print("You selected Option c.")
    else:
        print("Invalid option.")
"""


while True:
    display_categories()
    """
    display_options()
    """
    category_choice = input(TEXT_COLOR_MAGENTA + TEXT_BOLD + "Choose Thy Categorie [1-9] (or 'q' to exit): ")
    if category_choice == "q":
        break
    elif category_choice.isdigit():
        category_choice = int(category_choice)
        if 1 <= category_choice <= len(game_categories):
            categories = sorted(game_categories.keys())
            selected_category = categories[category_choice - 1]
            display_games(selected_category)
            game_choice = input(TEXT_BOLD + TEXT_COLOR_MAGENTA + "Choose Thy Game number (or go 'b'ack or 'q'uit): " + TEXT_RESET)
            if game_choice == "b":
                continue
            elif game_choice == "q":
                break
            elif game_choice.isdigit():
                game_choice = int(game_choice)
                games = sorted(game_categories[selected_category])
                if 1 <= game_choice <= len(games):
                    selected_game = games[game_choice - 1]
                    launch_game(selected_game)
                else:
                    print("Invalid game selection!")
                    input("Press Enter to continue...")
            else:
                print("Invalid input!")
                input("Press Enter to continue...")
        else:
            print("Invalid category selection!")
            input("Press Enter to continue...")

            """ Game loop code for additional options selectable with alpha
    elif category_choice.isalpha() and len(category_choice) == 1:
        category_choice = category_choice.lower()
        if category_choice in ('a', 'b', 'c'):
            handle_option_selection(category_choice)
        else:
            print("Invalid option!")
            input("Press Enter to continue...")
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
        """
