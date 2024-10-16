import os
import sys
import time


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from contacts import Contacts, ContactExistsError, ContactNotFoundError
from message_generator import generate_message
from message_sender import send_message
from logger import log_message

def main():
    contacts = Contacts()

    while True:
        print("\nGood Morning Message Sender")
        print("1. Send Messages")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Input your choice: ")

        if choice == '1':
            contact_list = contacts.get_contacts()

            if not contact_list:
                print("No contacts found. Please add contact first.")
            else:
                for contact in contact_list:
                    message = generate_message(contact['name'])
                    try:
                        if send_message(contact['name'], contact['email'], message):
                            log_message(contact, message)
                            print(f"Message sent to {contact['name']}")
                    except ValueError as e:
                        print(f"Error sending message to {contact['name']}: {str(e)}")
        
        elif choice == '2':
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            preferred_time = input("Enter preferred time (HH:MM AM/PM): ")
            try:
                contacts.add_contact(name, email, preferred_time)
                print("Contact added successfully.")
            except ContactExistsError as e:
                print(f"Error: {e}")



        elif choice == '3':
            name = input("Enter contact name to remove: ")
            email = input("Enter contact email to remove: ")

            try:
                contacts.remove_contact(name, email)
                print("Contact removed successfully")
                
                """ except ContactNotFoundError as e:
                    # This will handle the exception and not crash the program
                print(f"Error: {e}") """
            
            except ContactNotFoundError as e:
                # This will handle the exception and not crash the program
                print(f"Error: {e}")
        
                # Allow user to decide what to do next after the error
                user_choice = input("Do you want to try again with different details? (yes/no): ").strip().lower()

                if user_choice == 'yes':
                    continue  # Restart the loop to allow user to input different details
                else:
                    print("Exiting the remove contact operation.")

        elif choice == '4':
            
            if not contacts.get_contacts():
                print("No contacts found. Please add contact first.")
            else:
                print("Listing all contacts.")
                contacts.list_contacts()

        elif choice == '5':
            print("Existing the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()