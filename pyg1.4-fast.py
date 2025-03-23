import curses
import json
import os

# ----------------------------------------------------------------------
# Load your JSON data
# ----------------------------------------------------------------------
with open("/home/jan/git/scripts/pygames/game_data.json", "r") as file:
    data = json.load(file)

game_categories = data["categories"]
game_commands = data["commands"]

# Flatten all games into a single list (or keep them separated by category).
all_games = []
for cat, games in game_categories.items():
    for g in games:
        if g not in all_games:
            all_games.append(g)
all_games.sort()

# ----------------------------------------------------------------------
# Search utility
# ----------------------------------------------------------------------
def search_games(search_term):
    """
    Return a sorted list of matching games (case-insensitive partial match).
    If the search_term is empty, returns ALL games.
    """
    if not search_term:
        return all_games
    search_term_lower = search_term.lower()
    matches = [g for g in all_games if search_term_lower in g.lower()]
    return sorted(matches)

# ----------------------------------------------------------------------
# Run a game outside curses, then re-init curses so we can come back
# ----------------------------------------------------------------------
def run_game_in_normal_mode(stdscr, game_name):
    """
    1) End curses
    2) Clear terminal, run the game
    3) Wait for user input
    4) Re-init curses
    5) Return the new curses window object
    """
    curses.endwin()  # exit curses mode
    os.system("clear")
    print(f"Launching {game_name}...")

    cmd = game_commands.get(game_name)
    if cmd:
        os.system(cmd)
    else:
        print(f"No command found for game: {game_name}")

    input("\nPress Enter to return to the wizard...")

    # Re-initialize curses after the game exits
    new_stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    new_stdscr.keypad(True)

    # If you want color, re-init color pairs
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    return new_stdscr

# ----------------------------------------------------------------------
# Main curses loop
# ----------------------------------------------------------------------
def curses_main(stdscr):
    # Basic curses setup
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)

    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    search_string = ""
    filtered_results = search_games(search_string)
    highlight_index = 0

    while True:
        # Clear the screen every loop iteration
        stdscr.clear()

        # Current terminal size
        height, width = stdscr.getmaxyx()

        # Show instructions
        stdscr.addstr(0, 0, "PYGAMES v1.4 by qrzn")
        stdscr.addstr(1, 0, "Type to search (Esc to quit).")
        stdscr.addstr(2, 0, "Use Up/Down to highlight. Enter to launch the highlighted game.")
        stdscr.addstr(3, 0, f"Search: {search_string}")

        # Display the filtered results
        for i, game_name in enumerate(filtered_results):
            # Are we on the currently highlighted line?
            if i == highlight_index:
                if curses.has_colors():
                    stdscr.attron(curses.color_pair(2))  # "inverted" color
                # Truncate output if game name is wider than terminal
                stdscr.addstr(4 + i, 0, game_name[:width-1])
                if curses.has_colors():
                    stdscr.attroff(curses.color_pair(2))
            else:
                if curses.has_colors():
                    stdscr.attron(curses.color_pair(1))  # normal color
                stdscr.addstr(4 + i, 0, game_name[:width-1])
                if curses.has_colors():
                    stdscr.attroff(curses.color_pair(1))

            # If we approach the bottom of the screen, stop rendering
            if (4 + i) >= (height - 1):
                break

        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Check for exit keys
        if key == 27:  # Esc
            break

        if key == curses.KEY_BACKSPACE or key == 127:
            # Remove last char from the search string
            if len(search_string) > 0:
                search_string = search_string[:-1]
                filtered_results = search_games(search_string)
                highlight_index = 0
        elif key == curses.KEY_DOWN:
            if filtered_results:
                highlight_index = (highlight_index + 1) % len(filtered_results)
        elif key == curses.KEY_UP:
            if filtered_results:
                highlight_index = (highlight_index - 1) % len(filtered_results)
        elif key in (curses.KEY_ENTER, 10, 13):
            # Enter => launch the highlighted game (if any)
            if filtered_results:
                selected_game = filtered_results[highlight_index]
                # Launch the game outside curses and come back
                stdscr = run_game_in_normal_mode(stdscr, selected_game)
                # After returning, reset our local variables
                search_string = ""
                filtered_results = search_games(search_string)
                highlight_index = 0
        else:
            # If it's a printable character, add to the search string
            if 32 <= key < 127:
                search_string += chr(key)
                filtered_results = search_games(search_string)
                highlight_index = 0

def main():
    curses.wrapper(curses_main)

if __name__ == "__main__":
    main()
