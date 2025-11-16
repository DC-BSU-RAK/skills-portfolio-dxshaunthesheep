from tkinter import messagebox
import random
import tkinter as tk

root = tk.Tk()
root.geometry("1200x700")

bgcolor = "#800080" #Variable for Background Color
text_color = "white"  #Variable for text color


def RandomNumber(level):  # Chooses Difficulty 
    return random.randint(*({'Easy': (1, 9), 'Medium': (10, 99), 'Hard': (1000, 9999)}[level]))

def Symbol():  # Randomises Arithmetic Operator 
    return random.choice(['+', '-'])

class MathQuiz:  # OOP for Quiz 
    def __init__(self, root):
        self.root = root
        self.level = None
        self.no_of_questions = 0
        self.score = 0
        self.attempts = 1

        self.menu = tk.Frame(root)
        self.quiz = tk.Frame(root)
        self.result = tk.Frame(root)

        self.UI()

    #Menu UI
    def UI(self):
        self.clear()
        self.menu.pack(fill="both", expand=True)

        center_frame = tk.Frame(self.menu, bg=bgcolor)
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(self.menu, text="Choose a difficulty mode!", bg=bgcolor, fg=text_color,font=("Arial",24)).pack(pady=10)
        for lvl in ["Easy", "Medium", "Hard"]:
            tk.Button(self.menu, text=lvl.title(),
                      command=lambda L=lvl: self.StartQuiz(L), bg="#4CAF50", fg="white", font=("Arial",18), width=12, height=2).pack(pady=5)
