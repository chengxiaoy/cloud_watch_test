import os
import errno

import logging
from logging.handlers import RotatingFileHandler
from logging.config import dictConfig
import yaml

logger = logging.getLogger(__name__)


def mkdir_p(path):
    try:
        logger.warning(f"try to create path {path}")
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except Exception as e:
        logger.exception(f"an error occur: {e}")
        raise


class MakeFileHandler(RotatingFileHandler):
    def __init__(self, filename, **kwargs):
        mkdir_p(os.path.dirname(filename))
        RotatingFileHandler.__init__(self, filename, **kwargs)


def load_log_config():
    try:
        with open('log_config.yaml', 'r') as f:
            dictConfig(yaml.safe_load(f))
    except Exception as e:
        logger.exception(f"load log config yaml file error: {e}")
        logger.error(f"load log config yaml file error: {e}")
