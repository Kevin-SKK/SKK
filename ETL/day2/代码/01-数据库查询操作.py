import pymysql

# 1. 建立链接(桥)
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='chuanzhi',
    charset='utf8',
    autocommit=False
)
# 选择数据库
conn.select_db("zhengzhou")
# 2. 创建游标(小弟)
# 游标: 记录数据读取位置
cur = conn.cursor()
# 3. 游标执行sql语句
sql = "select * from goods;"
# 小弟执行slq
cur.execute(sql)
# 4. 获取查询到的数据(卸货)
# fetchall(): 获取所有的数据
# data类型 ==> ((),(),())
data = cur.fetchall()
for i in data:
    # i:是一个元组 同时是一条数据
    print(i)


# 5. 关闭
cur.close()
conn.close()
