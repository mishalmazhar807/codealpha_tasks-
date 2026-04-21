stored_username = "admin"
stored_password = "SecurePass@123"

attempts = 3

while attempts > 0:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == stored_username and password == stored_password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print(f"Invalid username or password. Attempts left: {attempts}")

if attempts == 0:
    print("Too many failed attempts. Access denied.")