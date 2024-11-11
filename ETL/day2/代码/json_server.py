# 需求一的所有的业务代码
from util.logging_util import init_my_logger
from util.file_util import get_file_name, get_need_process_file_name
from config import project_config as conf
from util.mysql_util import MySqlUtil, get_processed_file_list
from model.json_model import OrdersModel

# todo 开启日志功能
logger = init_my_logger()
logger.info("~~~~~日志开启成功~~~~~")

# todo 获取需要处理的json文件的绝对路径
json_file_names = get_file_name(conf.json_file_root_path)
logger.info(f"获取到了需要处理的文件的名字{json_file_names}")

# todo 从metadata数据库中获取处理过的json文件的名字
# 创建数据库对象
db_util = MySqlUtil()
# 获取处理过的文件列表
processed_file_list = get_processed_file_list(
    db_util,
    conf.metadata_db_name,
    conf.metadata_file_check_table_name,
    conf.metadata_file_check_create_cols
)

# todo 获取需要处理的json文件名字
need_process_file_list = get_need_process_file_name(json_file_names, processed_file_list)
print(need_process_file_list)

# todo 处理json文件
# 希望能够让文件中的所有的数据 ==> 插入到数据库中的sql语句
for path in need_process_file_list:
    # path ==> 需要处理的文件的绝对路径
    # path ==> /Users/xiechen/Desktop/郑州303/day02/代码/01_josn数据/x00
    for line in open(path, "r", encoding="utf8"):
        a = OrdersModel(line)
        print(a.order_id)
