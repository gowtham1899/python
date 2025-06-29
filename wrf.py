import csv
import json

# 1. Text File
with open("data.txt", "w") as f:
    f.write("name:John, age:30\n")

with open("data.txt", "r") as f:
    for line in f:
        parts = line.strip().split(", ")
        data = dict(p.split(":") for p in parts)
        print("Text Parsed:", data)

# 2. CSV File
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("CSV Row:", row)

# 3. JSON File
person = {"name": "Bob", "age": 28}

with open("data.json", "w") as f:
    json.dump(person, f)

with open("data.json", "r") as f:
    data = json.load(f)
    print("JSON Data:", data)
