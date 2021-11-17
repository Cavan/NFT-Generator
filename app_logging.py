import logging
import os as os
from datetime import datetime



currentDate = datetime.today().strftime('%Y-%m-%d')
cwd = os.getcwd()
FILENAME ="%s/appLogs/app_%s.log"%(cwd, currentDate)
logging.basicConfig(filename=FILENAME, filemode='a',level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class AppLogger():

    def __init__(self):
        pass

    def log_info(self, info_message):
        try:
            logging.info(info_message)
            return True
        except:
            return False

    def log_warnings(self, warn_message):
        try:
            logging.warning(warn_message)
            return True
        except:
            return False

    def log_errors(self, err_message):
        try:
            logging.error(err_message, exc_info=True)
            return True
        except:
            return False

    def log_exceptions(self, exec_message):
        try:
            logging.exception(exec_message)
            return True
        except:
            return False

