import os
import json
import logging
import sys
from pythonjsonlogger import jsonlogger

secrets_path_credentials = os.getenv("SECRETS_PATH_CREDENTIALS", "")

class StackdriverLogFormatter(jsonlogger.JsonFormatter, object):
    def __init__(self, fmt="%(levelname) %(message)", style="%", *args, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)

    def process_log_record(self, log_record):
        log_record["severity"] = log_record["levelname"]
        del log_record["levelname"]
        return super(StackdriverLogFormatter, self).process_log_record(log_record)

def setup_logging(logger, level=logging.INFO):
    log_handler = logging.StreamHandler(sys.stdout)
    formatter = StackdriverLogFormatter()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.setLevel(level)

def get_credentials(key: str):
    if not os.path.exists(secrets_path_credentials):
        return None

    with open(secrets_path_credentials, "r") as f:
        credentials = json.load(f)
    return credentials.get(key)

def process_adobe_data(adobe_data):
    """
    Process data received from Adobe API.
    Implement this function based on how you need to process the Adobe API data.
    """
    # Example processing (to be replaced with actual processing logic)
    processed_data = []
    for item in adobe_data:
        processed_item = {}  # Process each item
        processed_data.append(processed_item)
    return processed_data

def format_data_for_sheets(data):
    """
    Format the data for uploading to Google Sheets.
    This function should convert the data into a format that is suitable for Google Sheets.
    """
    # Example formatting (to be replaced with actual formatting logic)
    formatted_data = []
    for item in data:
        formatted_item = []  # Format each item as needed
        formatted_data.append(formatted_item)
    return formatted_data
