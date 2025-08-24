# Assigment 4 Task 2: Write and Append Data to a File

user_text = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_text + "\n")   # Writing user input with newline

print("Data written to output.txt")

append_text = input("Enter some text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(append_text + "\n")  # Appending new data

print("Data appended to output.txt")