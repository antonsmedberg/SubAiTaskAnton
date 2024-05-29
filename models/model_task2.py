from transformers import pipeline

def analyze_sentiment(text, prompt="", return_all_scores=False):
    """
    Analyserar sentimentet i texten.
    Prompt används för att styra sentimentanalysen.
    :param text: Texten som ska analyseras.
    :param prompt: En valfri prompt för att styra sentimentanalysen.
    :param return_all_scores: Om True, returnerar alla sentimentpoäng.
    :return: Sentimentanalysresultat som en sträng.
    """
    if not isinstance(text, str):
        raise ValueError("Text måste vara en sträng.")

    try:
        sentiment_analyzer = pipeline('sentiment-analysis', return_all_scores=return_all_scores)
        sentiments = sentiment_analyzer(text)
        sentiment_text = f"{prompt}: {sentiments}" if prompt else str(sentiments)
    except Exception as e:
        raise RuntimeError(f"Fel vid sentimentanalys: {e}")

    return sentiment_text