import os
import errno

import logging
from logging.handlers import TimedRotatingFileHandler
from logging.config import dictConfig
import yaml
import json

logger = logging.getLogger(__name__)


def mkdir_p(path):
    try:
        logger.warning(f"try to create path {path}")
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except Exception as e:
        logger.exception(f"an error occur: {e}")
        raise


class MakeFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, **kwargs):
        mkdir_p(os.path.dirname(filename))
        TimedRotatingFileHandler.__init__(self, filename=filename, when="D", **kwargs)


class JsonFormatter(logging.Formatter):
    def format(self, record):
        # 创建一个字典来保存日志记录的信息
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "name": record.name,
            "levelname": record.levelname,
            "thread": record.thread,
            "threadName": record.threadName,
            "message": record.getMessage(),
            "lineno": record.lineno,
            "processId": record.process,
            "processName": record.processName,
        }

        # 添加其他字段，如异常信息等
        if record.exc_info:
            log_entry['exc_info'] = self.formatException(record.exc_info)

        if record.stack_info:
            log_entry['stack_info'] = self.formatStack(record.stack_info)

        return json.dumps(log_entry, ensure_ascii=False)


def load_log_config():
    try:
        with open('config/log_config.yaml', 'r') as f:
            dictConfig(yaml.safe_load(f))
    except Exception as e:
        logger.exception(f"load log config yaml file error: {e}")
        logger.error(f"load log config yaml file error: {e}")
