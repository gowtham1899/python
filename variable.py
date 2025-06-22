# Variable
correct_password = "python123"
attempts = 0

# Loop with condition
while attempts < 3:
    # Get user input
    password = input("Enter your password: ")

    # Conditional check
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password.")
        attempts += 1

# After 3 failed attempts
if attempts == 3:
    print("Access denied. Too many attempts.")
