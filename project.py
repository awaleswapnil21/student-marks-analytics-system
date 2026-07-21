import numpy as np
import os

FILE_NAME = "students.txt"

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def save(self):
        with open(FILE_NAME, "a") as f:
            f.write(f"{self.roll}|{self.name}|{','.join(map(str, self.marks))}\n")

def load_students():
    students = []
    if not os.path.exists(FILE_NAME):
        return students
    with open(FILE_NAME) as f:
        for line in f:
            if line.strip():
                r, n, m = line.strip().split("|")
                students.append(Student(r, n, list(map(int, m.split(",")))))
    return students

def save_all(students):
    with open(FILE_NAME, "w") as f:
        for s in students:
            f.write(f"{s.roll}|{s.name}|{','.join(map(str, s.marks))}\n")

def add_student():
    try:
        roll = input("Roll No: ")
        name = input("Name: ")
        marks = [int(input(f"Subject {i+1} Marks: ")) for i in range(3)]
        Student(roll, name, marks).save()
        print("Student added successfully.")
    except ValueError:
        print("Invalid input.")

def view_students():
    s = load_students()
    if not s: return print("No records found.")
    for st in s:
        print(st.roll, st.name, st.marks)

def search_student():
    roll = input("Enter roll number: ")
    for st in load_students():
        if st.roll == roll:
            print(st.roll, st.name, st.marks)
            return
    print("Student not found.")

def analyze_marks():
    students = load_students()
    if not students: return print("No records.")
    arr = np.array([s.marks for s in students])
    print("Mean:", np.mean(arr))
    print("Max:", np.max(arr))
    print("Min:", np.min(arr))
    print("Std Dev:", np.std(arr))

def apply_grace():
    students = load_students()
    if not students: return print("No records.")
    roll = input("Enter roll number: ")
    try:
        grace = int(input("Enter grace marks: "))
        for s in students:
            if s.roll == roll:
                s.marks = list(np.array(s.marks) + grace)
                save_all(students)
                print("Grace marks applied and saved.")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid input.")

def matrix_operations():
    students = load_students()
    if not students: return print("No records.")
    arr = np.array([s.marks for s in students])
    print("Original Matrix:\n", arr)
    print("Transposed Matrix:\n", arr.T)

def random_students():
    for i in range(1, 6):
        roll = str(np.random.randint(100, 999))
        marks = list(np.random.randint(35, 101, 3))
        Student(roll, f"Student{i}", marks).save()
    print("5 Random students added.")

def student_result():
    students = load_students()
    if not students: return print("No records.")
    arr = np.array([s.marks for s in students])
    avg = np.mean(arr, axis=1)

    print("\nPassed Students:")
    for i, s in enumerate(students):
        if avg[i] >= 40: print(s.name, avg[i])

    print("\nFailed Students:")
    for i, s in enumerate(students):
        if avg[i] < 40: print(s.name, avg[i])

    topper_idx = np.argmax(avg)
    print(f"\nTopper: {students[topper_idx].name} ({avg[topper_idx]:.2f})")

while True:
    print("\n===== Student Performance Analytics =====")
    print("1.Add Student\n2.View Students\n3.Search Student\n4.Analyze Marks")
    print("5.Apply Grace\n6.Matrix Operations\n7.Random Dataset")
    print("8.Student Results\n9.Exit")
    ch = input("Enter choice: ")
    if ch == "1": add_student()
    elif ch == "2": view_students()
    elif ch == "3": search_student()
    elif ch == "4": analyze_marks()
    elif ch == "5": apply_grace()
    elif ch == "6": matrix_operations()
    elif ch == "7": random_students()
    elif ch == "8": student_result()
    elif ch == "9":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
