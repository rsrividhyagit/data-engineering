"""LOGGER"""

import os
import pathlib
from logging.config import dictConfig

# Setting up logging DEFAULT LOG
PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent.resolve()
LOG_DIR = os.path.join(PROJECT_ROOT, 'log')

LOG_FILE_NAME = 'data_engineering.log'
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)
print(LOG_FILE_PATH)

FORMAT = '%(asctime)s [{application}] [%(thread)d] [%(levelname)-4s] [%(name)s] [file=%(filename)s:%(lineno)d] ' \
         '%(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def setup_logging(application_name, level="INFO", fmt=FORMAT, file_logging=False):
    """
    LOGGING SETUP
    :param application_name: {str} Application Name
    :param level: {str} LOG Level
    :param fmt: {str} Log Format
    :param file_logging: {bool} True if File Logging is Enabled else False
    :return:
    """
    if not os.path.exists(LOG_DIR) and file_logging:
        os.makedirs(LOG_DIR)

    formatted_log = fmt.format(application=application_name)

    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': formatted_log,
                'datefmt': DATE_FORMAT
            }
        },
        'handlers': {
            'default': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': level,
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': 'midnight',
                'utc': True,
                'backupCount': 5,
                'level': level,
                'filename': LOG_FILE_PATH,
                'formatter': 'standard',
            }
        },
        'loggers': {
            '': {
                'handlers': ['default', 'file'] if file_logging else ['default'],
                'level': level
            }
        }
    }
    if not file_logging:
        config['handlers'].pop('file')

    dictConfig(config)
