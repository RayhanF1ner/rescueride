import random

# Stores user accounts (username: password)
users = {}

# List of landmarks
landmarks = [
    "Central Park",
    "City Museum",
    "Sunset Beach",
    "Liberty Monument",
    "Green Hill Park"
]


def register():
    print("\n=== REGISTER ===")
    username = input("Create a username: ")

    if username in users:
        print("Username already exists!")
        return

    password = input("Create a password: ")
    users[username] = password

    print("Registration successful!")


def login():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print(f"\nWelcome, {username}!")
        main_menu()
    else:
        print("Invalid username or password.")


def check_nearby_landmark():
    place = random.choice(landmarks)
    print("\nNearby Landmark:")
    print(place)


def get_help():
    place = random.choice(landmarks)
    print("\nHelp is on the way!")
    print(f"Emergency team will arrive at {place}.")


def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Check Nearby Landmark")
        print("2. Get Help")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_nearby_landmark()

        elif choice == "2":
            get_help()

        elif choice == "3":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice.")


# Main Program
while True:
    print("\n===== LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")