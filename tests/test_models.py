import unittest
from models.model_preprocess import preprocess_text
from models.model_task1 import extract_content
from models.model_task2 import analyze_sentiment
from models.model_task3 import summarize_content
from models.model_task4 import enhance_summary
import logging
from utils.log_manager import LogManager

# Konfigurera loggning för tester
LogManager.configure_logging(log_file="test_models.log", log_level=logging.DEBUG)

class TestModelFunctions(unittest.TestCase):

    def test_preprocess_text(self):
        input_text = "Hello, World! This is a Test."
        expected_output = "Förbearbeta text: hello world this is a test"
        actual_output = preprocess_text(input_text, prompt="Förbearbeta text")
        self.assertEqual(actual_output, expected_output)

    def test_extract_content(self):
        input_text = "Barack Obama was born in Hawaii. He was the 44th President of the United States."
        expected_words = {"barack", "obama", "hawaii", "president"}
        actual_output = extract_content(input_text, prompt="Extrahera innehåll")
        self.assertTrue(all(word in actual_output.lower() for word in expected_words))

    def test_analyze_sentiment(self):
        input_text = "I love this place!"
        actual_output = analyze_sentiment(input_text, prompt="Analysera sentiment")
        self.assertTrue("POSITIVE" in actual_output)

    def test_summarize_content(self):
        input_text = "Barack Obama was born in Hawaii. He was the 44th President of the United States."
        actual_output = summarize_content(input_text, prompt="Sammanfatta innehåll", max_length=20)
        self.assertIsInstance(actual_output, str)
        self.assertTrue(len(actual_output) > 0)

    def test_enhance_summary(self):
        input_text = "Barack Obama was born in Hawaii. He was the 44th President of the United States."
        actual_output = enhance_summary(input_text, prompt="Förbättra sammanfattning", max_length=20)
        self.assertIsInstance(actual_output, str)
        self.assertTrue(len(actual_output) > 0)

if __name__ == '__main__':
    unittest.main()