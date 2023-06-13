import os
import json
import shutil

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

"""
def print_header():
    print("-" * 50)
    print("{:^50}".format("Game Lizard"))
    print("-" * 50)
"""

def print_header():
    columns, _ = shutil.get_terminal_size()
    with open("header2.txt", 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            print(f"{line.center(columns)}")

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_categories():
    # Function to display available game categories
    clear_screen()
    print_header()
    print("Choose Thy Categorie:")
    index = 1
    for category in sorted(game_categories.keys()):
        print("{}. {}".format(index, category))
        index += 1
    print()

def display_games(category):
    # Function to display games in a specific category
    clear_screen()
    print_header()
    print("Games in the '{}' Category:".format(category))
    games = sorted(game_categories[category])
    index = 1
    for game in games:
        print("{}. {}".format(index, game))
        index += 1
    print()

def launch_game(game):
    # Function to launch a selected game
    clear_screen()
    print("Launching {}...".format(game))
    if game in game_commands:
        command = game_commands[game]
        os.system(command)
        print("Enjoy Thy game!")
    else:
        print("Thou art a Fool! There is no command to launch thy game.")
    input("Press Enter to continue...")
    display_categories()

# Main game launcher loop
while True:
    display_categories()
    category_choice = input("Choose Thy Categorie [1-9] (or 'q' to exit): ")
    if category_choice == "q":
        break
    elif category_choice.isdigit():
        category_choice = int(category_choice)
        if 1 <= category_choice <= len(game_categories):
            categories = sorted(game_categories.keys())
            selected_category = categories[category_choice - 1]
            display_games(selected_category)
            game_choice = input("Choose Thy Game number (or go 'b'ack or 'q'uit): ")
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
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
