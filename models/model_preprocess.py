import nltk
from nltk.corpus import stopwords

# Ladda NLTK-resurser
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text, prompt="", remove_stopwords=False):
    """
    Förbearbetar text genom att tokenisera och rengöra den.
    Prompt används för att styra förbearbetningen.
    :param text: Texten som ska förbearbetas.
    :param prompt: En valfri prompt för att styra förbearbetningen.
    :param remove_stopwords: Om True, tar bort stoppord från texten.
    :return: Förbearbetad text.
    """
    if not isinstance(text, str):
        raise ValueError("Text måste vara en sträng.")

    tokens = nltk.word_tokenize(text)  # Tokenisering
    cleaned_tokens = [token.lower() for token in tokens if token.isalnum()]

    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        cleaned_tokens = [token for token in cleaned_tokens if token not in stop_words]

    processed_text = ' '.join(cleaned_tokens)

    if prompt:
        processed_text = f"{prompt}: {processed_text}"

    return processed_text