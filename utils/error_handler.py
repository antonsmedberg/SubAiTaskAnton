import logging
from functools import wraps

def handle_exceptions(default_return=None):
    """
    Dekorator för att hantera undantag och logga fel.
    :param default_return: Värdet som ska returneras vid ett fel.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as ve:
                logging.error(f"Värdefel i {func.__name__}: {ve}")
                return default_return
            except TypeError as te:
                logging.error(f"Typfel i {func.__name__}: {te}")
                return default_return
            except Exception as e:
                logging.error(f"Okänt fel i {func.__name__}: {e}")
                return default_return
        return wrapper
    return decorator

# Exempel på användning:
# @handle_exceptions(default_return=None)
# def some_function():
#     ...