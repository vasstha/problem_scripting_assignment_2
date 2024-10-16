import json

class ContactExistsError(Exception):
    pass

class ContactNotFoundError(Exception):
    pass


class Contacts:
    def __init__(self, file_name = "contacts.json"):
        self.file_name = file_name
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        try:
            with open(self.file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_contacts(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self, name, email, preferred_time="08:00 AM"):
    # Check if email already exists in contacts
        if any(contact['email'] == email for contact in self.contacts):
            print(f"ContactExistsError raised for email: {email}")  # Debugging print
            raise ContactExistsError(f"A contact with email {email} already exists.")
        
        # Otherwise, add the new contact
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)
        print(f"Contact {name} with email {email} added successfully.")

    #remove contact by name
    def remove_contact(self, name, email):
        for contact in self.contacts:
            if contact['name'] == name and contact['email'] == email:
                self.contacts.remove(contact)
                print(f"Contact {name} with email {email} removed successfully.")
                return
        # If no contact is found, raise the exception
        raise ContactNotFoundError(f"Contact with name {name} and email {email} not found.")
        #self.contacts = [c for c in self.contacts if c['name'] != name]
        #print(f"Contact {name} removed.")

    #get all contacts
    def get_contacts(self):
        return self.contacts
    

    def get_contact(self, email):
        for contact in self.contacts:
            if contact['email'] == email:
                return contact
            
        return None
    
    def update_contact(self, email, new_name = None, new_email = None, new_preferred_time = None):
        contact = self.get_contact(email)
        if contact:
            if new_name:
                contact['name'] = new_name
            if new_email:
                #check if new email already exists
                if new_email != email and any(c['email'] == new_email for c in self.contacts):
                    raise ContactExistsError("A contact with email {new_email} already exists.")
                contact['email'] = new_email

            if new_preferred_time:
                contact['preferred_time'] = new_preferred_time
            print(f"Contact updated successfully.")

        else:
            raise ContactNotFoundError(f"No contact found with email {email}.")

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name : {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")      
        
