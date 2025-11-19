import tkinter as tk 
from PIL import Image, ImageTk
import random
root = tk.Tk()

# Load jokes from file
def load_jokes(filename="resources/randomJokes.txt"):
    jokes = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "?" in line:
                    setup, punchline = line.split("?", 1)
                    jokes.append((setup + "?", punchline.strip()))
    except FileNotFoundError:
        jokes = [("Sorry! No jokes have been found. Make sure that randomJokes.txt exists!")]
    return jokes

class Alexa:
    def __init__ (self, root):
        self.root = root
        self.root.title("Jokes Assistant")
        self.jokes = load_jokes()
        self.currentjoke = None

        bg_image = Image.open("background.png")
        self.bg_photo = ImageTk.PhotoImage(bg_image)

root.mainloop()