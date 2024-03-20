import logging
from helper import show_logging_form_diff_module
from logger_config import SensitiveDataFilter, PasswordFilter, MyJSONFormatter
from logging import Formatter


# Get a logger object
logger = logging.getLogger(__name__)
# logger.addFilter(SensitiveDataFilter())

root_logger = logging.getLogger()
root_logger.addFilter(SensitiveDataFilter())


# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message', extra={'x': 'hello'}) # extra context works only with json handler
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
logger.warning('This is a warning message with a password=12345')
try:
    1 / 0
except ZeroDivisionError:
    logger.exception('This is an exception message')

show_logging_form_diff_module()