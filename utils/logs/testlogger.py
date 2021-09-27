# -*- coding: UTF-8 -*-
import logging
from GLOBALS import *


class Style:

    def __init__(self):
        pass

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BOLD = '\033[1m'

    RESET = '\033[0m'


class Logger:

    # LOG_FILE = '../utils/logs/testlogs.log'
    logger = logging.getLogger(LOG_FILE)
    ch = logging.StreamHandler()
    fh = logging.FileHandler(LOG_FILE)

    def __init__(self):
        self.logger.setLevel(logging.INFO)
        self.ch.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to ch
        self.ch.setFormatter(formatter)
        self.fh.setLevel(logging.INFO)
        self.fh.setFormatter(formatter)

        # add ch to logs
        self.logger.addHandler(self.ch)
        self.logger.addHandler(self.fh)

    def get_logger(self):
        return self.logger


def info(logger, message):
    logger.info(message)


def error(logger, message):
    logger.error(Style.BOLD + Style.YELLOW + message + Style.RESET)
