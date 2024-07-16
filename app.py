import atexit
import logging.config
import yaml
import logging
from helper import show_logging_form_diff_module
import sys


# Load the config file
with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Get a logger object
logger = logging.getLogger(__name__)

# For the following part of code check readme multi-threaded/process part 
# Start the queue listener if Pyhon 3.12 or later
if sys.version_info >= (3, 12):
    queue_handler = logging.getHandlerByName('queue_handler')
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
else:
    logger.warning('.getHandlerByName is not available in this version of Python')

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message', extra={'x': 'hello'}) # extra context works only with json handler
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
logger.warning('This is a debug message with a password=12345')
try:
    1 / 0
except ZeroDivisionError:
    logger.exception('This is an exception message')

show_logging_form_diff_module()
