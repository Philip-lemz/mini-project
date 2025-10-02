name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 0 <= age <= 12:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teen"
elif 20 <= age <= 59:
    category = "Adult"
else:
    category = "Senior"

print("\nName:", name)
print("Age:", age)
print("Category:", category)
