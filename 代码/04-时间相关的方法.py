import time
# 获取当前时间戳
# 时间戳是从1970年01月01日开始计时
# 1970年01月01日 00:00:10 ==> 0000000010
# 10位级别的时间戳/13位级别的时间戳
time_01 = time.time()
print(time_01)
# 获取一个时间对象
time_02 = time.localtime(time_01)
print(time_02)
# 转化为具体时间
# %Y: 年
# %m: 月
# %d: 日
# %H: 时
# %M: 分
# %S: 秒
# 参数1: 时间格式 %Y_%m_%d_%H_%M
time_03 = time.strftime("%Y_%m_%d_%H_%M", time_02)
print(time_03)

time.strftime("%Y_%m_%d_%H_%M", time.localtime(time.time()))
