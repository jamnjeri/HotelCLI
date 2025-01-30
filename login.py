import os
def login(user_type):
    print('Login Screen')
    # Generic function to handle login for Administrator, Receptionist, and Restaurant Manager
    # - user_type is passed to determine which menu we are logging into.

    # Get users
    try:
        with open("users.txt", 'r') as file:
            users = file.readlines()
    except FileNotFoundError:
        print("Error: users.txt file not found.")
        return None


    print("""
    *******************************************************
    *              LOGIN MENU                             *
    *******************************************************
    """)

    # Ask for username & password
    # For Guests, we provide specific hints
    if user_type == "Guest":
        username = input("Enter username (Name used during booking): ")
        password = input("Enter password (Room Number): ")
    else:
        # For other roles, we proceed with normal login
        username = input("Enter username: ")
        password = input("Enter password: ")

    # Check if the username and password match any in the users file
    user_found = False  # Flag to track if user is found

    for user in users:
        user_info = user.strip().split(',')

        if len(user_info) == 3:  # Ensure valid format
            stored_username, stored_password, role = user_info
            
            # Check for matching username and password
            if username == stored_username:
                user_found = True  # We found a matching username

                if password == stored_password:  # Check if password matches
                    if role == user_type or (user_type == "Guest" and role == "Guest"):  # If the role matches
                        return role  # Return the role if login is successful
                    else:
                        print(f"Access Denied: This account is not for {user_type}.")
                        return None
                else:
                    print("Incorrect password. Please try again.")
                    return None
    
    # Handle case where username is not found
    if not user_found:
        print(f"Username '{username}' not found. Please check the details.")
    
    return None