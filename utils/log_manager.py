import logging
import sys
from logging.handlers import RotatingFileHandler

class LogManager:
    @staticmethod
    def configure_logging(log_file="app.log", log_level=logging.INFO, max_bytes=10485760, backup_count=5):
        """
        Konfigurerar loggning för applikationen.
        
        :param log_file: Filnamnet för loggfilen.
        :param log_level: Loggnivå (t.ex. logging.INFO, logging.DEBUG).
        :param max_bytes: Maximal storlek för loggfilen i bytes.
        :param backup_count: Antal backupfiler att hålla.
        """
        # Formatter för loggmeddelanden
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Loggning till fil med rotation
        file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)

        # Loggning till konsol
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(log_level)

        # Grundläggande loggkonfiguration
        logging.basicConfig(level=log_level, handlers=[file_handler, console_handler])

        # Stäng av loggning från externa bibliotek som kan vara för bullriga
        logging.getLogger('some_external_library').setLevel(logging.WARNING)

# Exempel på användning:
# LogManager.configure_logging(log_file="myapp.log", log_level=logging.DEBUG)