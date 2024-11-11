import pymysql
# 创建链接
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
# 创建游标
cur = conn.cursor()
# 执行sql
sql = "update goods set cate_name='yyy' where id=1;"
cur.execute(sql)
# 修改后进行查询
sql = "select * from goods;"
cur.execute(sql)
# 获取数据(卸货)
# 数据类型: ((),(),())
for i in cur.fetchall():
    print(i)
# 手动数据提交
conn.commit()
# 关闭连接
cur.close()
conn.close()
