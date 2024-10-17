import unittest
from morning_greeting.contacts import Contacts, ContactExistsError, ContactNotFoundError

class TestContacts(unittest.TestCase):
    
    def setUp(self):
        self.contacts = Contacts()

    def test_add_contact(self):
        self.contacts.add_contact("Ole", "ole@ole.com", "08:00 AM")
        self.assertEqual(len(self.contacts.get_contacts()), 1)

    def test_add_duplicate_contact(self):
        self.contacts.add_contact("Ole", "ole@ole.com", "08:00 AM")
        with self.assertRaises(ContactExistsError):
            self.contacts.add_contact("Ole", "ole@ole.com", "08:00 AM")

    def test_remove_contact(self):
        self.contacts.add_contact("ole", "ole@ole.com", "09:00 AM")
        self.contacts.remove_contact("ole", "ole@ole.com")
        self.assertEqual(len(self.contacts.get_contacts()), 0)

    def test_remove_non_existent_contact(self):
        with self.assertRaises(ContactNotFoundError):
            self.contacts.remove_contact("Unknown", "unknown@example.com")

if __name__ == '__main__':
    unittest.main()