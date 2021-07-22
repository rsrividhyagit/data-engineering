"""UTILS"""
import logging

logger = logging.getLogger(__name__)


def convert_string_to_int(string):
    """

    :param string:
    :return:
    """
    if isinstance(string, int):
        return string  # RETURNS WITH OUT TRYING TO CONVERT TO INT TO DEMONSTRATE FASTER RESPONSE TIMES.
    try:
        return int(string)
    except Exception as ce:
        logger.exception(ce)
    return string
