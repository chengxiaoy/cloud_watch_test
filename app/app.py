from flask import Flask
from log_utils import load_log_config
import logging

app = Flask(__name__)

load_log_config()
logger = logging.getLogger(__name__)

logger_str_level_dict = {
    'CRITICAL': 50,
    'ERROR': 40,
    'WARNING': 30,
    'INFO': 20,
    'DEBUG': 10,
    'NOTSET': 0
}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/log/<level>/<message>")
def log_msg(level: str, message):
    logger.log(logger_str_level_dict[level.upper()], message)
    return "ok"


@app.route("/exception")
def trigger_exception():
    try:
        1 / 0
    except Exception as e:
        logger.exception(f"an error occur: {e}")
    return "ok"


if __name__ == '__main__':
    app.run("0.0.0.0", 8000)
