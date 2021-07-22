"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""
import logging
from src.log import log
from src.data_processor.process_source_data import ProcessSourceData

# SETUP LOGGING
log.setup_logging(application_name="data-engineering", level='INFO', file_logging=False)

logger = logging.getLogger(__name__)


def run():
    """
    RUN
    :return: None
    """
    try:
        ProcessSourceData().process_data()
    except Exception as e:
        logger.exception(e)
    logger.info('The ETL Process Completed...')


if __name__ == '__main__':
    """Entrypoint"""
    logger.info('Beginning the ETL process...')
    run()

