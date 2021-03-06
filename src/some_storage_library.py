"""
__author__: Joshua Schlichting
* Modified - Added logger
"""
import logging
import os
import pathlib
import shutil

logger = logging.getLogger(__name__)

project_root = pathlib.Path(__file__).parent.parent.resolve()
destination = os.path.join(project_root, 'data', 'destination')


class SomeStorageLibrary:

    def __init__(self) -> None:
        logger.info('Instantiating storage library...')
        if not os.path.isdir(destination):
            os.mkdir(destination)

    def load_csv(self, filename: str) -> None:
        logger.info(f'Loading the following file to storage medium: {filename}')
        shutil.move(filename, destination)
        logger.info('Load completed!')
