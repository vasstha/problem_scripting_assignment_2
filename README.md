# Morning Greetings

Morning Greetings is a Python package that automates the process of sending personalized "Good Morning" messages to a list of friends.

## Installation

There are several ways to install the Morning Greetings package:

### 1. Install from GitHub

You can install the latest version directly from the GitHub repository:

```
pip install git+https://github.com/yourusername/morning_greetings.git
```

Replace `yourusername` with your actual GitHub username.

### 2. Install from local source

If you've cloned the repository or downloaded the source code:

1. Navigate to the project directory:
   ```
   cd path/to/morning_greetings
   ```
2. Install the package:
   ```
   pip install .
   ```

### 3. Install for development

If you're planning to modify the package:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/morning_greetings.git
   ```
2. Navigate to the project directory:
   ```
   cd morning_greetings
   ```
3. Install in editable mode:
   ```
   pip install -e .
   ```

## Usage

Here's a basic example of how to use the Morning Greetings package:

```python
from morning_greetings import ContactsManager, generate_message, send_message, log_message

# Initialize the ContactsManager
manager = ContactsManager()

# Add contacts
manager.add_contact("Alice", "alice@example.com", "07:00 AM")
manager.add_contact("Bob", "bob@example.com", "08:00 AM")

# Send messages
for contact in manager.get_contacts():
    message = generate_message(contact['name'])
    if send_message(contact['email'], message):
        log_message(contact, message)

# List all contacts
manager.list_contacts()
```

## Running Tests

To run the unit tests:

1. Ensure you're in the project directory
2. Run the following command:
   ```
   python -m unittest test
   ```

## Contributing

1. Fork the repository on GitHub
2. Create a new branch for your feature or bug fix
3. Commit your changes
4. Push your branch to your fork
5. Submit a pull request to the main repository

## License

This project is licensed under the MIT License - see the LICENSE file for details.


Morning Greetings
Morning Greetings is a Python package that automates the process of sending personalized "Good Morning" messages to a list of friends.
Installation

Clone this repository:
Copygit clone https://github.com/yourusername/morning_greetings.git

Navigate to the project directory:
Copycd morning_greetings

Install the package:
Copypip install -e .


Usage
Run the main script:
Copypython main.py
Follow the on-screen prompts to send messages, add contacts, remove contacts, or list contacts.
Features

Manage a list of contacts with their names, email addresses, and preferred greeting times
Generate personalized "Good Morning" messages
Simulate sending messages (can be replaced with actual email sending logic)
Log sent messages

File Structure

morning_greetings/: Main package directory

__init__.py: Package initializer
contacts.py: Module for managing contacts
message_generator.py: Module for generating personalized messages
message_sender.py: Module for simulating message sending
logger.py: Module for logging sent messages
contacts_manager.py: Module for managing contacts in a JSON file


main.py: Main script to run the program
setup.py: Setup file for package installation
README.md: This file
requirements.txt: List of package dependencies

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
License
MIT
