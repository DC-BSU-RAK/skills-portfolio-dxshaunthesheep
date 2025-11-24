import tkinter as tk
from tkinter import messagebox, simpledialog

def load_student_data(filename="studentMarks.txt"):
    """
    Pulls all the student info out of the text file.
    First line tells us how many students there are.
    Each line after that has: ID, name, 3 coursework marks, and an exam mark.
    """
    students = []
    try:
        with open(filename, "r") as f:
            num_students = int(f.readline().strip())  # grab the class size
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 6:  # make sure the line looks right
                    student_id = int(parts[0])
                    name = parts[1]
                    coursework = list(map(int, parts[2:5]))  # three coursework marks
                    exam = int(parts[5])
                    total_coursework = sum(coursework)
                    overall = total_coursework + exam
                    percentage = (overall / 160) * 100  # total possible points = 160
                    grade = calculate_grade(percentage)
                    # stash everything neatly in a dictionary
                    students.append({
                        "id": student_id,
                        "name": name,
                        "coursework": total_coursework,
                        "exam": exam,
                        "overall": overall,
                        "percentage": percentage,
                        "grade": grade
                    })
        return students, num_students
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {filename} not found.")
        return [], 0

def calculate_grade(percentage):
    """Turns a percentage into a letter grade, the classic A–F scale."""
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def format_student(student):
    """Takes a student’s data and makes it look nice for display."""
    return (f"Name: {student['name']}\n"
            f"ID: {student['id']}\n"
            f"Coursework Total: {student['coursework']}\n"
            f"Exam Mark: {student['exam']}\n"
            f"Overall %: {student['percentage']:.2f}\n"
            f"Grade: {student['grade']}\n")

#Button Functions
def view_all_students():
    """Show every student’s record plus a summary at the end."""
    output.delete("1.0", tk.END)  # clear the text box first
    total_percentage = 0
    for student in students:
        output.insert(tk.END, format_student(student) + "\n")
        total_percentage += student["percentage"]
    avg_percentage = total_percentage / len(students) if students else 0
    output.insert(tk.END, f"\nSummary:\nNumber of students: {len(students)}\n"
                          f"Average Percentage: {avg_percentage:.2f}%\n")

def view_individual_student():
    """Ask the user for a name or ID, then show just that student’s record."""
    query = simpledialog.askstring("Search Student", "Enter student name or ID:")
    if not query:
        return
    output.delete("1.0", tk.END)
    found = False
    for student in students:
        if query.lower() in student["name"].lower() or query == str(student["id"]):
            output.insert(tk.END, format_student(student))
            found = True
            break
    if not found:
        messagebox.showinfo("Not Found", "Student record not found.")

def show_highest_student():
    """Find the top scorer and show their details."""
    if not students:
        return
    highest = max(students, key=lambda s: s["overall"])
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Highest Scoring Student:\n\n" + format_student(highest))

def show_lowest_student():
    """Find the lowest scorer and show their details."""
    if not students:
        return
    lowest = min(students, key=lambda s: s["overall"])
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Lowest Scoring Student:\n\n" + format_student(lowest))


root = tk.Tk()
root.title("Student Marks Manager")

# Load up the student data from the file
students, num_students = load_student_data()

#  Menu Bar (classic dropdown style) 
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

student_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=student_menu)
student_menu.add_command(label="View All Records", command=view_all_students)
student_menu.add_command(label="View Individual Record", command=view_individual_student)
student_menu.add_command(label="Show Highest Score", command=show_highest_student)
student_menu.add_command(label="Show Lowest Score", command=show_lowest_student)
student_menu.add_separator()
student_menu.add_command(label="Exit", command=root.quit)

#Button Panel (quick access buttons)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_all = tk.Button(button_frame, text="View All Records", width=20, command=view_all_students)
btn_individual = tk.Button(button_frame, text="View Individual Record", width=20, command=view_individual_student)
btn_highest = tk.Button(button_frame, text="Highest Score", width=20, command=show_highest_student)
btn_lowest = tk.Button(button_frame, text="Lowest Score", width=20, command=show_lowest_student)

# Lay out the buttons side by side
btn_all.grid(row=0, column=0, padx=5, pady=5)
btn_individual.grid(row=0, column=1, padx=5, pady=5)
btn_highest.grid(row=0, column=2, padx=5, pady=5)
btn_lowest.grid(row=0, column=3, padx=5, pady=5)

#Output Area
output = tk.Text(root, width=70, height=25)
output.pack(padx=10, pady=10)

# Fire up the app
root.mainloop()