# multiplication_table.py

number = int(input("Enter a number: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Bonus: Nested loop for tables 1-5
print("\nMultiplication tables for numbers 1 to 5:")
for num in range(1, 6):
    print(f"\nTable for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
