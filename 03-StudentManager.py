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



