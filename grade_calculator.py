def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [95, 82, 67, 74, 89]

for i in range(len(students)):
    student = students[i]
    mark = marks[i]
    grade = calculate_grade(mark)
    print(f"{student}: {mark} - Grade {grade}")
