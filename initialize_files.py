import os    #os module - gives you access to functions that interact with the operating system. (e.g file & directory manipulation, path manipulation etc.)

def initialize_files():
    # Check if the users.txt file exists if not, create it.
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w') as f:
            # Add default admin:
            f.write("# username, password, role\n")     # Comment at the top of file that indicates the format of how the data is to be stored.
            f.write("jamila,jamila123,Administrator\n")  #default admin in first ran

        print("users.txt created with default admin.")

    # Check if rooms.txt file exists if not, create it.
    if not os.path.exists('rooms.txt'):
        with open('rooms.txt', 'w') as f:
            f.write('# room_number, room_type, price, availability\n')
            
            # Add Single rooms
            for i in range(1, 11):  # Numbers from 1 to 10
                f.write(f"S{100 + i},Single,100,No\n")  # S101, S102, ... S110

            # Add Double rooms
            for i in range(1, 11):  # Numbers from 1 to 10
                f.write(f"D{200 + i},Double,150,No\n")  # D201, D202, ... D210

            # Add Suite rooms
            for i in range(1, 6):  # Numbers from 1 to 5
                f.write(f"SU{300 + i},Suite,250,No\n")  # SU301, SU302, ... SU305

        print("rooms.txt created with default rooms.")

    # Check if 'bookings.txt' exists, if not create it
    if not os.path.exists('bookings.txt'):
        with open('bookings.txt', 'w') as f:
            # Create bookings file, initially empty
            f.write("# guest_name,contact,room_number,check_in_date,check_out_date\n")
        print("bookings.txt created.")

    # Check if 'config.txt' exists
    if not os.path.exists('config.txt'):
        with open('config.txt', 'w') as f:
            # Set default configuration values
            f.write("total_rooms=25\n")
            f.write("max_bookings_per_room=1\n")
        print("config.txt created with default settings.")


    print("All necessary files have been initialized.")
