import os
import json

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

# Dictionary to hold game categories and their associated games
game_categories = {
    "DOS": [
        "Albion",
        "Arena",
        "Ascendancy",
        "Centurion",
        "Civilization",
        "Caster of Magic",
        "Commander Keen", 
        "Daggerfall", 
        "Darklands", 
        "Duke Nukem 3D", 
        "Dune II", 
        "Master of Magic", 
        "Master of Orion", 
        "Master of Orion II - Battle at Antares", 
        "Pirates!", 
        "Ultima", 
        "Quake", 
        "Siedler 2", 
        "Shadow Warrior", 
        "Ultima", 
        "Ultima Underworld",
        "Veil of Darkness", 
        "Zeliard"
        ],
    "RPG": [
        "Albion",
        "Arena",
        "Arcanum",
        "Daggerfall",
        "Daggerfall Unity",
        "Darklands",
        "Diablo II",
        "Exult",
        "Fallout",
        "Fallout 2",
        "Fallout New Vegas",
        "OpenMW",
        "Ultima 4-6",
        "Ultima Underworld",
        "Veil of Darkness",
        ],
    "Strategy": [
        "Ascendancy",
        "Civilization",
        "Centurion",
        "Dungeon Keeper II",
        "Factorio",
        "Emperor",
        "Caster of Magic",
        "Master of Magic",
        "Master of Orion",
        "Master of Orion II - Battle at Antares",
        "Siedler 2",
        "Stronghold",
        "Stronghold Crusader",
        "Stronghold Crusader Extreme",
        "Pharaoh",
        "War Wind",
        "Weltwunder",
        "Zeus",
        ],
    "Action": [
        "Albion",
        "Arena",
        "Commander Keen",
        "Duke Nukem 3D",
        "Half-Life",
        "Pirates!",
        "Quake",
        ],
    "4X": [
        "Civilization",
        "Master of Magic",
        "Master of Orion",
        "Caster of Magic",
        "Master of Orion II - Battle at Antares",

        ],
    "Steam": [
        "Civilization",
        "Master of Magic",
        "Master of Orion",
        "Caster of Magic",
        "Master of Orion II - Battle at Antares",

        ],
    "Indie": [
        "Don't Starve",
        "Factorio",
        "Starbound",
        "Stardew Valley",
        ],
    "Wine": [
        "Arcanum", 
        "Emperor", 
        "Diablo II", 
        "Dungeon Keeper II", 
        "Fallout", 
        "Fallout 2", 
        "Fallout New Vegas", 
        "Galactic Civilizations II", 
        "Stronghold", 
        "Stronghold Crusader", 
        "Stronghold Crusader Extreme",
        "Pharaoh", 
        "War Wind", 
        "Weltwunder", 
        "Zeus"
        ],
    "Native": [
        "Exult", 
        "Factorio", 
        "Don't Starve", 
        "Daggerfall Unity", 
        "Return to the Roots", 
        "OpenMW", 
        "Stardew Valley", 
        "Starbound", 
        "The Ur-Quan Masters",
        "Widelands",
        "Valhalla"
        ],
    "Emulators": ["RetroArch", "ScummVM"],
}

# Dictionary to hold game commands
game_commands = {
    # DOS
    "Albion": "dosbox -conf ~/.dosbox/albion.conf",
    "Arena": "dosbox -conf ~/.dosbox/arena.conf",
    "Caster of Magic": "dosbox -conf ~/.dosbox/com.conf",
    "Commander Keen": "dosbox -conf ~/.dosbox/keen.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    "Dune 2": "dosbox -conf ~/.dosbox/dune2.conf",
    "Siedler 2": "dosbox -conf ~/.dosbox/s2.conf",
    "Master of Orion": "dosbox -conf ~/.dosbox/moo.conf",
    "Master of Magic": "dosbox -conf ~/.dosbox/mom.conf",
    "Ultima 4-6": "dosbox -conf ~/.dosbox/ultima.conf",
    "Ultima Underworld": "dosbox -conf ~/.dosbox/uuw.conf",
    "Pirates!": "dosbox -conf ~/.dosbox/pirates.conf",
    "Quake": "dosbox -conf ~/.dosbox/quake.conf",
    "Veil of Darkness": "dosbox -conf ~/.dosbox/veil.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    # wine
    "Arcanum": "cd ~/Spiele/wine/Arcanum/ && wine Arcanum.exe",
    "Emperor": "cd ~/Spiele/wine/emperor/ && wine Emperor.exe",
    "Diablo II": "cd ~/Spiele/wine/diablo2/ && wine Game.exe",
    "Fallout": "cd ~/Spiele/wine/fallout/ && wine FALLOUTW.exe",
    "Fallout 2": "cd ~/Spiele/wine/fallout2/ && wine fallout2.exe",
    "Dungeon Keeper II": "cd ~/Spiele/wine/dk2/ && wine DKII-DX.exe",
    "Galactic Civilizations II": "cd ~/Spiele/wine/galciv2/ && wine Game.exe",
    "Stronghold": "cd ~/Spiele/wine/stronghold/ && wine Stronghold.exe",
    "Stronghold Crusader": "cd ~/Spiele/wine/strongholdchd/ && wine shc.exe",
    "Stronghold Crusader Extreme": "cd ~/Spiele/wine/strongholdchd/ && wine shc.exe",
    "Pharaoh": "cd ~/Spiele/wine/pharaoh/ && wine Pharaoh.exe",
    "War Wind": "cd ~/Spiele/wine/warwind/ && wine WW.exe",
    "Weltwunder": "cd ~/Spiele/wine/c4/ && wine Game.exe",
    "Zeus": "cd ~/Spiele/wine/zeus/ && wine Zeus.exe",
    # Native
    "Daggerfall Unity": "~/Spiele/dfu/DaggerfallUnity.x86_64",
    "Don't Starve": "~/Spiele/dontstarve/start.sh",
    "Exult": "exult",
    "Factorio": "~/Spiele/factorio/bin/x64/factorio",
    "Starbound": "~/Spiele/starbound/start.sh",
    "Stardew Valley": "~/Spiele/stardew/start.sh",
    "OpenMW": "openmw-launcher",
    "Widelands": "widelands",
    "The Ur-Quan Masters": "uqm",
    "Valhalla": "~/Spiele/valhalla/start.sh",
    # Emulators
    "RetroArch": "retroarch",
    "ScummVM": "scummvm",
}

def header():
    print(BACKGROUND_COLOR_BLACK + TEXT_COLOR_MAGENTA + "-" * 50)
    print(BACKGROUND_COLOR_BLACK + TEXT_COLOR_MAGENTA + "{:^50}".format("Game Serpent Wizard 1.0"))
    print("{:^50}".format("by qrzn"))
    print("-" * 50)

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_categories():
    # Function to display available game categories
    clear_screen()
    header()
    print(BACKGROUND_COLOR_BLACK + TEXT_COLOR_MAGENTA + "Choose Thy Categorie:")
    index = 1
    for category in sorted(game_categories.keys()):
        print("{}. {}".format(index, category))
        index += 1
    print()

def display_games(category):
    # Function to display games in a specific category
    clear_screen()
    header()
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
