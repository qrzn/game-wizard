import json
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)

# Dictionary to hold game categories and their associated games
game_categories = {
    "FAVS": [
        "Zeus",
        "Arcanum",
        "Daggerfall Unity",
        "Stardew Valley",
        "Master of Orion",
        "OpenMW",
        "Emperor",
        "Pharaoh",
        "Return to the Roots",
        ],
    "RPG": [
        "Albion",
        "The Elder Scrolls - Arena",
        "Arcanum",
        "Daggerfall",
        "Daggerfall Unity",
        "Darklands",
        "Dune",
        "Lands of Lore",
        "Diablo II",
        "Ultima VII",
        "Ultima VI",
        "Ultima VIII",
        "Ultima IX",
        "Fallout",
        "Fallout 2",
        "Fallout New Vegas",
        "OpenMW",
        "Ultima Underworld",
        "Ultima Underworld 2",
        ],
    "Strategy": [
        "Anno 1404",
        "Anno 1503",
        "Anno 1701",
        "Centurion",
        "Dungeon Keeper II",
        "Factorio",
        "Dune 2",
        "Emperor",
        "Return to the Roots",
        "Siedler 2",
        "Stronghold",
        "Stronghold Crusader",
        "Stronghold Crusader Extreme",
        "Tropico",
        "OpenXcom",
        "Pharaoh",
        "War Wind",
        "Weltwunder",
        "Zeus",
        ],
    "Adventure": [
        "Shadow of the Comet",
        "Broken Sword",
        "Broken Sword II",
        "ScummVM",
        ],
     "4X": [
        "Alien Crossfire",
        "Ascendancy",
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
}

# Dictionary to hold game commands
game_commands = {
    # DOS, games that run in dosbox
    "Albion": "dosbox -conf ~/.dosbox/albion.conf",
    "Arena": "dosbox -conf ~/.dosbox/arena.conf",
    "Caesar II": "dosbox -conf ~/.dosbox/caesar2.conf",
    "Caster of Magic": "dosbox -conf ~/.dosbox/com.conf",
    "Commander Keen": "dosbox -conf ~/.dosbox/keen.conf",
    "Daggerfall": "dosbox -conf ~/.dosbox/fall.conf",
    "Dune": "dosbox -conf ~/.dosbox/dune.conf",
    "Dune 2": "dosbox -conf ~/.dosbox/dune2.conf",
    "Darklands": "dosbox -conf ~/.dosbox/darklands.conf",
    "Gods": "dosbox -conf ~/.dosbox/gods.conf",
    "Dune 2": "dosbox -conf ~/.dosbox/dune2.conf",
    "Lands of Lore": "dosbox -conf ~/.dosbox/lol.conf",
    "Siedler 2": "dosbox -conf ~/.dosbox/siedler2.conf",
    "Master of Orion": "dosbox -conf ~/.dosbox/moo.conf",
    "Master of Orion 2": "dosbox -conf ~/.dosbox/moo2.conf",
    "Master of Magic": "dosbox -conf ~/.dosbox/mom.conf",
    "Pirates!": "dosbox -conf ~/.dosbox/pirates.conf",
    "Ultima Underworld": "dosbox -conf ~/.dosbox/uuw.conf",
    "Shadow of the Comet": "dosbox -conf ~/.dosbox/shadow.conf",
    "Quake": "dosbox -conf ~/.dosbox/quake.conf",
    "Veil of Darkness": "dosbox -conf ~/.dosbox/veil.conf",

    # games that run through wine
    "Age of Mythology": "cd ~/Games/aomee/ && wine aomx.exe",
    "Alien Crossfire": "cd ~/Games/smacx/ && wine terranx.exe",
    "Anno 1404": "cd ~/Games/anno1404/ && wine Addon.exe",
    "Anno 1503": "cd ~/Games/anno1503/ && wine 1503Startup.exe",
    "Anno 1701": "cd ~/Games/anno1701/ && wine Anno1701AddOn.exe",
    "Arcanum": "cd ~/Games/arcanum/ && wine Arcanum.exe",
    "Black & White": "cd ~/Games/blackwhite/ && wine white.exe",
    "Emperor": "cd ~/Games/emperor/ && wine Emperor.exe",
    "Diablo II": "cd ~/Games/diablo2/ && wine Game.exe",
    "Fallout": "cd ~/Games/fallout/ && wine FALLOUTW.exe",
    "Fallout 2": "cd ~/Games/fallout2/ && wine fallout2.exe",
    "Fallout New Vegas": "cd ~/Games/fnv/ && wine nvse_loader.exe",
    "Dungeon Keeper II": "cd ~/Games/dk2/ && wine DKII-DX.exe",
    "Galactic Civilizations II": "cd ~/Games/galciv2/ && wine Game.exe",
    "Stronghold": "cd ~/Games/stronghold/ && wine Stronghold.exe",
    "Stronghold Crusader": "cd ~/Games/strongholdchd/ && wine shc.exe",
    "Stronghold Crusader Extreme": "cd ~/Games/strongholdchd/ && wine shc.exe",
    "Tropico": "cd ~/Games/tropico/ && wine Tropico.exe",
    "Pharaoh": "cd ~/Games/pharaoh/ && wine Pharaoh.exe",
    "Sid Meier's Pirates!": "cd ~/Games/smpirates/ && wine Pirates!.exe",
    "War Wind": "cd ~/Games/warwind/ && wine WW.exe",
    "Weltwunder": "cd ~/Games/c4/ && wine Game.exe",
    "Zeus": "cd ~/Games/zeus/ && wine Zeus.exe",

    # games that run natively on linux
    "Daggerfall Unity": "~/Games/dfu/DaggerfallUnity.x86_64",
    "Don't Starve": "~/Games/dontstarve/start.sh",
    "Egypt - Old Kingdom": "~/Games/egypt/start.sh",
    "Ultima VII": "exult",
    "Ultima VIII": "scummvm ultima8",
    "Ultima VI": "dosbox -conf ~/.dosbox/ultima6.conf",
    "Factorio": "~/Games/factorio/bin/x64/factorio",
    "Return to the Roots": "sh ~/Games/rttr/bin/rttr.sh",
    "Starbound": "~/Games/starbound/start.sh",
    "Stardew Valley": "~/Games/stardew/start.sh",
    "OpenMW": "openmw-launcher",
    "Widelands": "widelands",
    "OpenXcom": "openxcom",
    "The Ur-Quan Masters": "uqm",
    "Valhalla": "~/Games/valhalla/start.sh",

    # Emulators
    "RetroArch": "retroarch",
    "ScummVM": "scummvm",
    "Dosbox": "dosbox",
    "Steam": "steam",
    
    # games that run through steam
    "Amnesia - The Dark Descent": "steam steam://rungameid/57300",
    "Amnesia - A Machine for Pigs": "steam steam://rungameid/239200",
    "Stellaris": "steam steam://rungameid/281990",
    "Civilization V": "steam steam://rungameid/8930",
    "Civilization VI": "steam steam://rungameid/289070",
    "Dawn of War": "steam steam://rungameid/9450",
    "Earth 2160": "steam steam://rungameid/1900",
    "Lost Ruins": "steam steam://rungameid/1306630",
    "Apotheon": "steam steam://rungameid/208750",
    "Gravity Circuit": "steam steam://rungameid/858710",
    "Kerbal Space Program": "steam steam://rungameid/281990",
    "X3 - Terran Conflict": "steam steam://rungameid/2820",
    "Dawn of War": "steam steam://rungameid/9450",
    "XCOM 2": "steam steam://rungameid/268500",
    "CrossCode": "steam steam://rungameid/368340",
    "Terraria": "steam steam://rungameid/105600",
    "Sakura Dungeon": "steam steam://rungameid/407330",
    "Legend of Grimrock": "steam steam://rungameid/207170",
}

# Creating a dictionary to hold both categories and commands
data = {
    "categories": game_categories,
    "commands": game_commands
}

# Writing the dictionary to a JSON file
with open("game_data.json", "w") as file:
    json.dump(data, file)
clear_screen()
print("gmsdata.py - game data tool for pygames - © 2025 qrzn")
print_with_delay("✅ Game Data JSON file generated successfully.")
