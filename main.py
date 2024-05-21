'''
main driver for a simple social network project
'''
import importlib
import users
import user_status
import csv

filename = 'accounts.csv'
filename_2 = 'status_updates.csv'


def init_user_collection():
    '''
    Creates and returns a new instance of UserCollection
    '''

    return users.UserCollection()


def init_status_collection():
    '''
    Creates and returns a new instance of UserStatusCollection
    '''

    return user_status.UserStatusCollection()


def load_users(user_collection, filename):
    '''
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''

    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                for user_attribute in list(row.values()):
                    if not user_attribute or user_attribute.isspace():
                        print(f"ERROR: Empty field in {row}")
                        return False

                    user_id = row['USER_ID']
                    email = row['EMAIL']
                    user_name = row['NAME']
                    user_last_name = row['LASTNAME']

                    user_collection.add_user(user_id, email, user_name, user_last_name)

        print("\n\t\tFile read successfully")

        return True

    except FileNotFoundError:
        print('\n\t\tERROR: The File does not exist!')
        return False
    except OSError:
        print("\n\t\tERROR: There's an OS error here.")
        return False


def save_users(user_collection, filename):
    '''
    Saves all users in user_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such as an invalid filename).
    - Otherwise, it returns True.
    '''
    header = ['USER_ID', 'EMAIL', 'NAME', 'LASTNAME']
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            for row in user_collection.database:

                user_ids = user_collection.database[row].user_id
                emails = user_collection.database[row].email
                firstname = user_collection.database[row].user_name
                lastname = user_collection.database[row].user_last_name
                
                new_dict = {'USER_ID': user_ids, 'EMAIL': emails, 'NAME': firstname, 'LASTNAME': lastname}
                writer.writerow(new_dict)

    except FileNotFoundError:
        print("ERROR: The File does not exist")
        return False
    except OSError:
        print("ERROR: There's an OS Error")
        return False


def load_status_updates(status_collection, filename_2):
    '''
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection
    STATUS_ID,USER_ID,STATUS_TEXT
    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    '''
    try:
        with open(filename_2, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                status_id = row['STATUS_ID']
                user_id = row['USER_ID']
                status_text = row['STATUS_TEXT']

                status_collection.add_status(status_id, user_id, status_text)

        print("\n\t\tFile read successfully")
        return True
    except FileNotFoundError:
        print('\n\t\tERROR: The File does not exist!')
        return False
    except OSError:
        print("\n\t\tERROR: There's an OS error here.")
        return False


def save_status_updates(status_collection, filename_2):
    '''
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    '''
    try:
        with open(filename_2, 'w', newline='') as csvfile:
            header = ['STATUS_ID', 'USER_ID', 'STATUS_TEXT']
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            for row in status_collection.database:

                status_id = status_collection.database[row].status_id
                user_id = status_collection.database[row].user_id
                status_text = status_collection.database[row].status_text

                new_dict = {'STATUS_ID': status_id, 'USER_ID': user_id, 'STATUS_TEXT': status_text}
                writer.writerow(new_dict)
            print("Status updates saved successfully.")
            return True
    except FileNotFoundError:
        print("ERROR: The File does not exist")
        return False
    except OSError:
        print("ERROR: There's an OS Error")
        return False


def add_user(user_collection, user_id, email, user_name, user_last_name):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    '''


    user_collection.add_user(user_id, email, user_name, user_last_name)


def update_user(user_collection, user_id, email, user_name, user_last_name):
    '''
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''


    print(f'\n\t\t',user_collection.modify_user(user_id, email, user_name, user_last_name))


def delete_user(user_collection, user_id):
    '''
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''
    
    print(f'\n\t\t',user_collection.delete_user(user_id))


def search_user(user_collection, user_id):
    '''
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    '''

    print(f'\n\t\t',
        user_collection.search_user(user_id).user_id,
        user_collection.search_user(user_id).email,
        user_collection.search_user(user_id).user_name,
        user_collection.search_user(user_id).user_last_name)


def add_status(status_collection, status_id, user_id, status_text):
    '''
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    status_collection.add_status(status_id,user_id,status_text)


def update_status(status_collection, status_id, user_id, status_text):
    '''
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    
    status_collection.modify_status(status_id, user_id, status_text)


def delete_status(status_collection,status_id):
    '''
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    '''
    
    status_collection.delete_status(status_id)


def search_status(status_collection, status_id):
    '''
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    '''

    
    status_collection.search_status(status_id)


def main():

    user_collection = init_user_collection()
    status_collection = init_status_collection()

    while True:

        print("""\n
        ************ Users Database Menu ************
        1. Load Users Database
        2. Save Users Database
        3. Add Users to Users Database
        4. Modify Users in User Database
        5. Delete User in Users Database
        6. Search User in Users Database


        ************ User Status Database Menu ************
        7. Load User Status Database
        8. Save User Status Database
        9. Add New Status to Database
        10. Modify User Status in Status Database
        11. Delete Status in Status Database
        12. Search Status in Status Database


        0. Exit Program
""")

        choice = input("\n\t\tPlease make a choice: ")

        if choice == '0':
            print("\n\t\tExiting Program")
            break


        elif choice == '1':
            load_users(user_collection, filename)



        elif choice == '2':
            save_users(user_collection, filename)


        elif choice == '3':
            user_id = input("\n\t\tType in a user ID: ").lower()
            email = input("\n\t\tType in an email address: ").lower()
            user_name = input("\n\t\tType in users first name: ").lower()
            user_last_name = input("\n\t\tType in users last name: ").lower()

            add_user(user_collection, user_id, email, user_name, user_last_name) 


        elif choice == '4': 
            user_id = input("\n\t\tType in a user ID: ").lower()
            email = input("\n\t\tType in an email address: ").lower()
            user_name = input("\n\t\tType in users first name: ").lower()
            user_last_name = input("\n\t\tType in users last name: ").lower()
            update_user(user_collection, user_id, email, user_name, user_last_name)


        elif choice == '5':
            user_id = input('\n\t\tplease type in a user id to remove: ').lower()
            delete_user(user_collection, user_id)


        elif choice == '6':
            user_id = input('\n\t\ttype in a user id: ').lower()
            search_user(user_collection, user_id)



        elif choice == '7': 
            load_status_updates(status_collection, filename_2)


        elif choice == '8':
            save_status_updates(status_collection, filename_2)


        elif choice == '9':
            status_id = input('\n\t\ttype in a status id: ').lower()
            user_id = input('\n\t\ttype in a user id: ').lower()
            status_text = input('\n\t\ttype in status update: ').lower()
            add_status(status_collection, status_id, user_id, status_text) 


        elif choice == '10':
            status_id = input("\n\t\ttype in status id: ").lower()
            user_id = input("\n\t\ttype in user id: ").lower()
            status_id = input("\n\t\ttype in status update: ").lower()
            update_status(status_collection, status_id, user_id, status_text)


        elif choice == '11':
            status_id = input('\n\t\tplease type in a status id to remove: ').lower()
            delete_status(status_collection, status_id)


        elif choice == '12':
            status_id = input('\n\t\ttype in a status id to search: ').lower()
            search_status(status_collection, status_id)


        else:
            print("\n\t\tInvalid choice, please choose from the listed options")


if __name__ == '__main__':

    main()