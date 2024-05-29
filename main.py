from utils.log_manager import LogManager
from utils.error_handler import handle_exceptions
from models.model_preprocess import preprocess_text
from models.model_task1 import extract_content
from models.model_task2 import analyze_sentiment
from models.model_task3 import summarize_content
from models.model_task4 import enhance_summary
from utils.resource_monitor import ResourceMonitor
import logging

# Konfigurera loggning
LogManager.configure_logging(log_file="application.log", log_level=logging.INFO)

@handle_exceptions(default_return=None)
def run_workflow(input_text):
    # Prompts för varje steg
    prompts = {
        "preprocess": "Förbearbeta text",
        "extract": "Extrahera innehåll",
        "sentiment": "Analysera sentiment",
        "summarize": "Sammanfatta innehåll",
        "enhance": "Förbättra sammanfattning"
    }

    # Steg 1: Förbearbeta texten
    preprocessed_text = preprocess_text(input_text, prompts["preprocess"])
    logging.info(f"Förbearbetad text: {preprocessed_text}")

    # Steg 2: Extrahera viktigt innehåll
    extracted_content = extract_content(preprocessed_text, prompts["extract"])
    logging.info(f"Extraherat innehåll: {extracted_content}")

    # Steg 3: Analysera sentiment
    sentiment_analysis = analyze_sentiment(extracted_content, prompts["sentiment"])
    logging.info(f"Sentimentanalys: {sentiment_analysis}")

    # Steg 4: Sammanfatta innehållet
    summary = summarize_content(extracted_content, prompts["summarize"], max_length=min(20, len(extracted_content)))
    logging.info(f"Sammanfattning: {summary}")

    # Steg 5: Förbättra sammanfattningen
    enhanced_summary = enhance_summary(summary, prompts["enhance"], max_length=min(20, len(summary)))
    logging.info(f"Förbättrad sammanfattning: {enhanced_summary}")

    return enhanced_summary

@handle_exceptions(default_return=None)
def main(input_text):
    # Initiera och starta resursövervakning
    monitor = ResourceMonitor(interval=2)
    monitor.start()

    try:
        result = run_workflow(input_text)
    finally:
        # Se till att övervakningen stoppas
        monitor.stop()
    
    return result

if __name__ == "__main__":
    input_text = "Din inputtext här."
    result = main(input_text)
    if result:
        print("Slutlig sammanfattning:", result)
    else:
        print("Ett fel uppstod under körning av arbetsflödet.")