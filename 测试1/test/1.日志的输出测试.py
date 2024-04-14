import logging
logger = logging.getLogger()
stream_handle = logging.StreamHandler()
fmt = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(filename)s [%(lineno)d]: %(message)s"
)
stream_handle.setFormatter(fmt)
logger.addHandler(stream_handle)
logger.setLevel(20)
logger.info('999')
logger.error('eee')