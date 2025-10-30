student_and_marks={
    'ela':92,
    'fila':78,
    'gila':88,
    'mila':95
}
search=input("Enter the student's name: ")
if search in student_and_marks:
    print(f"{search}'s marks: {student_and_marks[search]}")
else:
    print("Student not found.")
