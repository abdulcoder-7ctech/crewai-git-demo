def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hardcoded credentials for demo
    valid_username = "admin"
    valid_password = "secret123"

    if username == valid_username and password == valid_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
