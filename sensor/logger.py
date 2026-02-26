import logging
import os
import sys

from datetime import datetime

# 1. Generate timestamp in the format: MM_DD_YYYY_HH_MM_SS
# This matches your request: 01_12_2026_11_11_39
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create the logs directory
LOG_FILE_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_FILE_DIR, exist_ok=True)

# 3. Create the full file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)

# 4. Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

'''
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.getLogger().info("Logger initialized")
'''
'''
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH= os.path.join(logs_path,LOG_FILE)



logging.basicConfig(
filename =LOG_FILE_PATH,
format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
level= logging.INFO,
)

'''



