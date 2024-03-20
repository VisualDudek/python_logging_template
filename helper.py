import logging

logger = logging.getLogger(__name__)

def show_logging_form_diff_module():
    logger.warning('This is a warning message form helper module')
    logger.debug('This is a debug message form helper module')