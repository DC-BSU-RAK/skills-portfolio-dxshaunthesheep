import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

root = tk.Tk()
root.title("Student Marks Manager")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

def load_studentdata(filename="studentMarks.txt"):
    students=[]
    try:
        with open(filename, "r") as f:
            num_of_students = int(f.readline().strip())
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 6:
                    student_ID = int(parts[0])
                    student_Name = parts[1]
                    course = list(map(int, parts[2:5]))
                    exam = int(parts[5])
                    total_coursework = sum(course)
                    overall = total_coursework + exam
                    percentage = (overall / 160) * 100
                    grade = calculate_grade(percentage)
                    students.append({
                        "id": student_ID,
                        "name": student_Name,
                        "coursework": total_coursework,
                        "exam": exam,
                        "overall": overall,
                        "percentage": percentage,
                        "grade": grade
                    })
        return students, num_of_students
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {filename} not found.")
        return [], 0

def calculate_grade(percentage):
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
    return (f"Name: {student['name']}\n"
            f"ID: {student['id']}\n"
            f"Coursework Total: {student['coursework']}\n"
            f"Exam Mark: {student['exam']}\n"
            f"Overall %: {student['percentage']:.2f}\n"
            f"Grade: {student['grade']}\n")

def view_all_students():
    output.delete("1.0", tk.END)
    total_percentage = 0
    for student in students:
        output.insert(tk.END, format_student(student) + "\n")
        total_percentage += student["percentage"]
    avg_percentage = total_percentage / len(students) if students else 0
    output.insert(tk.END, f"\nSummary:\nNumber of students: {len(students)}\n"
                          f"Average Percentage: {avg_percentage:.2f}%\n")
def view_individual_student():
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
    if not students:
        return
    highest = max(students, key=lambda s: s["overall"])
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Highest Scoring Student:\n\n" + format_student(highest))

def show_lowest_student():
    if not students:
        return
    lowest = min(students, key=lambda s: s["overall"])
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Lowest Scoring Student:\n\n" + format_student(lowest))

    students, num_students = load_studentdata()

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

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_all = tk.Button(button_frame, text="View All Records", width=20, command=view_all_students)
btn_individual = tk.Button(button_frame, text="View Individual Record", width=20, command=view_individual_student)
btn_highest = tk.Button(button_frame, text="Highest Score", width=20, command=show_highest_student)
btn_lowest = tk.Button(button_frame, text="Lowest Score", width=20, command=show_lowest_student)

btn_all.grid(row=0, column=0, padx=5, pady=5)
btn_individual.grid(row=0, column=1, padx=5, pady=5)
btn_highest.grid(row=0, column=2, padx=5, pady=5)
btn_lowest.grid(row=0, column=3, padx=5, pady=5)

output = tk.Text(root, width=60, height=25)
output.pack(padx=10, pady=10)

root.mainloop()

