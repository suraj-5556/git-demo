import csv
import random

# Controlled bad values
bad_ages = ["-1", "0", "abc", "", None]
bad_marks = ["-10", "200", "xyz", "", None]

names = [
    "Suraj", "Rahul", "Mira", "Tom", "Isha", "Karan", "Neha", "Amit",
    "Ravi", "Diya", "Pooja", "Sam", "Tina", "Vivek", "Ronit", "Ira"
]

def generate_row():
    name = random.choice(names)

    # 70% chance valid, 30% invalid
    if random.random() < 0.7:
        age = str(random.randint(15, 30))
    else:
        age = random.choice(bad_ages)

    if random.random() < 0.7:
        marks = str(random.randint(0, 100))
    else:
        marks = random.choice(bad_marks)

    return [name, age, marks]


# Create CSV
with open("data/students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "marks"])

    for _ in range(100):
        writer.writerow(generate_row())

print("students.csv generated with 100 mixed-quality rows.")
