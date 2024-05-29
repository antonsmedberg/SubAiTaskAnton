from transformers import pipeline

def enhance_summary(text, prompt="", model_name='facebook/bart-large-cnn', max_length=50, min_length=25):
    """
    Förbättrar sammanfattningen ytterligare med en annan modell.
    Prompt används för att styra förbättringen av sammanfattningen.
    :param text: Texten som ska förbättras.
    :param prompt: En valfri prompt för att styra förbättringen.
    :param model_name: Namnet på modellen som ska användas för att förbättra sammanfattningen.
    :param max_length: Maximal längd på den förbättrade sammanfattningen.
    :param min_length: Minimal längd på den förbättrade sammanfattningen.
    :return: Förbättrad sammanfattning.
    """
    if not isinstance(text, str):
        raise ValueError("Text måste vara en sträng.")

    try:
        enhancer = pipeline('summarization', model=model_name)
        enhanced_summary = enhancer(text, max_length=max_length, min_length=min_length, do_sample=False)
        enhanced_text = enhanced_summary[0]['summary_text']
        enhanced_text = f"{prompt}: {enhanced_text}" if prompt else enhanced_text
    except Exception as e:
        raise RuntimeError(f"Fel vid förbättring av sammanfattning: {e}")

    return enhanced_text