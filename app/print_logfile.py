import logging
import time
import random
from log_utils import load_log_config

load_log_config()

logger = logging.getLogger(__name__)


def raise_exception_method():
    try:
        1 / 0
    except Exception as e:
        raise ValueError("zero can't be divided") from e


def log():
    random_int = random.Random().randint(1, 10)
    logger.debug('This message should go to the log file')
    logger.debug(f'test f-str {random_int}')
    logger.debug('This message should go to \n the log file')
    logger.info('So should this')
    logger.info('So \n should \n this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
    try:
        raise_exception_method()
    except Exception as e:
        logger.exception(f"Exception: an error occur: {e}")
        logger.exception(f"Error: an error occur: {e}")


if __name__ == '__main__':
    while True:
        interval_time_seconds = random.Random().randint(1, 5)
        time.sleep(interval_time_seconds)
        log()
