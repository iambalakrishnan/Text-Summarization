import os
import sys
import logging
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m-%d_%Y_%H_%M_%S')}.log"
LOGS_DIR = f"{datetime.now().strftime('%m-%d_%Y_%H')}_HRS"
logs_path = os.path.join("artifacts","running_logs",LOGS_DIR)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s: %(lineno)d: %(name)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a",
)

logger = logging.getLogger("textSummarizerLogger")