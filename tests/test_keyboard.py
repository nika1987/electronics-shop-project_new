import unittest

from src.keyboard import KeyBoard


class TestKeyBoard(unittest.TestCase):
    def setUp(self):
        self.keyboard = KeyBoard('Logitech', 50.0, 10)

    def test_init(self):
        self.assertEqual(self.keyboard.name, 'Logitech')
        self.assertEqual(self.keyboard.price, 50.0)
        self.assertEqual(self.keyboard.quantity, 10)

    def test_change_lang(self):
        self.assertEqual(self.keyboard.language, 'EN')
        self.keyboard.change_lang('RU')
        self.assertEqual(self.keyboard.language, 'RU')
        with self.assertRaises(AttributeError):
            self.keyboard.change_lang('ES')