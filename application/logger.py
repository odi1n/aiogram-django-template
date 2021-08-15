import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import datetime as dt

import os
from pathlib import Path

path_script = Path(__file__).parents[0]
_log_file = os.path.join(path_script, 'log')

_log_format = f"%(asctime)s - [%(levelname)s] - [%(threadName)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    # logger.addHandler(_handler_timed_rotation_file())
    # logger.addHandler(_handler_rotating_handler())
    logger.addHandler(_handler_timed_rotation_file())
    logger.addHandler(_handler_stream())
    return logger


def _handler_rotating_handler():
    my_handler = RotatingFileHandler(_log_file,
                                     mode='a',
                                     maxBytes=5 * 1024 * 1024,
                                     backupCount=5,
                                     encoding=None,
                                     delay=0)
    my_handler.setFormatter(logging.Formatter(_log_format))
    return my_handler


def _handler_timed_rotation_file():
    my_handler = TimedRotatingFileHandler(
        filename=os.path.join(_log_file, dt.datetime.now().strftime("%Y-%m-%d") + ".log"),
        when='H',
        interval=2,
        backupCount=5)
    my_handler.setFormatter(logging.Formatter(_log_format))
    return my_handler


def _handler_file():
    file_handler = logging.FileHandler(os.path.join(_log_file, "log_file.log"))
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def _handler_stream():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


log = get_logger(__name__)
