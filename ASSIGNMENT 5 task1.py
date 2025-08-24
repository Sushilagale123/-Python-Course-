# ASSIGNMENT 5 Task 1: Create a Dictionary of Student Marks

student_marks = {
    "Sunil": 85,
    "Anil": 78,
    "Radhika": 92,
    "Sumit": 67,
    "Sushil":90
}

name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Sorry, no record found for '{name}'.")