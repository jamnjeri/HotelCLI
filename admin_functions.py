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
def get_unique_room_number(room_number, prefix, room_type):
    # Ensure the room number is numeric
    if not room_number.isdigit():
        return False

    # Combine the room number with the prefix
    room_number_with_prefix = prefix.upper() + room_number

    # Read room data from the rooms.txt file
    existing_rooms = read_rooms_data()  # Assuming this function reads all rooms data

    # Check if the room number with the prefix already exists for the given room type
    for room in existing_rooms:
        if room[0] == room_number_with_prefix and room[1] == room_type:
            return False  # Room number is not unique

    # If we reach here, it means the room number is unique
    return True
        

# Function to extract the prefix (alphabet part) of the room type
def get_room_prefix(room_type):
    room_data = read_rooms_data()  # Get the data from the file
    existing_prefixes = set()

    # Gather existing prefixes from the room numbers for both existing and custom room types
    for room in room_data:
        existing_prefixes.add(''.join([char for char in room[0] if char.isalpha()]))

    # Check if the room type exists in the file
    if room_type in [room[1] for room in room_data]:
    
        for room in room_data:
            if room[1] == room_type:  # Compare room type
                room_number = room[0]  # Get the room number
                # Check the prefix by extracting leading alphabetic characters
                prefix = ''.join([char for char in room_number if char.isalpha()])
                return room_type, prefix  # Return both room type and its prefix
            
    else:
        # For new room types (Option 4 - Custom Room Type)
        while True:
            # Generate potential prefixes (first letter, first two letters, etc.)
            potential_prefix = room_type[:1]  # Start with the first letter
            if potential_prefix not in existing_prefixes:
                return room_type, potential_prefix  # Return the room type and the unique prefix
            potential_prefix = room_type[:2]  # Try the first two letters
            if potential_prefix not in existing_prefixes:
                return room_type, potential_prefix  # Return the room type and the unique prefix
            potential_prefix = room_type[:3]  # Try the first three letters
            if potential_prefix not in existing_prefixes:
                return room_type, potential_prefix  # Return the room type and the unique prefix
            
            # If none of these worked, prompt the user for a new room type (if needed)
            print(f"The prefix for room type '{room_type}' already exists. Please choose another name.")
            room_type = input("Enter a new custom room type: ")


# Function to get the price for an existing room type
def get_price_for_room_type(room_type):
    try:
        with open("rooms.txt", 'r') as file:
            # Skip the first line (comment)
            next(file)
            for line in file:
                room_info = line.strip().split(',')
                if len(room_info) == 4 and room_info[1] == room_type:
                    # If room type matches, return the price
                    return float(room_info[2])  # Price is at index 2
    except FileNotFoundError:
        print("Error: rooms.txt file not found.")
    return None  # Return None if room type not found


# Function to add the new room to rooms.txt
def add_room_to_file(room_number, room_type, price):
    availability = "No"  # Assume the new room is not available by default

    try:
        with open("rooms.txt", 'a') as file:
            # Prepare the new room entry in the correct format
            new_room_entry = f"{room_number},{room_type},{price},{availability}\n"
            
            # Append the new room entry to the file
            file.write(new_room_entry)
            print(f"Room {room_number} ({room_type}) has been added successfully.")
    
    except FileNotFoundError:
        print("Error: rooms.txt file not found.")


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
    # room_type_choice = input(f"Please choose an option (1-{len(existing_room_types) + 2}): ")

    chosen_room_type = None
    prefix = None
    room_number = None
    price = None

    while True:  # Loop to keep asking for a valid input
        # Prompt user to select a room type option
        room_type_choice = input(f"Please choose an option (1-{len(existing_room_types) + 2}): ")

        try:
            room_type_choice = int(room_type_choice)  # Convert input to integer
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue  # If input is not a valid number, continue asking
    
        # Check if the selected choice corresponds to a room type
        if 1 <= room_type_choice <= len(existing_room_types):
            selected_room_type = existing_room_types[room_type_choice - 1]
            chosen_room_type, prefix = get_room_prefix(selected_room_type)  # Extract prefix
            break
            # print(f"Room Type: {selected_room_type} Function Room Type Return: {chosen_room_type} (Prefix: {prefix})")
        elif room_type_choice == len(existing_room_types) + 1:  # Custom Room Type
            room_type = input("Enter a custom room type (must not match existing types): ")
            while room_type in existing_room_types:
                # print(f"Error: '{room_type}' already exists. Please choose a different name.")
                room_type = input("Enter a custom room type (must not match existing types): ")
            # Generate prefix for the custom room type
            chosen_room_type, prefix = get_room_prefix(room_type)
            break
            # print(f"Room Type: {chosen_room_type} (Prefix: {prefix})")
        elif room_type_choice == len(existing_room_types) + 2:  # Exit option
            print("Exiting...")
            print("Thank you for using the Hotel Management System. Goodbye!")
            return
        else:
            print("Invalid choice. Returning to the administrator menu.")
            return
    

    print(f"Room Typeeeeeeeeeeee: {chosen_room_type} (Prefix: {prefix})")

    while True:
        room_number = input(f"Enter the room number for {chosen_room_type} (e.g., 101 for prefix '{prefix}'): ")

        # Check if the room number is unique
        if not get_unique_room_number(room_number, prefix, chosen_room_type):
            print(f"Error: Room number {prefix.upper() + room_number} already exists for {chosen_room_type}. Please choose a different number.")
            continue  # Re-prompt the user for a unique room number
        else:
            break  # Proceed once a unique room number is entered

    
    room_number_with_prefix = prefix.upper() + room_number

    room_number = room_number_with_prefix

    print(f"Room Typeeeeeeeeeeee: {chosen_room_type} Prefix: {prefix} Room Number: {room_number}")


    # Check if the room type exists in rooms.txt
    existing_price = get_price_for_room_type(chosen_room_type)

    if existing_price is not None:
        # Room type exists, use existing price
        print(f"Room Type {chosen_room_type} already exists. The price is {existing_price}.")
        price = existing_price
    else:
        # Room type doesn't exist, prompt user for price
        while True:
            price = input(f"Enter the price for the {chosen_room_type} room (greater than 0): ")

            # Ensure the price is numeric and greater than 0
            try:
                price = float(price)
                if price <= 0:
                    print("Error: Price must be greater than 0.")
                    continue  # Re-prompt for a valid price
                else:
                    break  # Valid price, exit the loop
            except ValueError:
                print("Error: Price must be a valid number.")
                continue  # Re-prompt for a valid price

    print(f"Room Type: {chosen_room_type} Room Number: {room_number} Price: {price}")

    # Add the new room to the file
    add_room_to_file(room_number_with_prefix, chosen_room_type, price)


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
