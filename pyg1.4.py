import os
import json
import subprocess
import time

def print_header():
    with open("header2.txt", 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            print(line)

# Load the JSON file
def load_game_data(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: Game data file not found.")
        exit(1)

def play_sound_effect(sound_file):
    subprocess.run(['play', '-q', sound_file])

def clear_screen():
    os.system('clear')

def display_categories(game_categories):
    clear_screen()
    print("Initializing Game Wizard")
    print("." * 50)
    print("Master, I found the following Categories:\n")
    for index, category in enumerate(game_categories, 1):
        print(f"{index}. {category}")
    print()

def display_games(game_categories, selected_category):
    clear_screen()
    print(f"Looking up Games in the '{selected_category}' Category...")
    print("." * 50)
    print_header()
    print(f"Master, these Games are in the '{selected_category}' Category:\n")
    games = game_categories[selected_category]
    for index, game in enumerate(games, 1):
        print(f"{index}. {game}")
    print()

def launch_game(game_commands, selected_game):
    clear_screen()
    print_header()
    print("=" * 50)
    print(f" -> Launching {selected_game}...\n")
    print(f" -> Have fun! :-)\n")
    print("=" * 50)

    if selected_game in game_commands:
        command = game_commands[selected_game]
        os.system(command)
        clear_screen()
        print_header()
        print(f"I hope you had fun playing {selected_game}!\n")
    else:
        clear_screen()
        print_header()
        print("The Wizard says: There is no command to launch this game!\n")
    input("\nPress Enter to continue...")


def main():
    data = load_game_data("game_data.json")
    game_categories = data.get("categories", {})
    game_commands = data.get("commands", {})

    while True:
        display_categories(game_categories)
        category_choice = input("Choose a Category [1-9] (or 'q' to exit): ")
        if category_choice == "q":
            play_sound_effect('ui_hacking_charenter_01.wav')
            break
        if category_choice.isdigit():
            category_choice = int(category_choice)
            if 1 <= category_choice <= len(game_categories):
                categories = list(game_categories.keys())
                selected_category = categories[category_choice - 1]
                while True:
                    display_games(game_categories, selected_category)
                    game_choice = input("Choose a Game number (or 'b' to go back or 'q' to quit): ")
                    if game_choice == "b":
                        play_sound_effect('ui_hacking_charenter_01.wav')
                        break
                    if game_choice == "q":
                        play_sound_effect('ui_hacking_charenter_01.wav')
                        exit(0)
                    if game_choice.isdigit():
                        game_choice = int(game_choice)
                        games = game_categories.get(selected_category, [])
                        if 1 <= game_choice <= len(games):
                            selected_game = games[game_choice - 1]
                            launch_game(game_commands, selected_game)
                        else:
                            play_sound_effect('ui_hacking_passbad.wav')
                            print("Invalid game selection!")
                            input("Press Enter to continue...")
                    else:
                        play_sound_effect('ui_hacking_passbad.wav')
                        print("Invalid input!")
                        input("Press Enter to continue...")
            else:
                play_sound_effect('ui_hacking_passbad.wav')
                print("Invalid category selection!")
                input("Press Enter to continue...")

if __name__ == "__main__":
    main()
