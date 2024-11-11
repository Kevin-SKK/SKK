import json

# python_data = json.loads(json_data)
#
# sql = f"insert into xxx values({python_data['name']},{python_data['age']},{python_data['address']});"

json_data = """{"name":"张三", "age":11, "address": "北京市海淀区"}"""


class Model:
    def __init__(self, data):
        # data : 认为是json数据类型
        # self.data : python的数据类型
        data = json.loads(data)
        self.name = data["name"]
        self.age = data["age"]
        self.address = data["address"]

    def to_sql(self):
        sql = f"insert into xxx values('{self.name}',{self.age},'{self.address}');"
        return sql


a = Model(json_data)
print(a.to_sql())