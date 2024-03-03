import logging
import os
from datetime import datetime

# Create log file name using current timestamp
# Ensures unique log file name
LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Determine log path folder and create if needed
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE) 
os.makedirs(logs_path,exist_ok=True)

# Create full log file path 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    # Log to defined log file
    filename=LOG_FILE_PATH,

    # Format log message to include:
    # - Timestamp , Line number , Module name , Log level , Log message
    format=" [ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",

    # Log level - log all info level msgs and above
    level=logging.INFO,
        
)

# Usage:

# logging.debug("This is a debug message") 
# logging.info("This info msg will be logged")  
# logging.error("This error msg will also be logged")