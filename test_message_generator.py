import unittest

from morning_greeting.message_generator import generate_message

class TestMessageGenerator(unittest.TestCase):


    def test_message_includes_name(self):
        name = "Liv"
        email = "liv@liv.com"
        message = generate_message(name, email)
        self.assertIn(name, email, message)
