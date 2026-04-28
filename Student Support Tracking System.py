# Student Support Tracking System
import tkinter as tk
from tkinter import messagebox

#class stores individual student info
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

        # each student can have multiple visits stored in a list
        self.visits = []

    def add_visit(self, visit):
        # just appends a new visit object to the list
        self.visits.append(visit)
# This class represents a single visit/session
class Visit:
    def __init__(self, date, reason):
        self.date = date
        self.reason = reason

# Main system class that holds all students
class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
    
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
# GUI PART
class App:
    def __init__(self, root):
        self.system = StudentSystem()

        self.root = root
        self.root.title("Student Support Tracker")

        # --- Student inputs ---
        tk.Label(root, text="Student ID").grid(row=0, column=0)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1)

        tk.Label(root, text="Student Name").grid(row=1, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1)

        tk.Button(root, text="Add Student", command=self.add_student).grid(row=2, column=0, columnspan=2)

        #Visit inputs
        tk.Label(root, text="Visit Date").grid(row=3, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=3, column=1)

        tk.Label(root, text="Reason").grid(row=4, column=0)
        self.reason_entry = tk.Entry(root)
        self.reason_entry.grid(row=4, column=1)

        tk.Button(root, text="Log Visit", command=self.log_visit).grid(row=5, column=0, columnspan=2)

        # output box to show results
        self.output = tk.Text(root, height=10, width=40)
        self.output.grid(row=6, column=0, columnspan=2)

        tk.Button(root, text="View Students", command=self.view_students).grid(row=7, column=0, columnspan=2)

    # Add a student to the system
    def add_student(self):
        student_id = self.id_entry.get()
        name = self.name_entry.get()

        # basic validation so empty values don't break things
        if student_id == "" or name == "":
            messagebox.showerror("Error", "Please fill out both fields")
            return

        new_student = Student(student_id, name)
        self.system.add_student(new_student)

        messagebox.showinfo("Success", "Student added")

        # clear inputs after adding
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
    # Log a visit for a student
    def log_visit(self):
        student_id = self.id_entry.get()
        date = self.date_entry.get()
        reason = self.reason_entry.get()

        student = self.system.find_student(student_id)

        if student is None:
            messagebox.showerror("Error", "Student not found")
            return

        new_visit = Visit(date, reason)
        student.add_visit(new_visit)

        messagebox.showinfo("Success", "Visit logged")

        # clear visit fields
        self.date_entry.delete(0, tk.END)
        self.reason_entry.delete(0, tk.END)

    def view_students(self):
        self.output.delete("1.0", tk.END)

        # loop through everything and print it nicely
        for student in self.system.students:
            self.output.insert(tk.END, f"ID: {student.student_id} | Name: {student.name}\n")

            if len(student.visits) == 0:
                self.output.insert(tk.END, "  No visits yet\n")

            for visit in student.visits:
                self.output.insert(tk.END, f"  - {visit.date} : {visit.reason}\n")

            self.output.insert(tk.END, "\n")
# RUN THE PROGRAM
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()