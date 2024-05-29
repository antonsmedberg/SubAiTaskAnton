from transformers import pipeline

def extract_content(text, prompt="", extract_sentences=False):
    """
    Extraherar viktiga meningar från texten baserat på namngivna entiteter.
    Prompt används för att styra extraheringen.
    :param text: Texten som ska analyseras.
    :param prompt: En valfri prompt för att styra extraheringen.
    :param extract_sentences: Om True, extraherar meningar som innehåller viktiga entiteter.
    :return: Extraherat innehåll baserat på namngivna entiteter.
    """
    if not isinstance(text, str):
        raise ValueError("Text måste vara en sträng.")

    try:
        extractor = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english')
        entities = extractor(text)
        if extract_sentences:
            important_sentences = set()
            for entity in entities:
                important_sentences.add(entity['word'])
            extracted_text = '. '.join(important_sentences)
        else:
            important_words = set(entity['word'] for entity in entities)
            extracted_text = ' '.join(important_words)
    except Exception as e:
        raise RuntimeError(f"Fel vid extrahering av innehåll: {e}")

    if prompt:
        extracted_text = f"{prompt}: {extracted_text}"

    return extracted_text