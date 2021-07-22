"""FILE HANDLER"""
import csv
import logging

from src.file_handler.constants import FILE_READ_MODE, FILE_WRITE_MODE

logger = logging.getLogger(__name__)


class ProcessFile:
    """
    PROCESS FILE
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def read_file(self):
        """
        READ FILE
        :return: {str} File Buffer
        """
        logger.info(f'READING FILE FROM FILEPATH: {self.filepath}')
        try:
            with open(file=self.filepath, mode=FILE_READ_MODE) as f:
                return f.read()
        except FileNotFoundError as fne:
            logger.error(f'Please check the file path: {self.filepath}\n{fne}')  # KNOWN EXCEPTIONS WITH OUT TRACEBACK
        except Exception as ex:
            logger.exception(ex)
        return False

    def write_file(self, data: str):
        """
        WRITE FILE - UNUSED FUNCTION - CAN BE USED FOR OTHER APPROACHES THAN USING csv MODULE
        :param: data {str} Data to write to file
        :return: {str} File Buffer
        """
        logger.info(f'READING FILE FROM FILEPATH: {self.filepath}')
        try:
            with open(file=self.filepath, mode=FILE_WRITE_MODE) as f:
                return f.write(data)
        except FileNotFoundError as fne:
            logger.error(f'Please chek the file path: {self.filepath}\n{fne}')  # KNOWN EXCEPTIONS WITH OUT TRACEBACK
        except Exception as ex:
            logger.exception(ex)
        return False

    def write_to_csv(self, header: list, data: list, encoding: str = 'UTF-8', newline: str = '') -> bool:
        """
        WRITE TO CSV
        :param header: {list} Header List
        :param data: {list[list]} Data List of Lists
        :param encoding: {str} Data Encoding
        :param newline: {str} New Line
        :return: {bool} True if Successful else False
        """
        logger.debug(f'DATA HEADER: {header}')
        logger.debug(f'DATA: {data}')
        try:
            with open(file=self.filepath, mode=FILE_WRITE_MODE, encoding=encoding, newline=newline) as f:
                writer = csv.writer(f)
                writer.writerow(header)  # WRITE THE HEADER
                writer.writerows(data)  # WRITE MULTIPLE ROWS
            return True
        except Exception as e:
            logger.exception(e)
        return False
