# Game wizard, fast edition, for when things have to go a bit faster, without beeping

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
BACKGROUND_COLOR_CYAN = "\033[46m"
BACKGROUND_COLOR_GREEN = "\033[42m"
BACKGROUND_COLOR_WHITE = "\033[47m"
BACKGROUND_COLOR_RESET = "\033[49m"

# ANSI escape sequences for text colors
TEXT_COLOR_CYAN = "\033[36m"
TEXT_COLOR_RESET = "\033[0m"

# ANSI escape sequences for background colors
BACKGROUND_COLOR_BLACK = "\033[40m"
BACKGROUND_COLOR_RESET = "\033[49m"

# Load the JSON file

with open ("/home/jan/git/scripts/pygames/game_data.json", "r") as file:
    data = json.load(file)

# Retrieve the game categories and commands
game_categories = data["categories"]
game_commands = data["commands"]

def print_file_with_delay(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print_with_delay(line)

def print_with_delay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)

def display_center_text_with_delay(text, delay=0.01):
    columns = shutil.get_terminal_size().columns
    centered_text = text.rstrip().center(columns)
    for line in centered_text.splitlines():
        print_with_delay(line)
        time.sleep(delay)

def print_with_delay_header(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(1.5)

def print_centered(line):
    # Get the terminal size
    terminal_size = shutil.get_terminal_size()

    # Calculate the number of spaces needed for horizontal centering
    spaces = (terminal_size.columns - len(line)) // 2

    # Calculate the number of lines needed for vertical centering
    lines = (terminal_size.lines - 1) // 2

    # Print empty lines for vertical centering
    for _ in range(lines):
        print()

    # Print spaces for horizontal centering
    print(' ' * spaces, end='')

    # Print the line with a time delay
    print_with_delay(line)

    # Print a new line after the line is printed
    print()

# print one line strings in the center with delay
def display_center_text(text):
    columns = shutil.get_terminal_size().columns
    centered_text = text.rstrip().center(columns)
    print(centered_text)

def greeter():
    clear_screen()
    print_centered(TEXT_COLOR_MAGENTA + TEXT_BOLD + "Initializing Game Wizard\n")
    print_centered("." * 50 + TEXT_RESET)

# Print the header, make it so it displays in the center
def print_header():
    columns, _ = shutil.get_terminal_size()
    with open("/home/jan/git/scripts/pygames/header2.txt", 'r') as file:
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
    print(TEXT_COLOR_CYAN + TEXT_BOLD + "\n -> CATEGORIES:\n" + TEXT_COLOR_RESET)
    index = 1
    for category in sorted(game_categories.keys()):
        print(TEXT_BOLD + TEXT_COLOR_GREEN + "{}. {}".format(index, category)+ TEXT_RESET)
        index += 1
    print()
    print(TEXT_COLOR_MAGENTA + TEXT_BOLD + "The Wizard: "+ TEXT_COLOR_RESET +TEXT_COLOR_YELLOW + TEXT_BOLD + "What is Thy answer?" + TEXT_COLOR_RESET)

def display_games(category):
    # Function to display games in a specific category
    clear_screen()
    print_header()
    print(TEXT_BOLD + TEXT_COLOR_CYAN + "\n -> {}\n".format(category) + TEXT_RESET)
    games = sorted(game_categories[category])
    index = 1
    for game in games:
        print(TEXT_BOLD + TEXT_COLOR_GREEN + "{}. {}".format(index, game) + TEXT_RESET)
        index += 1
    print()
    print(TEXT_COLOR_MAGENTA + TEXT_BOLD + "The Wizard: "+ TEXT_COLOR_RESET +TEXT_COLOR_YELLOW + TEXT_BOLD + "What is Thy answer?" + TEXT_COLOR_RESET)

def launch_game(game):
    # Function to launch a selected game
    clear_screen()
    print_with_delay(TEXT_BOLD + TEXT_COLOR_YELLOW + " -> preparing ritual to summon {}...".format(game) + "\n\n" + TEXT_RESET)
    print_with_delay(TEXT_BOLD + TEXT_COLOR_RED + " -> evoking the machine spirit" + "\n\n"+ TEXT_RESET)
    print_with_delay(TEXT_BOLD + TEXT_COLOR_GREEN + " -> booting up..." + "\n\n"+ TEXT_RESET)
    print_with_delay(TEXT_BOLD + TEXT_COLOR_CYAN + " -> accessing stuff & shit..." + "\n\n"+ TEXT_RESET)
    print_with_delay(TEXT_BOLD + TEXT_COLOR_RED + " -> done!" + "\n\n"+ TEXT_RESET)
    clear_screen()
    if game in game_commands:
        command = game_commands[game]
        os.system(command)
        clear_screen()
        print_with_delay(TEXT_BOLD + TEXT_COLOR_YELLOW +"\n I hope you had fun wasting your time playing {}!\n".format(game) + TEXT_RESET)
    else:
        clear_screen()
        print_with_delay(TEXT_COLOR_RED + TEXT_BOLD + "The Wizard says: Thou art a Fool! There is no command to launch {}!\n".format(game) + TEXT_RESET)
    input(TEXT_BOLD + TEXT_COLOR_RED +"\nPress Enter to continue..."+ TEXT_COLOR_RESET)
    display_categories()

while True:
    display_categories()
    category_choice = input(TEXT_COLOR_RED + TEXT_BOLD + "\nThou sayest: " + TEXT_RESET + TEXT_COLOR_GREEN + TEXT_BOLD)
    if category_choice == "q":
        break
    elif category_choice == "x":
        break
    elif category_choice.isdigit():
        category_choice = int(category_choice)
        if 1 <= category_choice <= len(game_categories):
            categories = sorted(game_categories.keys())
            selected_category = categories[category_choice - 1]
            display_games(selected_category)
            game_choice = input(TEXT_BOLD + TEXT_COLOR_RED + "\nThou sayest: " + TEXT_RESET + TEXT_COLOR_GREEN + TEXT_BOLD)
            if game_choice == "b":
                continue
            elif game_choice == "q":
                break
            elif game_choice == "x":
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
