import psutil
import time
import threading
import logging
from utils.log_manager import LogManager

# Konfigurera loggning
LogManager.configure_logging(log_file="resource_monitor.log", log_level=logging.DEBUG)

class ResourceMonitor:
    def __init__(self, interval=1):
        """
        Initierar ResourceMonitor med ett specificerat intervall för övervakning.
        :param interval: Hur ofta resurser ska övervakas (i sekunder).
        """
        self.interval = interval
        self.monitoring = False
        self.thread = None

    def start(self):
        """
        Startar resursövervakningen i en separat tråd.
        """
        if not self.monitoring:
            self.monitoring = True
            self.thread = threading.Thread(target=self._monitor, daemon=True)
            self.thread.start()
            logging.info("Resursövervakning startad.")

    def stop(self):
        """
        Stoppar resursövervakningen.
        """
        if self.monitoring:
            self.monitoring = False
            if self.thread and self.thread.is_alive():
                self.thread.join()
            logging.info("Resursövervakning stoppad.")

    def _monitor(self):
        """
        Privat metod som övervakar resursanvändningen och loggar det kontinuerligt.
        """
        try:
            while self.monitoring:
                cpu_usage = psutil.cpu_percent(interval=None)
                memory_info = psutil.virtual_memory()
                logging.info(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_info.percent}%")
                time.sleep(self.interval)
        except Exception as e:
            logging.error(f"Fel vid resursövervakning: {e}")
            self.stop()

if __name__ == "__main__":
    monitor = ResourceMonitor(interval=2)
    monitor.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop()