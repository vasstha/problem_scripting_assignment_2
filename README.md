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
