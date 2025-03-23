import os
import json
import shutil
import time
import curses

# ANSI escape sequence constants
TEXT_BOLD = "\033[1m"
TEXT_RESET = "\033[0m"
TEXT_COLOR_RED = "\033[31m"
TEXT_COLOR_GREEN = "\033[32m"
TEXT_COLOR_YELLOW = "\033[33m"
TEXT_COLOR_MAGENTA = "\033[35m"
TEXT_COLOR_CYAN = "\033[36m"

# Load game data from JSON file
with open("game_data.json", "r") as file:
    data = json.load(file)
game_categories = data["categories"]
game_commands = data["commands"]

def print_centered(stdscr, text, y=None):
    height, width = stdscr.getmaxyx()
    x = width // 2 - len(text) // 2
    y = height // 2 if y is None else y
    stdscr.addstr(y, x, text)

def display_menu(stdscr, title, items, extra_line=""):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Print the extra line above the title if provided
        if extra_line:
            extra_line_y = 1  # Adjust this value to change the position
            print_centered(stdscr, extra_line, extra_line_y)

        # Print the title
        title_y = 3 if extra_line else 1  # Adjust title position based on extra line
        print_centered(stdscr, title, title_y)

        for idx, row in enumerate(items):
            x = width // 2 - len(row) // 2
            y = height // 2 - len(items) // 2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        
        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(items) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_row
        elif key in [ord('q'), ord('Q')]:
            return None


def launch_game(stdscr, game):
    # Clear the screen
    stdscr.clear()

    # Check if the game command exists
    if game in game_commands:
        command = game_commands[game]

        # Display launching message
        print_centered(stdscr, f"Launching {game}...", 0)
        stdscr.refresh()
        time.sleep(2)

        # Clear the screen and launch the game
        stdscr.clear()
        stdscr.refresh()
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(command)

        # After game execution, return to the menu
        stdscr.clear()
        print_centered(stdscr, f"Finished playing {game}. Press any key to return.", 0)
        stdscr.refresh()
        stdscr.getch()
    else:
        # Game command not found
        print_centered(stdscr, f"No command found to launch {game}.", 0)
        stdscr.refresh()
        time.sleep(2)

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_MAGENTA)
    extra_line = "Game Wizard II"  # Define the extra line text

    while True:
        # Display categories with the extra line
        choice = display_menu(stdscr, "Select Category", sorted(game_categories.keys()), extra_line)
        if choice is None or choice == len(game_categories):
            break

        category = sorted(game_categories.keys())[choice]

        # Display games within the selected category with the extra line
        game_choice = display_menu(stdscr, f"Select Game in {category}", sorted(game_categories[category]) + ["\nBack"], extra_line)
        if game_choice is None or game_choice == len(game_categories[category]):
            continue

        game = sorted(game_categories[category])[game_choice]
        launch_game(stdscr, game)

curses.wrapper(main)
