import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

root = tk.Tk()
root.title("Student Marks Manager")

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




