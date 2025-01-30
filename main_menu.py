import os
from initialize_files import initialize_files  # Import the initialize function
from login import login
from admin_functions import admin_menu

def main_menu():
    # Initialize files (create necessary files if they don't exist)
    initialize_files()

    # ASCII Art
    print("""
    *******************************************************
    *                                                     *
    *         Welcome to the Hotel Management System      *
    *                                                     *
    *******************************************************

                                      /\\
                                      /\\
                                      /\\
                                      /\\
                                    _`=='_
                                 _-~......~-_
                             _--~............~--_
                       __--~~....................~~--__
           .___..---~~~................................~~~---..___,
            `=.________________________________________________,='
               @^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^@
                        |  |  I   I   II   I   I  |  |
                        |  |__I___I___II___I___I__|  |
                        | /___I_  I   II   I  _I___\\ |
                        |'_     ~~~~~~~~~~~~~~     _`|
                    __-~...~~~~~--------------~~~~~...~-__
            ___---~~......................................~~---___
.___..---~~~......................................................~~~---..___,
 `=.______________________________________________________________________,='
    @^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^@
              |   |    | |    |  |    ||    |  |    | |    |   |
              |   |____| |____|  |    ||    |  |____| |____|   |
              |__________________|____||____|__________________|
            _-|_____|_____|_____|__|------|__|_____|_____|_____|-_  __Jamila__

    *******************************************************
    *               Main Menu                             *
    *******************************************************
    1. Administrator Login
    2. Receptionist Login
    3. Hotel Guest Login
    4. Restaurant Manager Login
    5. Exit
    *******************************************************

    Please choose an option (1-5): """)
    
    choice = input("Enter choice: ")

    if choice == "1":
        admin_login()
    elif choice == "2":
        receptionist_login()
    elif choice == "3":
        guest_login()
    elif choice == "4":
        restaurant_manager_login()
    elif choice == "5":
        print("Thank you for using the Hotel Management System. Goodbye!")
        print("""
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
        """)
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def admin_login():
    if login("Administrator"):
        print("Login Succesful, administrator")
        admin_menu()  # Call the admin menu if login successful
    else:
        print("Login failed. Returning to main menu.")
        main_menu()

def receptionist_login():
        if login("Receptionist"):
            # receptionist_menu()  # Call the receptionist menu if login successful
            print("Login Succesful, receptionist")
        else:
            print("Login failed. Returning to main menu.")
            main_menu()

def guest_login():
        if login("Guest"):
            # guest_menu()  # Call guest menu if login successful
            print("Login Succesful, guest")
        else:
            print("Login failed. Returning to main menu.")
            main_menu()

def restaurant_manager_login():
        if login("Restaurant Manager"):
            # restaurant_manager_menu()  # Call restaurant manager menu if login successful
            print("Login Succesful, restaurant manager")
        else:
            print("Login failed. Returning to main menu.")
            main_menu()

if __name__ == "__main__":
    main_menu()
