# For administrator-specific tasks
import os

def read_rooms_data():
    try:
        with open("rooms.txt", 'r') as file:
            # Skip the comment line and read only room data
            room_data = [
                line.strip().split(',')
                for line in file.readlines() if not line.startswith('#')
            ]
        return room_data
    except FileNotFoundError:
        print("Error: rooms.txt file not found.")
        return []

# Function to extract unique room types from the rooms data
def get_existing_room_types():
    room_types = set()  # Using a set to avoid duplicates
    try:
        with open("rooms.txt", 'r') as file:
            # Skip the first line (comment)
            next(file)
            for line in file:
                # Extract room type from each line
                room_info = line.strip().split(',')
                if len(room_info) == 4:
                    room_type = room_info[1]  # Assuming room type is at index 1
                    room_types.add(room_type)  # Add to set to ensure uniqueness
    except FileNotFoundError:
        print("Error: rooms.txt file not found.")
        return []
    
    # Convert the set to a sorted list (if needed, for display in order)
    return sorted(list(room_types))

# Function to get a unique room number for the selected room type
def get_unique_room_number(room_type, existing_room_numbers):
    while True:
        room_number = input(f"Enter the room number for the {room_type} room: ")
        if not room_number.isdigit():
            print("Error: Room number must be a valid number.")
            continue
        room_number = room_type[0].upper() + room_number  # Add prefix based on room type
        if room_number in existing_room_numbers:
            print("Error: Room number already exists. Please enter a unique room number.")
        else:
            return room_number
        

# Function to extract the prefix (alphabet part) of the room type
def get_room_prefix(room_type):
    prefix = ''.join([char for char in room_type if char.isalpha()])  # Extracts alphabetic characters
    return prefix


# Function to add a new room (simplified version)
def add_room():
    existing_room_types = get_existing_room_types()
    
    # Display dynamic room types menu
    print("""
    *******************************************************
    *               Room Types Menu                       *
    *******************************************************
    """)
    
    for idx, room_type in enumerate(existing_room_types, 1):
        print(f"{idx}. {room_type}")
    
    # Option for custom room type and exit option
    print(f"{len(existing_room_types) + 1}. Other (Custom Room Type)")
    print(f"{len(existing_room_types) + 2}. Exit")
    
    # Prompt user to select a room type option
    room_type_choice = input(f"Please choose an option (1-{len(existing_room_types) + 2}): ")

    # Handle the selection
    try:
        room_type_choice = int(room_type_choice)  # Convert input to integer
    except ValueError:
        print("Invalid choice. Please enter a number.")
        return
    
    # Check if the selected choice corresponds to a room type
    if 1 <= room_type_choice <= len(existing_room_types):
        selected_room_type = existing_room_types[room_type_choice - 1]
        prefix = get_room_prefix(selected_room_type)  # Extract prefix
        print(f"Room Type: {selected_room_type} (Prefix: {prefix})")
    elif room_type_choice == len(existing_room_types) + 1:  # Custom Room Type
        room_type = input("Enter a custom room type (must not match existing types): ")
        while room_type in existing_room_types:
            print(f"Error: '{room_type}' already exists. Please choose a different name.")
            room_type = input("Enter a custom room type (must not match existing types): ")
        prefix = get_room_prefix(room_type)  # Extract prefix for the custom type
        print(f"Room Type: {room_type} (Prefix: {prefix})")
    elif room_type_choice == len(existing_room_types) + 2:  # Exit option
        print("Exiting...")
        return
    else:
        print("Invalid choice. Returning to the administrator menu.")
        return

    # if room_type_choice == str(len(existing_room_types) + 1):  # Custom Room Type
    #     room_type = input("Enter a custom room type (must not match existing types): ")
    #     while room_type in existing_room_types:
    #         print(f"Error: '{room_type}' already exists. Please choose a different name.")
    #         room_type = input("Enter a custom room type (must not match existing types): ")
    # elif room_type_choice == '6':
    #     print("Thank you for using the Hotel Management System. Goodbye!")
    #     exit()
    # else:
    #     room_type = list(existing_room_types)[int(room_type_choice) - 1]

    # # Extract existing room numbers
    # existing_room_numbers = {room[0] for room in room_data}

    # # Get a unique room number for the selected room type
    # room_number = get_unique_room_number(room_type, existing_room_numbers)

    # # Get price and ensure it's numeric
    # while True:
    #     try:
    #         price = float(input("Enter the room price: "))
    #         if price <= 0:
    #             print("Error: Price must be a positive number.")
    #             continue
    #         break
    #     except ValueError:
    #         print("Error: Price must be a valid number.")

    # # Get availability and ensure it's valid
    # while True:
    #     availability = input("Enter the availability (Yes/No): ").strip().capitalize()
    #     if availability in ['Yes', 'No']:
    #         break
    #     else:
    #         print("Error: Availability must be either 'Yes' or 'No'.")

    # # Append the new room to rooms.txt
    # with open('rooms.txt', 'a') as f:
    #     f.write(f"{room_number},{room_type},{price},{availability}\n")
    
    # print(f"New room {room_number} ({room_type}) added successfully!")


def admin_menu():
    print("""
          
    *******************************************************
    *               Administrator Menu                    *
    *******************************************************
    1. Add New Rooms
    2. Remove Rooms
    3. Update Room Information
    4. Generate Reports
    5. View All Data
    6. Exit
    *******************************************************

    Please choose an option (1-6): """)
    
    choice = input("Enter choice: ")

    if choice == "1":
        add_room()

    elif choice == "2":
        print("Removing selected room")

    elif choice == "3":
        print("Updating Room Information")

    elif choice == "4":
        print("Generating Reports")
    
    elif choice == "5":
        print("View All Data")

    elif choice == "6":
        print("Thank you for using the Hotel Management System. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        admin_menu()
