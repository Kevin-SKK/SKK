# 需求一的所有的业务代码
from util.logging_util import init_my_logger
from util.file_util import get_file_name
from config import project_config as conf

# todo 开启日志功能
logger = init_my_logger()
logger.info("~~~~~日志开启成功~~~~~")

# todo 获取需要处理的json文件的绝对路径
json_file_names = get_file_name(conf.json_file_root_path)
logger.info(f"获取到了需要处理的文件的名字{json_file_names}")


