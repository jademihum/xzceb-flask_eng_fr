import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    def Test1(self):
        self.assertNotEqual(englishToFrench, None)
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase):
    def Test1(self):
        self.assertNotEqual(frenchToEnglish, None)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
