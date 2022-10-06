import logging
import const


def create_logger(name: str, form: str = const.MESSAGE_FORM) -> logging.Logger:
    """
    creates custom logger object
    :param name: name of the logger (convention to use __name__ when the function is called)
    :param form: shape of the logged messages
    :return: logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(form)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    file_handler = logging.FileHandler(const.LOGFILE_NAME)
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)

    return logger
