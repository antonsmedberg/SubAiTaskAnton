import unittest
from unittest.mock import patch
from main import run_workflow
import logging
from utils.log_manager import LogManager

# Konfigurera loggning för tester
LogManager.configure_logging(log_file="test_collaboration.log", log_level=logging.DEBUG)

class TestModelCollaboration(unittest.TestCase):

    @patch('models.model_preprocess.preprocess_text')
    @patch('models.model_task1.extract_content')
    @patch('models.model_task2.analyze_sentiment')
    @patch('models.model_task3.summarize_content')
    @patch('models.model_task4.enhance_summary')
    def test_models_collaboration(self, mock_enhance, mock_summarize, mock_analyze, mock_extract, mock_preprocess):
        # Mock responses for each sub-task
        mock_preprocess.return_value = "Förbearbeta text: hello world this is a test"
        mock_extract.return_value = "Extrahera innehåll: hello world"
        mock_analyze.return_value = "Analysera sentiment: [{'label': 'POSITIVE', 'score': 0.99}]"
        mock_summarize.return_value = "Sammanfatta innehåll: hello world summarized"
        mock_enhance.return_value = "Förbättra sammanfattning: hello world enhanced summarized"
        
        input_text = "Hello, World! This is a Test."
        expected_output = "Förbättra sammanfattning: hello world enhanced summarized"

        # Run the workflow
        actual_output = run_workflow(input_text)
        
        # Assertions
        mock_preprocess.assert_called_once_with(input_text, "Förbearbeta text")
        mock_extract.assert_called_once_with(mock_preprocess.return_value, "Extrahera innehåll")
        mock_analyze.assert_called_once_with(mock_extract.return_value, "Analysera sentiment")
        mock_summarize.assert_called_once_with(mock_extract.return_value, "Sammanfatta innehåll", max_length=20)
        mock_enhance.assert_called_once_with(mock_summarize.return_value, "Förbättra sammanfattning", max_length=20)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()