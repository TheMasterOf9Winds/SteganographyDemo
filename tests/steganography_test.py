import unittest
from PIL import Image
import os
import json
from steganography import message_to_binary, binary_to_message, hide_message_in_image, reveal_message_in_image

class TestSteganography(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('tests/test_cases.json', 'r', encoding='utf-8') as file:
            cls.test_cases = json.load(file)

    def setUp(self):
        # Create a simple image for testing
        self.test_image = 'test_image.png'
        image = Image.new('RGB', (100, 100), color='white')
        image.save(self.test_image)

    def tearDown(self):
        # Remove the test image and hidden message image after tests
        if os.path.exists(self.test_image):
            os.remove(self.test_image)
        if os.path.exists('hidden_message_image.png'):
            os.remove('hidden_message_image.png')

    def test_message_to_binary(self):
        for case in self.test_cases['message_to_binary']:
            with self.subTest(case=case):
                self.assertEqual(message_to_binary(case['message']), case['expected_binary'])

    def test_binary_to_message(self):
        for case in self.test_cases['binary_to_message']:
            with self.subTest(case=case):
                self.assertEqual(binary_to_message(case['binary']), case['expected_message'])

    def test_hide_and_reveal_message_in_image(self):
        for case in self.test_cases['hide_and_reveal_message_in_image']:
            with self.subTest(case=case):
                hide_message_in_image(self.test_image, case['message'])
                revealed_message = reveal_message_in_image('hidden_message_image.png')
                self.assertEqual(revealed_message, case['message'])

    def test_hide_message_too_long(self):
        message = "a" * 1000  # A long message
        with self.assertRaises(ValueError):
            hide_message_in_image(self.test_image, message)

if __name__ == '__main__':
    unittest.main()