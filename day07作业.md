# Python面向对象高级-作业

## 总结题

请使用xmind思维导图对本章节知识做个知识总结。



## 简答题

###  题目1(简答题)

#### 题干

请写出单继承与多继承的语法格式?

单：class 子类名(父类名):

多：class 子类名(父类名1，父类名2，···):

#### 考察知识点

- 单继承
- 多继承



###  题目2(简答题)

#### 题干

什么是方法重写，为什么要方法重写?

答：子类中出现与父类一模一样的方法时（返回值类型，方法名和参数列表都相同），会出现覆盖效果，也称为重写或者复写。声明不变，重新实现。

​	在方法重写时，如果子类需要引用父类中原有的方法，可以使用 super 关键字。当子类重写父类方法后，在子类对象使用该方法时，会执行子类中重写的方法。

#### 考察知识点

- 面向对象
- 方法重写



## 实操题

### 题目3（实操题）

#### 题干

1. 创建一个Animal（动物）基类，其中有一个run方法，输出`跑起来....`；
2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run()方法还有eat()方法；
   1. run方法输出 `跑起来....`
   2. eat 方法输出 `吃东西...`

#### 考察知识点

- 面向对象
- 继承

答：

```python
class Animal():
    def run(self):
        print("跑起来....")


class Horse(Animal):
    def eat(self):
        print('吃东西...')


if __name__ == '__main__':
    h = Horse()
    h.run()
    h.eat()
```

### 题目4（实操题）

#### 题干

1. 创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来....`

2. 创建一个Horse（马）类继承于动物类，Horse类中重写run方法，增加打印输出"`迈着矫健的步伐跑起来!!`"，同时实现eat方法, 输出 `吃东西...`

#### 考察知识点

- 单继承
- super关键字

答：

```python
class Animal():
    def run(self):
        print("跑起来....")


class Horse(Animal):
    def run(self):
        Animal.run(self)
        super().run()
        print('迈着矫健的步伐跑起来!!')

    def eat(self):
        print('吃东西...')


if __name__ == '__main__':
    h = Horse()
    h.run()
    h.eat()
```

### 题目5（实操题）

#### 题干

1. 创建一个动物(Animal)的基类，其中有一个run方法, 输出`跑起来....`
2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
   1. run方法输出 `跑起来....`
   2. eat 方法输出 `吃东西...`
3. 创建一个 SwiftHorse（千里马）类继承Horse类，初始化init方法name属性为千里马，同时针对吃东西，SwiftHorse类中重写eat方法，增加打印输出"`一天可以吃一担粮食...`"

#### 考察知识点

- 多层继承
- 面向对象

答：

```python
class Animal():
    def run(self):
        print("跑起来....")


class Horse(Animal):
    def run(self):
        print('跑起来....')

    def eat(self):
        print('吃东西...')


class SwiftHorse(Horse):
    def __init__(self):
        self.name = '千里马'

    def eat(self):
        print('一天可以吃一担粮食...')


if __name__ == '__main__':
    h = SwiftHorse()
    h.run()
    h.eat()
```

### ==[可选]==题目6（实操题）

#### 题干

定义一个`Person` 类,包含初始化 init 方法:

实例属性:       名字, name
						年龄, age

1. 记录由该类创建的对象的个数，创建一个对象，计数+1，删除一个对象，计数-1；

2. 定义一个方法，可以打印当前对象的个数；

3. 定义一个方法`show_info`, 输出以下信息

   ```
   这是一个 Person 类,谢谢查看!
   ```

4. 打印对象的时候，可以输出打印自己的名字和年龄

   ```python
   我的名字是 xxx, 年龄是 xxx
   ```

5. 定义一个方法 `study`, 输出以下信息

   ```python
   我叫 xxx, 我要好好学习
   ```

6. 操作步骤

   1.  调用`show_info `方法；
   2.  创建两个对象, 打印当前对象，并打印当前的对象个数；
   3.  分别使用两个对象调用`study`方法；
   4.  删除一个对象，打印输出当前的对象个数。

#### 考察知识点

- 面向对象

- 属性和方法

- 类属性

答：

```python
class Person(object):
    # 定义类属性count,统计该类创建的对象的个数
    __count = 0

    # 定义init方法,创建实例属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__count += 1

    # 定义类方法,打印当前对象的个数
    @classmethod
    def get_count(cls):
        return cls.__count

    # 定义静态方法show_info
    @staticmethod
    def show_info():
        print('这是一个Person类, 谢谢查看!')

    # 定义str方法
    def __str__(self):
        return f"姓名:{self.name}, 年龄:{self.age}。"

    # 定义study方法
    def study(self):
        print(f"我叫 {self.name}, 我要好好学习。")

    # 定义__del__方法
    def __del__(self):
        Person.__count -= 1


# 调用show_info方法
Person.show_info()
print(Person.get_count())
xw = Person('小王', 18)
print(xw, xw.get_count())
xh = Person('小红', 18)
print(xh, xh.get_count())

xw.study()
xh.study()

del xw
print(Person.get_count())
```

### 题目 7

1.按如下要求完成代码的编写：

1). 定义一个Person类，包含姓名和年龄属性，要求姓名是公有属性，年龄是私有属性

2). 提供获取私有属性的公有方法 get_age方法

3). 提供可以设置私有属性的set_age方法，要求如果输入的年龄在 0--120 之间，设置年龄，否则提示输入不正确

4). 重写 `__str__` 要求打印对象时，把姓名和年龄都打印出来

#### 考察知识点

- 面向对象

- 权限

  答：

  ```python
  class Person(object):
      def __init__(self, name, age):
          self.name = name
          self.__age = age  # 私有属性
  
      def get_age(self):
          return self.__age  # 获取私有属性
  
      def set_age(self, age):
          if 0 <= age <= 120:
              self.__age = age  # 设置私有属性
          else:
              print("输入不正确")
  
      def __str__(self):
          return "姓名：{}，年龄：{}".format(self.name, self.__age)  # 打印对象信息
  
  
  if __name__ == '__main__':
      p = Person("张三", 18)
      print(p.get_age())
      p.set_age(22)
      print(p.get_age())
      p.set_age(130)
      print(p.get_age())
      print(p)
  ```

