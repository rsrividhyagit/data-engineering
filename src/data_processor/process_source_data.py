"""PROCESS SOURCE DATA"""
import logging
import os
import pathlib
from datetime import datetime

from src.constants import SOURCE_DATA_COLUMNS_TXT, SOURCE_DATA_TXT, DEFAULT_DELIMITER, SOURCE_DATA_PROCESSED, \
    CSV_EXTENSION, FILE_NAME_TIMESTAMP_FORMAT
from src.file_handler.file_handler import ProcessFile
from src.some_storage_library import SomeStorageLibrary
from src.utils.util import convert_string_to_int

logger = logging.getLogger(__name__)

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent.resolve()
SOURCE_FILES_PATH = os.path.join(PROJECT_ROOT, 'data', 'source')


class ProcessSourceData:
    """
    PROCESS SOURCE DATA
    """

    def __init__(self, source_files_path: str = SOURCE_FILES_PATH, files: tuple = (SOURCE_DATA_COLUMNS_TXT,
                                                                                   SOURCE_DATA_TXT)):
        self.source_files_path = source_files_path
        self.files = files

    def extract_columns_data_convert_to_dict(self, delimiter: str = DEFAULT_DELIMITER):
        """
        EXTRACT COLUMNS DATA CONVERT TO DICT
        :param delimiter: {str} Delimiter
        :return: {dict} Data Dictionary
        """
        data_dict = {}
        file_processor = ProcessFile(filepath=os.path.join(self.source_files_path, self.files[0]))
        data = file_processor.read_file()
        for line in data.split('\n'):
            values = line.split(delimiter)
            data_dict.update({convert_string_to_int(values[0]): values[1].strip('\n')})
        return data_dict

    @staticmethod
    def sort_by_id_rtn_column_headers(data_dict: dict):
        """

        :param data_dict:
        :return:
        """
        logger.info(f'SOURCE COLUMNS DATA: {data_dict}')
        response = dict(sorted(data_dict.items(), key=lambda kv: kv[0])).values()
        logger.info(response)
        return list(response)

    def get_sorted_columns(self):
        """

        :return:
        """
        return self.sort_by_id_rtn_column_headers(self.extract_columns_data_convert_to_dict())

    def get_sorted_data(self):
        """

        :return:
        """
        order_id_index = 0
        data_list = []
        file_processor = ProcessFile(filepath=os.path.join(self.source_files_path, self.files[1]))
        data = file_processor.read_file()
        for line in data.split('\n'):
            data_list.append(line.split('|'))
        return sorted(data_list, key=lambda x: int(x[order_id_index]))

    def get_output_file_name(self):
        """

        :return:
        """
        now = datetime.strftime(datetime.now(), FILE_NAME_TIMESTAMP_FORMAT)
        return os.path.join(self.source_files_path, f'{SOURCE_DATA_PROCESSED}_{now}{CSV_EXTENSION}')

    def process_data(self):
        """

        :return:
        """
        try:

            # PROCESS HEADER
            header = self.get_sorted_columns()
            # PROCESS DATA
            data = self.get_sorted_data()

            # Get Output File Name with timestamp to handle Already Exist.
            csv_file_path = self.get_output_file_name()

            # WRITE TO CSV
            ProcessFile(filepath=csv_file_path).write_to_csv(header=header, data=data)

            # STORAGE LIBRARY MOVE
            SomeStorageLibrary().load_csv(filename=csv_file_path)
        except Exception as e:
            logger.exception(e)
            raise e
        return True
