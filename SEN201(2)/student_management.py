"""
Student Management System
Author: Issachar
Description:
A Python-based system for managing student records.
Auto matric generation, search, file storage, and duplicate prevention.
"""

import json

class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "department": self.department
        }

class StudentManagementSystem:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    self.students.append(Student(**item))
        except FileNotFoundError:
            self.students = []

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump([s.to_dict() for s in self.students], file, indent=4)

    def generate_matric(self):
        if not self.students:
            return "25/1000"
        last = max(int(s.student_id.split("/")[1]) for s in self.students)
        return f"25/{last + 1}"

    def add_student(self):
        name = input("Enter Student Name: ")
        department = input("Enter Department: ")
        matric = self.generate_matric()

        self.students.append(Student(matric, name, department))
        self.save_students()
        print(f"Student added successfully with Matric No: {matric}")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        for s in self.students:
            print(f"{s.student_id} | {s.name} | {s.department}")

    def search_student(self):
        matric = input("Enter Matric Number: ")
        for s in self.students:
            if s.student_id == matric:
                print(f"FOUND → {s.student_id} | {s.name} | {s.department}")
                return
        print("Student not found.")

    def remove_student(self):
        matric = input("Enter Matric Number to remove: ")
        self.students = [s for s in self.students if s.student_id != matric]
        self.save_students()
        print("Student removed successfully.")

    def menu(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Remove Student")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.remove_student()
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()
