# 写我们的整个项目的所有的配置信息
import time

# ###### json_server相关的配置信息 #####
log_file_root_path = "/Users/xiechen/Desktop/郑州303/day02/代码/logs"  # 日志路径
log_name = f'py_etl_{time.strftime("%Y_%m_%d_%H", time.localtime(time.time()))}.log'  # 日志文件名
json_file_root_path = "/Users/xiechen/Desktop/郑州303/day02/代码/01_josn数据"  # json文件所在的路径
# ############# mysql数据库配置选项 ##################
host = "127.0.0.1"
port = 3306
user = 'root'
passwd = 'chuanzhi'
charset = "utf8"
autocommit = False
# #############--mysql数据库配置选项--##################
metadata_host = "127.0.0.1"
metadata_port = 3306
metadata_user = 'root'
metadata_passwd = 'chuanzhi'
metadata_charset = "utf8"
# #############--元数据库配置选项--##################
metadata_db_name = "metadata"
metadata_file_check_table_name = "file_check"
metadata_file_check_create_cols = """
            id INT PRIMARY KEY AUTO_INCREMENT, 
            file_name VARCHAR(255) UNIQUE NOT NULL COMMENT '被处理的文件名称', 
            process_lines INT COMMENT '本文件中有多少条数据被处理', 
            process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '处理时间'
             """

