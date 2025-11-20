import tkinter as tk
from PIL import Image, ImageTk
import random

# Load jokes from the .txt file
def load_jokes(filename="randomJokes.txt"):
    jokes = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "?" in line:
                    setup, punchline = line.split("?", 1)
                    jokes.append((setup + "?", punchline.strip()))
    except FileNotFoundError: 
        jokes = [("Sorry! No jokes found.", "Make sure randomJokes.txt exists!")]
    return jokes #Outputs message incase file was not found in directory. 

class Alexa: #OOP class for Joke Assistant
    def __init__(self, root):
        self.root = root
        self.root.title("Jokes Assistant")
        self.jokes = load_jokes()
        self.current_joke = None

       #Loads the background image 
        self.original_bg = Image.open("background.png")
        self.bg_photo = ImageTk.PhotoImage(self.original_bg)

        # Creates a canvas for the background 
        self.canvas = tk.Canvas(root, width=self.bg_photo.width(), height=self.bg_photo.height())
        self.canvas.pack(fill="both", expand=True)
        self.bg_image_id = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")


        # Labels to store the punchline button and the setup button 
        self.setup_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center", bg="white")
        self.punchline_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=400, justify="center", bg="white")

        # Buttons for Alexa
        self.tell_button = tk.Button(root, text="Alexa tell me a Joke", command=self.show_setup, width=25, height=2)
        self.punchline_button = tk.Button(root, text="Show Punchline", command=self.show_punchline, width=25, height=2)
        self.next_button = tk.Button(root, text="Tell me another joke", command=self.show_setup, width=25, height=2)
        self.quit_button = tk.Button(root, text="Quit", command=root.quit, width=25, height=2)

        # Place widgets on canvas
        self.canvas.create_window(250, 100, window=self.setup_label)
        self.canvas.create_window(250, 150, window=self.punchline_label)
        self.canvas.create_window(250, 220, window=self.tell_button)
        self.canvas.create_window(250, 270, window=self.punchline_button)
        self.canvas.create_window(250, 320, window=self.next_button)
        self.canvas.create_window(250, 370, window=self.quit_button)

    def show_setup(self):
        self.current_joke = random.choice(self.jokes)
        self.setup_label.config(text=self.current_joke[0])
        self.punchline_label.config(text="")

    def show_punchline(self):
        if self.current_joke:
            self.punchline_label.config(text=self.current_joke[1])

    def resize_background(self, event):
        if event.widget == self.root:
            new_width = event.width
            new_height = event.height
            resized = self.original_bg.resize((new_width, new_height))
            self.bg_photo = ImageTk.PhotoImage(resized)
            self.canvas.config(width=new_width, height=new_height)
            self.canvas.itemconfig(self.bg_image_id, image=self.bg_photo)

# Start Alexa the Joke Assistant 
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False) #Makes the window not resiazble
    root.geometry("500x450")  
    app = Alexa(root)
    root.mainloop()