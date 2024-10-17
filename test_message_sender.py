import unittest
from unittest.mock import patch
from morning_greeting.message_sender import send_message

class TestMessageSender(unittest.TestCase):

    @patch('message_sender.send_message')
    def test_send_message(self, mock_send_message):
        mock_send_message.return_value = True
        result = send_message("test@example.com", "Test Message")
        self.assertTrue(result)

    @patch('message_sender.send_message')
    def test_send_message_failure(self, mock_send_message):
        mock_send_message.side_effect = ValueError("Invalid email address")
        with self.assertRaises(ValueError):
            send_message("invalid-email", "Test Message")

if __name__ == '__main__':
    unittest.main()