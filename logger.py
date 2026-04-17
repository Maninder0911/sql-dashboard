import logging
import os

LOG_FOLDER = "logs"
LOG_FILE = "organizer.log"

os.makedirs(LOG_FOLDER, exist_ok=True)

log_path = os.path.join(LOG_FOLDER, LOG_FILE)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)


def get_logger():
    return logging.getLogger()
