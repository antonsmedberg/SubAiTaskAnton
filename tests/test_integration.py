import unittest
from main import main
import logging
from utils.log_manager import LogManager

# Konfigurera loggning för tester
LogManager.configure_logging(log_file="test_integration.log", log_level=logging.DEBUG)

class TestIntegration(unittest.TestCase):

    def test_full_workflow(self):
        input_text = "Barack Obama was born in Hawaii. He was the 44th President of the United States."
        summary = main(input_text)
        
        # Kontrollera att den slutliga sammanfattningen är en sträng och inte tom
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) > 0)
        
        # Ytterligare kontroller kan läggas till för att verifiera korrekthet i sammanfattningen
        print("Sammanfattning:", summary)

if __name__ == '__main__':
    unittest.main()