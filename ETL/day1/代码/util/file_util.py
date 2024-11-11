import os


# 获取所有的需要处理的json文件的绝对路径
def get_file_name(path="./"):
    """
    返回指定路径下的所有文件的绝对路径
    :param path: 指定路径
    :return: 列表[所有的文件的绝对路径]
    """
    # 获取所有的指定路径下的文件的名字
    file_names = os.listdir(path)
    # 存储所有的文件的绝对路径
    absolute_path_names = []
    # 获取绝对路径
    for name in file_names:
        # path ==> /Users/xiechen/Desktop/郑州303/day01/代码/01_josn数据
        # name ==> 'x01', 'x00', 'x02'
        absolute_path = f"{path}/{name}"
        absolute_path_names.append(absolute_path)

    return absolute_path_names
