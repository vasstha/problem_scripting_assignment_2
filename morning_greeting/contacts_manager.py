import json
import os

class ContactsManager:
    def __init__(self, file_path='contacts.json'):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error reading {self.file_path}. File may be empty or corrupted. Starting with an empty contact list.")
            return []

    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.contacts, file, indent = 2)

    def add_contact(self, name, email, preferred_time = "08:00"):
        contact = {
            'name' : name,
            'email' : email,
            'preferred_time' : preferred_time
        }
        self.contacts.append(contact)
        self.save_contacts()

    def remove_contact(self, name, email):
        self.contacts = [c for c in self.contacts if c ['name'] != name and c['email'] == email]

    def get_contacts(self):
        return self.contacts

    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time {contact['preferred_time']}")