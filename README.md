
# SubAiTaskAnton

## Projektbeskrivning

Detta projekt är utformat för att använda flera AI-modeller för att lösa en större uppgift genom att dela upp den i deluppgifter. Projektet använder sig av flera modeller från HuggingFace Transformers för att förbearbeta text, extrahera innehåll, analysera sentiment, sammanfatta innehåll och förbättra sammanfattningar.

## Projektstruktur

```
SubAiTaskAnton/
├── main.py
├── requirements.txt
├── utils/
│   ├── error_handler.py
│   ├── log_manager.py
│   ├── resource_monitor.py
├── models/
│   ├── __init__.py
│   ├── model_preprocess.py
│   ├── model_task1.py
│   ├── model_task2.py
│   ├── model_task3.py
│   ├── model_task4.py
├── tests/
│   ├── __init__.py
│   ├── test_collaboration.py
│   ├── test_integration.py
│   ├── test_models.py
└── setup_nltk.py
```

## Installation

Följ dessa steg för att installera och konfigurera projektet:

1. Klona repositoriet:
    ```sh
    git clone <repository-url>
    cd SubAiTaskAnton
    ```

2. Skapa och aktivera en virtuell miljö (valfritt men rekommenderas):
    ```sh
    python -m venv venv
    source venv/bin/activate  # På Windows: venv\Scripts\activate
    ```

3. Installera beroenden:
    ```sh
    pip install -r requirements.txt
    ```

4. Ladda NLTK-resurser:
    ```sh
    python setup_nltk.py
    ```

## Användning

För att köra huvudprogrammet, använd:
```sh
python main.py
```

### Exempel på körning

```python
input_text = "Din inputtext här."
result = main(input_text)
print("Slutlig sammanfattning:", result)
```

## Tester

För att köra testerna, använd:
```sh
python -m unittest discover -s tests
```

## Filbeskrivningar

### `main.py`

Innehåller huvudlogiken för arbetsflödet som består av följande steg:
1. Förbearbeta texten
2. Extrahera viktigt innehåll
3. Analysera sentiment
4. Sammanfatta innehållet
5. Förbättra sammanfattningen

### `utils/`

- **error_handler.py**: Hanterar undantag och loggar fel.
- **log_manager.py**: Konfigurerar loggning för projektet.
- **resource_monitor.py**: Övervakar systemresurser som CPU och minne.

### `models/`

- **model_preprocess.py**: Förbearbetar text genom tokenisering och rengöring.
- **model_task1.py**: Extraherar viktigt innehåll baserat på namngivna entiteter.
- **model_task2.py**: Analyserar sentiment i texten.
- **model_task3.py**: Sammanfattar texten.
- **model_task4.py**: Förbättrar sammanfattningen med en annan modell.

### `tests/`

Innehåller tester för att verifiera att modellerna och arbetsflödet fungerar korrekt.

- **test_collaboration.py**: Tester för samarbete mellan modellerna.
- **test_integration.py**: Integrationstester för hela arbetsflödet.
- **test_models.py**: Enhetstester för varje modellfunktion.

## Författare

Anton Oskar Smedberg

## Licens

Detta projekt är licensierat under MIT-licensen.
