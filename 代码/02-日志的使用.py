import logging


def log_to_stream():
    """
    这个方法是为了把日志显示到控制台中的
    :return: None
    """

    # 1. 日志对象
    logger = logging.getLogger()
    # 2. handler对象 控制日志输出为 控制台/文件
    stream_handler = logging.StreamHandler()
    # 3. fmt对象 控制具体的输出格式
    # %(asctime)s : 当前时间
    # %(levelname)s : 日志级别
    # %(filename)s : 文件名
    # %(lineno)d : 行号
    # %(message)s : 日志具体信息
    fmt = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
    )
    # 4. 日志格式设置(通过格式对象 确定日志具体的输出样式)
    stream_handler.setFormatter(fmt)
    # 5. 设置日志到日是 控制台/文件
    logger.addHandler(stream_handler)
    # 日志级别如果不设置默认就是error
    # 设置日志级别
    logger.setLevel(20)
    # 具体的日志输出
    logger.debug("this is debug")
    logger.info("this is info")
    logger.error("this is error")


def log_to_file():
    """
    这个函数是把日志信息输出到文件中
    :return:None
    """
    # 1.日志对象
    logger = logging.getLogger()
    # 2.handler对象
    file_handler = logging.FileHandler(
        filename="/Users/xiechen/Desktop/郑州303/day01/代码/logs/a.log",
        mode="a",
        encoding="utf8"
    )
    # 3.格式对象
    fmt = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
    )
    # 4. 添加格式对象
    file_handler.setFormatter(fmt)
    # 5. 添加handler
    logger.addHandler(file_handler)
    # 6. 设置日志级别
    logger.setLevel(20)
    # 日志输出
    logger.info("this is info")
    logger.error("this is error")


if __name__ == '__main__':
    # log_to_stream()
    log_to_file()
