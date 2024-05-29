from transformers import pipeline

def summarize_content(text, prompt="", model_name='sshleifer/distilbart-cnn-12-6', max_length=50, min_length=25):
    """
    Sammanfattar texten.
    Prompt används för att styra sammanfattningen.
    :param text: Texten som ska sammanfattas.
    :param prompt: En valfri prompt för att styra sammanfattningen.
    :param model_name: Namnet på modellen som ska användas för sammanfattning.
    :param max_length: Maximal längd på sammanfattningen.
    :param min_length: Minimal längd på sammanfattningen.
    :return: Sammanfattad text.
    """
    if not isinstance(text, str):
        raise ValueError("Text måste vara en sträng.")

    try:
        summarizer = pipeline('summarization', model=model_name)
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        summarized_text = summary[0]['summary_text']
        summarized_text = f"{prompt}: {summarized_text}" if prompt else summarized_text
    except Exception as e:
        raise RuntimeError(f"Fel vid sammanfattning: {e}")

    return summarized_text