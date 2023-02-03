import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    def Test1(self):
        self.assertEqual(englishToFrench(''), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase):
    def Test1(self):
        self.assertEqual(frenchToEnglish(''), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
