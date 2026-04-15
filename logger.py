import sys
import os
from datetime import datetime
import re

class Logger:
    def __init__(self, filename="data/system_logs.txt"):

        log_dir = os.path.dirname(filename)
        

        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir) 
            
        self.terminal = sys.stdout

        self.log = open(filename, "a", encoding="utf-8")

    def remove_colors(self, text):

        return re.sub(r'\x1b\[[0-9;]*m', '', text)

    def write(self, message):

        self.terminal.write(message)


        if message.strip() != "":
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            clean_message = self.remove_colors(message)

            if not clean_message.endswith("\n"):
                clean_message += "\n"

            log_message = f"[{timestamp}] {clean_message}"
            self.log.write(log_message)
            self.log.flush() 

    def flush(self):
        self.terminal.flush()
        self.log.flush()

def start_logging():

    if not isinstance(sys.stdout, Logger):
        sys.stdout = Logger() #
