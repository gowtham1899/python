import csv
import json
import logging

# ---------- Setup Logging ----------
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------- 1. Text File ----------
try:
    with open("data.txt", "w") as f:
        f.write("name:John, age:30\n")
        f.write("name:Jane, age:25\n")
    logging.info("Wrote to data.txt successfully")

    with open("data.txt", "r") as f:
        for line in f:
            parts = line.strip().split(", ")
            data = dict(p.split(":") for p in parts)
            print("Text Parsed:", data)

except Exception as e:
    logging.error("Error handling text file: %s", e)
    print("❌ Error in text file section")

# ---------- 2. CSV File ----------
try:
    with open("data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", 25])
        writer.writerow(["Bob", 28])
    logging.info("Wrote to data.csv successfully")

    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("CSV Row:", row)

except Exception as e:
    logging.error("Error handling CSV file: %s", e)
    print("❌ Error in CSV file section")

# ---------- 3. JSON File ----------
try:
    person = {"name": "Charlie", "age": 35}

    with open("data.json", "w") as f:
        json.dump(person, f)
    logging.info("Wrote to data.json successfully")

    with open("data.json", "r") as f:
        data = json.load(f)
        print("JSON Data:", data)

except Exception as e:
    logging.error("Error handling JSON file: %s", e)
    print("❌ Error in JSON file section")

# ---------- 4. User Input with Exception ----------
try:
    number = int(input("\nEnter a number to divide 100 by: "))
    result = 100 / number
    print("✅ Result:", result)
except ValueError:
    logging.error("Invalid input: not a number")
    print("❌ Please enter a valid number.")
except ZeroDivisionError:
    logging.error("Division by zero")
    print("❌ Cannot divide by zero.")
except Exception as e:
    logging.error("Unknown error in division: %s", e)
    print("❌ An error occurred.")
finally:
    print("📌 Program finished.")
