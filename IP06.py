#PWD MANAGER

import os

# File to store passwords
PASSWORD_FILE = "passwords.txt"

def add_password():
    #Add a new password
    account = input("Enter the account name: ")
    password = input("Enter the password: ")

    with open(PASSWORD_FILE, 'a') as file:
        file.write(f"{account}: {password}\n")
    print(f"Password for '{account}' added successfully.")

def view_passwords():
    #View all stored passwords
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            passwords = file.readlines()

        if not passwords:
            print("No passwords stored.")
        else:
            print("\nStored Passwords:")
            for line in passwords:
                print(line.strip())
    else:
        print("No passwords stored.")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            print("Exiting the Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
