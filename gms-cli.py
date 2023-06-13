import os

# Dictionary to hold game categories and their associated games
game_categories = {
                "DOS": ["Albion", "Caster of Magic", "Commander Keen", "Daggerfall", "Siedler 2"],
                "Wine": ["Arcanum", "Emperor", "Diablo II", "Stronghold", "Pharaoh", "Weltwunder", "Zeus"],
            "Steam": ["Game 2"],
            "Native": ["Widelands"],
            "Emulators": ["Game 2"],
}

# Dictionary to hold game commands
game_commands = {
    # DOS
    "Albion": "dosbox -conf ~/.dosbox/albion.conf",
    "Caster of Magic": "dosbox -conf ~/.dosbox/com.conf",
    "Commander Keen": "dosbox -conf ~/.dosbox/keen.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    "Siedler 2": "dosbox -conf ~/.dosbox/s2.conf",
    # wine
    "Emperor": "wine ~/Spiele/emperor/ && wine Emperor.exe",
    # Native
    "Widelands": "widelands",
    # Emulators
    "RetroArch": "retroarch",
}

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_categories():
    # Function to display available game categories
    clear_screen()
    print("Game Serpent Wizard 1.0")
    print("Available Categories:")
    index = 1
    for category in sorted(game_categories.keys()):
        print("{}. {}".format(index, category))
        index += 1
    print()

def display_games(category):
    # Function to display games in a specific category
    clear_screen()
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
        print("Enjoy the game!")
    else:
        print("No command found to launch the game.")
    input("Press Enter to continue...")
    display_categories()

# Main game launcher loop
while True:
    display_categories()
    category_choice = input("Enter the category number (or 'quit' to exit): ")
    if category_choice == "quit":
        break
    elif category_choice.isdigit():
        category_choice = int(category_choice)
        if 1 <= category_choice <= len(game_categories):
            categories = sorted(game_categories.keys())
            selected_category = categories[category_choice - 1]
            display_games(selected_category)
            game_choice = input("Enter the game number (or 'back' to go back): ")
            if game_choice == "back":
                continue
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

