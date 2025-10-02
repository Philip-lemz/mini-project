# Student Marks Analyzer

student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
student_marks = [85, 92, 78, 88, 95]

# Calculate average marks
average_marks = sum(student_marks) / len(student_marks)

# Assign grades
grades = []
for mark in student_marks:
    if mark >= 90:
        grades.append("A")
    elif mark >= 80:
        grades.append("B")
    elif mark >= 70:
        grades.append("C")
    elif mark >= 60:
        grades.append("D")
    else:
        grades.append("F")

# Print summary table
for i in range(len(student_names)):
    print(f"{student_names[i]}: {student_marks[i]} - Grade {grades[i]}")

# Print average marks
print(f"Average marks: {average_marks}")
