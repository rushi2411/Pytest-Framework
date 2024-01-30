import logging
import os
import datetime


class LogGen:

    @staticmethod
    def loggen():
        timestamp = datetime.datetime.now()
        project_dir = os.getcwd()
        current_file = os.path.abspath(__file__)
        file_name = os.path.basename(current_file).split('.')[0]
        log_file = os.path.join(project_dir, "logs", "log.log")

        logger = logging.getLogger('myLogger')
        logger.setLevel(logging.DEBUG)

        # create handler
        console = logging.StreamHandler()
        file_handler = logging.FileHandler(log_file)

        #create formatter
        formatter = logging.Formatter("%(filename)s %(asctime)s %(levelname)s %(name)s: %(lineno)d %(message)s")

        console.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console)
        logger.addHandler(file_handler)

        return logger



