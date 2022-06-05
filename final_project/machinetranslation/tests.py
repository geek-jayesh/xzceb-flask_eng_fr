import unittest

from translator import english_to_french, french_to_english

class TestLanguageTransaltion(unittest.TestCase):

    def test_e2f(self):
        self.assertEqual(
            english_to_french(null), 
            null
        )
        self.assertEqual(
            english_to_french(
                "Hello, my name is Jayesh and I'm here to help you."
            ), 
            "Bonjour, mon nom est Jayesh et je suis là pour vous aider."
        )

    def test_f2e(self):
        self.assertEqual(
            french_to_english(
                "Bonjour, mon nom est Jayesh et je suis là pour vous aider."
            ), 
            "Hello, my name is Jayesh and I'm here to help you."
        )



if __name__ == "__main__":
    unittest.main()