# 今日目标: 面向对象基本概念

<font size='6' color='red'>类,对象,属性,方法,魔法方法</font>



## 1.理解面向对象思想

- 面向过程思想: 遇到问题,分析步骤.按照步骤解决问题.(复杂,重复)
- 面向对象思想: 遇到问题,找到能解决问题的对象去解决.(简单,复用)



## 2.类和对象

```python
# 定义类的格式:
# class 类名():
#     代码
#     ......
class Student():

    def study(self):
        print('学生好好学习')

    def eat(self):
        print('学生大鱼大肉,好好吃.')

if __name__ == '__main__':
    #创建对象格式:
    # 对象名 = 类名()
    xiaoming = Student()

    #使用对象的格式:
    #对象名.函数名()
    xiaoming.eat()
    xiaoming.study()
```



## 3.self关键字

```python
# self指的是调用该函数的对象
# 调用函数我们不需要给self传参.因为python解释器会把调用者当成参数传递给self
class Student():

    def study(self):
        print('学生好好学习')

    # 谁来调用eat()-- self就是谁.
    def eat(self):
        print(self)#<__main__.Student object at 0x00000240B39B8460>
        print(id(self))#2476914476128
        print('学生大鱼大肉,好好吃.')

if __name__ == '__main__':

    xiaoming = Student()
    print(xiaoming) #<__main__.Student object at 0x00000240B39B8460>
    print(id(xiaoming)) #2476914476128  -- id()函数时对内存地址的封装.
    xiaoming.eat()

    print("*"*30)
    laowang = Student()
    print(laowang)
```



## 4.添加和获取属性

- 类的外部 操作 属性

```python
# 类的外部可以给类添加属性.
class Student():

    def study(self):
        print('学生好好学习')

    # 谁来调用eat()-- self就是谁.
    def eat(self):
        print('学生大鱼大肉,好好吃.')

if __name__ == '__main__':
    s1 = Student()
    # 类的外部>>>添加属性
    #格式:  对象名.属性名 = 值
    s1.name = 'tom'
    print(s1.name)

    s1.age = 19
    print(s1.age)

    s2 = Student()
   # 类以外的属性.定义后方能使用.
   # print(s2.name)#AttributeError: 'Student' object has no attribute 'name'
```

- 类的内部添加属性

```python
class Student():

    ### add_name虽然可以在类的内部给学生对象添加实行.但是.容易忘记调用.必须自己手工调用.!!!
    def add_name(self):
        # 在类的内部--添加属性
        self.name = "小明"

    def study(self):
        #在类的内部--获取属性名
        print(f'{self.name}:在认真学习')

if __name__ == '__main__':
    s1 = Student()
    s1.add_name()# 在类的内部给对象添加了一个name属性.

    print(s1.name)#小明
    s1.study()
```



## 5.魔法方法init()

```python
class Student():

    #__init__()方法，在创建对象时默认被调用，不需要手动调用
    def __init__(self,name,age,sex):
        # 在类的内部--添加属性
        print('__init__')
        #self.name是给对象添加属性name, = name是参数name的值赋值给=左边的变量.
        self.name = name
        self.age = age
        self.sex = sex

    def study(self):
        #在类的内部--获取属性名
        print(f'{self.name}:在认真学习')

if __name__ == '__main__':
    s1 = Student('小明',19,'男')

    print(s1.name)#小明
    print(s1.age)#小明
    print(s1.sex)#小明
    s1.study()
```

## 6.对象内存图[扩展]

![image-20230503120436238](day06课堂笔记.assets/image-20230503120436238.png)

## 7.魔法方法__str()

```python
"""
汽车类:
    属性:
        颜色-color:
        品牌-brand:
        价格-price:
    行为:
        run()
        stop()
        speed()
"""

class Car():
    #属性:
    def __init__(self,color,brand,price):
        self.color = color
        self.brand = brand
        self.price = price
    #行为:
    def run(self):
        print("汽车在飞驰")

    def stop(self):
        print('刹车要及时')

    def speed(self):
        print('超车要加速')

    #魔法行为
    def __str__(self):
        return f"{self.color}的{self.brand}售价{self.price}"

if __name__ == '__main__':
    c = Car('红色','法拉利',199900)
    # 默认情况下.打印一个对象,打印的就是该对象的地址值.
    print(c)#<__main__.Car object at 0x000001DC37EF65E0>

    #python定义的列表类.它的对象就不打印地址值.而是打印元素.
    my_list = [1,2,3]
    print(my_list)#[1, 2, 3]

    # 我想打印汽车对象的时候.打印汽车的信息.
    C2 = Car('黑色',"BYD",290000) #黑色的BYD售价290000
    print(C2)
```



## 8.魔法方法__repr()[扩展]

```python
class Car():
    #属性:
    def __init__(self,color,brand,price):
        self.color = color
        self.brand = brand
        self.price = price
    #行为:
    def run(self):
        print("汽车在飞驰")

    def stop(self):
        print('刹车要及时')

    def speed(self):
        print('超车要加速')

    #魔法行为
    def __str__(self):
        return f"{self.color}的{self.brand}售价{self.price}"

    #魔法方法__repr__
    def __repr__(self):
        return f"{self.color}的,{self.brand},售价:{self.price}"


if __name__ == '__main__':
    #制造3辆汽车
    c1 = Car('红色','法拉利',1990000)
    c2 = Car('黑色','BYD',290000)
    c3 = Car('白色','WULING',29000)

    #打包发货
    cars = [c1,c2,c3]

    #发货前检查--失败:
    # "[<__main__.Car object at 0x000001DB2A918460>,
    # <__main__.Car object at 0x000001DB2A9569A0>,
    # <__main__.Car object at 0x000001DB2A9D85B0>]"
    print(cars)

    #定义 __repe__之后:
    #[红色的,法拉利,售价:1990000, 黑色的,BYD,售价:290000, 白色的,WULING,售价:29000]
```



## 9.魔法方法__del()

```python
class Car():
    #属性:
    def __init__(self,color,brand,price):
        self.color = color
        self.brand = brand
        self.price = price
    #行为:
    def run(self):
        print("汽车在飞驰")

    def stop(self):
        print('刹车要及时')

    def speed(self):
        print('超车要加速')

    # 魔法行为
    def __str__(self):
        return f"{self.color}的{self.brand}售价{self.price}"

    def __del__(self):
        print(f'被删除的对象是{self}')

if __name__ == '__main__':
    #创建对象
    c1 = Car('红色','法拉利',1990000)

    # 删除对象
    del c1 # 被删除的对象是红色的法拉利售价1990000
```





## 10.面向对象方式创建容器对象[扩展]

- 字面值创建
  - 列表: list1 = [1,2,3]    
  - 字典: dict1 = {'name':'tom',"age":20}
  - 元组: tuple1 = (1,2,3)
  - 集合: set1 = {1,2,3}
- 面向对象
  - 容器类型( [容器] )
  - 此方式可以实现不同容器之间的转换.

```python
#字面值方式: (1,2,3)
tuple1 = (1,2,3)
print(type(tuple1),tuple1)

# 面向对象方式
tuple2 = tuple()
print(type(tuple2),tuple2)

list1 = list()
list1.append(123)
list1.append('hello')
print(type(list1),list1)

# 使用面向对象方式.可以对数据进行转换.
tuple3 = tuple(list1)
print(tuple3)

list2 = list("12323")
print(list2)

#集合可以自动去除重复--存取无序
set1 = set(list2)
print(set1)
```

## 11.面向对象案例1

```python
# 地瓜的属性
#     被烤的时间
#     地瓜的状态
#     添加的调料
# 地瓜的方法
#     被烤
#         用户根据意愿设定每次烤地瓜的时间
#         判断地瓜被烤的总时间是在哪个区间，修改地瓜状态
#     添加调料
#         用户根据意愿设定添加的调料
#         将用户添加的调料存储
# 显示对象信息
class Sweetpotato():

    def __init__(self):
        '''
        对象属性初始化:
        :param time: 被烤时间  0
        :param state: 当前状态   '生的'
        :param flavour: 已将撒上的调料 []
        '''
        self.time = 0
        self.state = '生的'
        self.flavour = []

    #烤地瓜方法
    def cooking(self,time):
        self.time += time
        if 0 <= self.time < 3:
            self.state = '生的'
        elif 3 <= self.time < 5:
            self.state = '半生不熟'
        elif 5 <= self.time < 8:
            self.state = '熟了'
        elif self.time >= 8:
            self.state = '烤糊了'

    def add_flavour(self,flavour):
        #添加用户撒入的调料
        self.flavour.append(flavour)

    def __str__(self):
        return f'地瓜已经被烤{self.time}分钟,当前状态{self.state},已撒上调料{self.flavour}'

if __name__ == '__main__':
    s1 = Sweetpotato()# 创建地瓜
    print(s1)

    s1.cooking(7)# 调用地瓜的被烤方法

    s1.add_flavour('孜然')
    s1.add_flavour('辣椒')
    s1.add_flavour('食盐')

    print(s1)#地瓜已经被烤7分钟,当前状态熟了,已撒上调料['孜然', '辣椒', '食盐']
```





## 12.面向对象案例 2 

```python
# 房子类
#     实例属性
#         房子地理位置
#         房子占地面积
#         房子剩余面积
#         房子内家具列表
#     实例方法
#         容纳家具
#     显示房屋信息
# 家具类
#     家具名称
#     家具占地面积
class Furniture:
    def __init__(self,name,area):
        self.name = name# 家具名称
        self.area = area# 家具占地面积

    def __str__(self):
        return f"名称:{self.name},占地面积{self.area}"

    def __repr__(self):
        return f"名称:{self.name},占地面积{self.area}"


class House:
    def __init__(self,address,area):
        self.address = address# 房子位置
        self.area = area#房子的大小面积
        self.free_area = area #新家剩余面积等于房间总面积
        self.furnitures = [] # 新家默认没有家具

    def add_furniture(self,furniture):
        # 先判断-后添加
        if self.free_area >= furniture.area:
            self.furnitures.append(furniture)
            #添加了新家具.剩余面积要减少
            self.free_area -= furniture.area
        else:
            print('房子太小,赶紧换别墅吧.')

    def __str__(self):
        return f"房子位置:{self.address},房子面积:{self.area},房子剩余面积:" \
               f"{self.free_area},房子里面的家具{self.furnitures}"

if __name__ == '__main__':
    #创建2个家具
   shafa =  Furniture('头等舱',1.2)
   chuang =  Furniture('席梦思',4.5)

    #购买一套房子
   home = House('长春路1号院3#901',128)

   #把家具搬进家里
   home.add_furniture(shafa)
   home.add_furniture(chuang)

   # 参观新房
   print(home)
```







