name = input("Enter your name: ")
score = int(input("Enter your score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

print("\nStudent:", name)
print("Score:", score)
print("Grade:", grade)
