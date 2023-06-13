import tkinter as tk
from PIL import Image, ImageTk
import os

class GameLauncher(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.game_label = tk.Label(self, text="Select a game to launch:")
        self.game_label.pack(side="top")

        self.category_label = tk.Label(self, text="Select a category:")
        self.category_label.pack(side="top")

        self.category_listbox = tk.Listbox(self)
        self.category_listbox.pack(side="left", fill="y")

        self.game_listbox = tk.Listbox(self)
        self.game_listbox.pack(side="left", fill="y")

        self.games_by_category = self.generate_categories()

        for category in self.games_by_category.keys():
            self.category_listbox.insert(tk.END, category)

        self.category_listbox.bind("<<ListboxSelect>>", self.update_game_list)

        self.thumbnail_label = tk.Label(self)
        self.thumbnail_label.pack(side="top")

        self.launch_button = tk.Button(self, text="Launch Game", command=self.launch_game)
        self.launch_button.pack(side="bottom")

    def generate_categories(self):
        games_by_category = {}

        games_data = {
            "Game 1": {"Category": "Category 1", "Thumbnail": "path/to/game1_thumbnail.png"},
            "Game 2": {"Category": "Category 2", "Thumbnail": "path/to/game2_thumbnail.png"},
            "Game 3": {"Category": "Category 1", "Thumbnail": "path/to/game3_thumbnail.png"},
            "Game 4": {"Category": "Category 2", "Thumbnail": "path/to/game4_thumbnail.png"},
        }

        for game, game_data in games_data.items():
            category = game_data["Category"]
            thumbnail_path = game_data["Thumbnail"]

            if category in games_by_category:
                games_by_category[category].append({"Game": game, "Thumbnail": thumbnail_path})
            else:
                games_by_category[category] = [{"Game": game, "Thumbnail": thumbnail_path}]

        return games_by_category

    def update_game_list(self, event):
        selected_category = self.category_listbox.get(tk.ACTIVE)
        self.game_listbox.delete(0, tk.END)
        self.thumbnail_label.configure(image="")  # Clear previous thumbnail

        if selected_category in self.games_by_category:
            games = self.games_by_category[selected_category]
            games.sort(key=lambda x: x["Game"])  # Sort the games alphabetically

            for game_data in games:
                game = game_data["Game"]
                self.game_listbox.insert(tk.END, game)

    def load_thumbnail(self, thumbnail_path):
        thumbnail = Image.open(thumbnail_path)
        thumbnail = thumbnail.resize((100, 100))  # Resize the thumbnail as desired
        thumbnail = ImageTk.PhotoImage(thumbnail)
        self.thumbnail_label.configure(image=thumbnail)
        self.thumbnail_label.image = thumbnail

    def launch_game(self):
        selected_game = self.game_listbox.get(tk.ACTIVE)
        if selected_game == "Game 1":
            os.system("path/to/game1.exe")
        elif selected_game == "Game 2":
            os.system("path/to/game2.exe")
        elif selected_game == "Game 3":
            os.system("path/to/game3.exe")
        elif selected_game == "Game 4":
            os.system("path/to/game4.exe")

        thumbnail_path = self.get_thumbnail_path(selected_game)
        self.load_thumbnail(thumbnail_path)

    def get_thumbnail_path(self, game):
        for category_games in self.games_by_category.values():
            for game_data in category_games:
                if game_data["Game"] == game:
                    return game_data["Thumbnail"]
        return ""

root = tk.Tk()
root.geometry("400x400")  # Set the initial size of the GUI (width x height)
launcher = GameLauncher(master=root)
launcher.pack(fill="both", expand=True)
launcher.mainloop()

