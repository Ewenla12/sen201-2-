
"""
Student Management System (Upgraded)
Author: Issachar
Description:
A simple Python-based system for managing student records.
Uses Object-Oriented Programming, file storage, and menu-driven interaction.
"""

import json

class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "course": self.course
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

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        self.students.append(Student(student_id, name, course))
        self.save_students()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        for s in self.students:
            print(f"ID: {s.student_id}, Name: {s.name}, Course: {s.course}")

    def remove_student(self):
        student_id = input("Enter Student ID to remove: ")
        self.students = [s for s in self.students if s.student_id != student_id]
        self.save_students()
        print("Student removed successfully.")

    def menu(self):
        while True:
            print("\n1. Add Student")
            print("2. View Students")
            print("3. Remove Student")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.remove_student()
            elif choice == "4":
                print("Exiting program.")
                break
            else:
                print("Invalid option.")


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()
