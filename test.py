import unittest

#import all the test module
from test_contacts import TestContacts
from test_message_generator import TestMessageGenerator
from test_message_sender import TestMessageSender

def run_all_tests():
    #Initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    #add tests to the suite
    suite.addTests(loader.loadTestsFromTestCase(TestContacts))
    suite.addTests(loader.loadTestsFromTestCase(TestMessageGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestMessageSender))

    #Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_all_tests()