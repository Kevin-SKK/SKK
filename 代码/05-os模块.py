import os

# listdir可以获取指定路径下的所有的文件/文件夹的名字 以列表的形式进行存储
ret1 = os.listdir("/Users/xiechen/Desktop/郑州303/day01/代码/01_josn数据")
print(ret1)
# 获取当前的工作路径
ret2 = os.getcwd()
print(ret2)
# 获取文件名
ret3 = os.path.basename("/Users/xiechen/Desktop/郑州303/day01/代码/01_josn数据/x00")
print(ret3)