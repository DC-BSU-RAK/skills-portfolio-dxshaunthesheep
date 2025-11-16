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
    def StartQuiz(self, level):
        self.level = level
        self.no_of_questions = 0
        self.score = 0
        self.attempts = 1
        self.clear(except_frame=self.quiz)                      
        self.quiz.config(bg=bgcolor)
        self.quiz.pack(fill="both", expand=True)
        self.askQuestion()

    def askQuestion(self):  # Asks the user a question
        for widget in self.quiz.winfo_children():
            widget.destroy()
            
        self.clear(except_frame=self.quiz)
        self.quiz.config(bg=bgcolor, highlightthickness= 0, bd=0)
        self.quiz.pack(fill="both", expand=True)
        if self.no_of_questions == 10:
            return self.ShowResult()

        self.num1 = RandomNumber(self.level)
        self.num2 = RandomNumber(self.level)
        self.Symb = Symbol()

        # Avoids negative answers
        if self.Symb == '-' and self.num2 > self.num1:
            self.num1, self.num2 = self.num2, self.num1

        #Container for center frame 
        center_frame = tk.Frame(self.quiz, bg=bgcolor)
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        #Label to Track Question Number
        Qtracker = tk.Label(center_frame, text=f"Question {self.no_of_questions + 1} of 10",
                   bg=bgcolor, fg=text_color, font=("Arial", 20))
        Qtracker.pack(pady=(0, 10))


        question = tk.Label(self.quiz, text=f"{self.num1} {self.Symb} {self.num2} ="
                            ,bg=bgcolor, fg=text_color,font=("Arial",24))
        question.pack(pady=20)

        self.box = tk.Entry(self.quiz, bg="#f0f0f0", fg="black", font=("Arial",18),width=10)
        self.box.pack(pady=10)

        #Label to Track Player's Score 
        score_label = tk.Label(center_frame, text=f"Score: {self.score}",
                       bg=bgcolor, fg=text_color, font=("Arial", 20))
        score_label.pack(pady=(0, 10))

        #Submit Button 
        submit = tk.Button(self.quiz, text="Submit", command=self.CheckAnswer, bg="#4CAF50", fg="white"
                           ,font=("Arial",18),width=12, height=2)
        submit.pack(pady=10)

        #Button to Exit mid Quiz 
        exit_btn = tk.Button(center_frame, text="Exit Quiz", command=self.UI,
                     bg="#f44336", fg="white", font=("Arial", 16), width=12, height=2)
        exit_btn.pack(pady=10)

        self.quiz.config(bg=bgcolor, highlightthickness=0, bd=0)

        def CheckAnswer(self):  # Validates player’s answer
            Answer = self.box.get()
        try:
            Answer = int(Answer)
        except:
            messagebox.showwarning("Invalid", "Please enter a number.")
            return

        correctAns = self.num1 + self.num2 if self.Symb == '+' else self.num1 - self.num2

        # If answer is Correct
        if Answer == correctAns:
            if self.attempts == 1:
                self.score += 10
            else:
                self.score += 5

            messagebox.showinfo("Correct", "Well done!")
            self.no_of_questions += 1
            self.attempts = 1
            self.askQuestion()
            return

        # If answer is Wrong
        else:
            if self.attempts == 1:
                self.attempts = 2
                messagebox.showwarning("Nope", "Try again.")
            else:
                messagebox.showerror("Wrong", f"Correct answer was: {correctAns}")
                self.no_of_questions += 1
                self.attempts = 1

            self.askQuestion()
