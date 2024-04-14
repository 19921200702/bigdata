import logging
from 测试1.config import project_config as conf
class Logging:
    def __init__(self,level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
def init_logger():
    logger = Logging().logger
    if logger.handlers:
        return logger
    file_handler = logging.FileHandler(
        filename=conf.log_root_path + conf.log_name,
        mode='a',
        encoding='UTF-8'
    )
    fmt = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(filename)s [%(lineno)d]: %(message)s"
    )
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)
    return logger
init_logger().info('测试info')
init_logger().error('测试error')