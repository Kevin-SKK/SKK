# 今日目标: 面向对象高级

<font size='6' color='red'>继承,方法重写,权限,类成员,实例成员</font>

## 1.继承入门

==class 子类名(父类名):==

**`面向对象中的继承`**: 指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法.

**`面向对象中继承的作用`**: 提高代码的复用率, 减少重复代码的书写.

```python
class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('动物吃饭')

    def sleep(self):
        print('动物睡觉')

# class 类名(父类名):  --  继承语法
class Cat(Animal):
    def catch_mouse(self):
        print('可以捉老鼠')

if __name__ == '__main__':
    c = Cat('tom',2)
    c.eat()
    c.sleep()
    c.catch_mouse()
```



## 2.单继承和多继承

==class 子类名(父类名1,父类名2):==

==注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法==

```python
class Fu():
    def study(self):
        print('望子成龙')

    def show(self):
        print('家长言行教育')

class Teacher():
    def study(self):
        print("老师会教学生一技之长")

    def interview(self):
        print('工资是靠面试谈来的')

class Zi(Fu,Teacher):
    pass

if __name__ == '__main__':
    z = Zi()
    # 注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法。
    z.study()#望子成龙
    z.show()
    z.interview()
```



## 3.子类和父类定义同名属性

```python
class Fu():
    def __init__(self):
        print('--父类init走了--')
        self.name = '父亲'

class Zi(Fu):
    def __init__(self):
        print('--子类init走了--')
        # super()表示父类的对象.
        super().__init__()
        self.name = '孩子'

if __name__ == '__main__':
    z = Zi()
    print(z.name)# 孩子  ---子类和父类具有同名属性和方法，默认使用子类的同名属性和方法
```



## 4.子类和父类定义同名方法(覆盖)

```python
# 类和父类具有同名属性和方法，默认使用子类的同名属性和方法
class Fu():
    def fall_in_love(self):
        print('写一封情书')

class Zi(Fu):
    def fall_in_love(self):
        print('玩微信')

if __name__ == '__main__':
    z = Zi()
    z.fall_in_love()#玩微信
```



## 5.super()调用父类方法(扩展)

```python
# 类和父类具有同名属性和方法，默认使用子类的同名属性和方法
class Fu():
    def fall_in_love(self):
        print('写一封情书')

class Zi(Fu):
    def fall_in_love(self):
        # 子类觉得父类的功能还有用.但是不是完全可行.
        # 在这里想要调用父类的功能.
        #方式1:类名调用类中的函数(self)
            #Fu.__init__(self)
            #Fu.fall_in_love(self)

        #方式2: super()调用父类方法.
        super().fall_in_love()

        print('玩微信')

if __name__ == '__main__':
    z = Zi()
    z.fall_in_love()#玩微信

    print(Zi.__mro__) # 查看类中继承关系拓扑图
   #  (<class '__main__.Zi'>, <class '__main__.Fu'>, <class 'object'>)
```



## 6.多层继承

```python
class A(object):
    def show(self):
        print('aaa')

class B():
    def show(self):
        print('bbb')

class C(A,B):
    def show(self):
        print('ccc')

class D(C):
    def show1(self):
        print('ddd')

if __name__ == '__main__':
    print(D.__mro__) 
    #(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
    d = D()
    d.show()# ccc

```



## 7.私有权限[重要]

![image-20230504115938056](day07课堂笔记.assets/image-20230504115938056.png)

```python
class Person():
    # 属性:name和age
    def __init__(self, name, age):
        self.name = name
        # 给 age 变量 加上私有属性-- 超出本类无法访问.
        self.__age = age

    def __str__(self):
        return f'我的名字是:{self.name},我的你年龄是:{self.__age}'

    # 公开的设置年龄的方法--- 可以加上校验
    def set_age(self,age):
        if age > 0 and age < 200:
            self.__age = age

    # 公开的返回私有变量age的值.
    def get_age(self):
        return self.__age

 #学生类继承父类
class Student(Person):
    pass


if __name__ == '__main__':
    p1 = Person('tom',19)
    print(p1)
    #过了一年.tom长大一岁.结果手抖了.多敲一个0
    #p1.age = 200

    #print(p1.age)#AttributeError: 'Person' object has no attribute 'age'
    p1.set_age(20)
    print(p1.get_age())#20

    s = Student("tom",19)
    #私有属性 --子类通过继承--无法获取.
   # print(s.age)#AttributeError: 'Student' object has no attribute 'age'
   # print(s.__age)#AttributeError: 'Student' object has no attribute '__age'
```

## 8.多态[了解]

```python
class Animal():
    def eat(self):
        print('动物吃饭')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Dog(Animal):
    def eat(self):
        print('狗吃肉')

class XXX():
    def eat(self):
        print('外星动物--风餐露宿')

# 变量: 类型  ==  对类型解释
def feed(a:Animal):
    a.eat()

if __name__ == '__main__':
    a = Animal()
    feed(a)
    #创建猫对象--猫对象是动物的子类
    c = Cat()
    feed(c)

    d = Dog()
    feed(d)

    x = XXX()
    feed(x)
```



## 9.类属性和实例属性

- 类属性: 
  - 定义在类中,方法外. 
  - 属于类可以用类名调用. 
  - 所有对象共享一个类属性.可以访问不能修改.
- 实例属性:
  - 一般情况定义在__init()函数中
  - 属于对象.可以用对象名调用.
  - 实例属性属于对象.每个对象单独有一份自己的实例属性.

```python
class Student():
    # 类属性 == 学校名称
    school_name = '黑马'

    def __init__(self,name,age):
        # 实例属性
        self.name = name
        self.age = age

if __name__ == '__main__':

    #类属性 ,用类名就可以调用
    print(Student.school_name)
    Student.school_name = '黑马程序员'

    #实例属性需要用对象来调用
    s1 = Student('小明',19)
    print(s1.name,s1.age,s1.school_name)

    # 使用对象修改类属性--不能生效
    #s1.school_name = '传智教育'  # 实际是给 s1 对象添加了属性 school_name

    s2 = Student('小强',20)
    print(s2.name,s2.age,s2.school_name)
```

## 10.类方法和实例方法

```python
class Student():
    # 类属性 == 学校名称
    school_name = '黑马'

    def __init__(self,name,age):
        # 实例属性
        self.name = name
        self.age = age

    #类方法
    @classmethod
    def print_school_name(cls):
        print(f'我的学校是:{cls.school_name}')

    #实例方法
    def study(self):
        print('我在黑马学编程')

if __name__ == '__main__':
    # 类名可以直接调用类方法
    Student.print_school_name()

    # 类名不可以直接调用实例方法
    #Student.study()# TypeError: study() missing 1 required positional argument: 'self'
    s = Student('tom',19)
    s.study()# 我在黑马学编程

    s.print_school_name() #我的学校是:黑马 -- 不推荐使用对象调用 类方法.
```





## 11.工具类的制作[扩展]

```python
# 工具类: 为了方便调用者使用类中的属性或方法.
class My_Math():

    #类属性
    PI = 3.14

    #类方法 -- 求任意个整数的和
    @classmethod
    def sum(cls,*args):
        sum = 0
        for i in args:
            sum += i
        return sum

if __name__ == '__main__':
    print(My_Math.sum(1, 2, 3, 4, 5))
    print(My_Math.PI)
```



## 12.静态方法[了解]

```python
class MyTools:

    #定义静态方法
    @staticmethod
    def print_Tools_info():
        print("这是我写得工具类.工具类中只用类属性和类方法.方便你来使用.请用类名来用吧.")

if __name__ == '__main__':
    #静态方法可以使用类名调用
    MyTools.print_Tools_info()

    # 静态方法可以使用对象名调用
    mt = MyTools()
    mt.print_Tools_info()

    print(mt.print_Tools_info)

    mt2 = MyTools()
    mt2.print_Tools_info()

    print(mt2.print_Tools_info)
```



## 13.综合案例

```yacas
1. 设计一个 Game 类 (类名)
2. 属性:
	• 定义一个 top_score 类属性 -> 记录游戏的历史最高分
	• 定义一个 player_name 实例属性 -> 记录当前游戏的玩家姓名
3. 方法:
	• 静态方法 show_help() -> 直接打印  这是游戏帮助信息
	• 类方法 show_top_score() -> 显示历史最高分
	• 实例方法 start_game() -> 开始当前玩家的游戏
        -   3.1 输出 玩家 xxx 开始游戏
        -   3.2 使用随机数,生成 10 - 100 之间的随机数字作为本次游戏的得分
        -   3.3 打印 玩家 xxx 本次游戏得分 xxx
        -   3.4 判断本次游戏得分和最高分之间的关系
4. 主程序步骤: __main__
    1 查看帮助信息
    2 查看历史最高分
    3 创建游戏对象，开始游戏
```

```python
# 1. 设计一个 Game 类 (类名)
# 2. 属性:
#  • 定义一个 top_score 类属性 -> 记录游戏的历史最高分
#  • 定义一个 player_name 实例属性 -> 记录当前游戏的玩家姓名
# 3. 方法:
#  • 静态方法 show_help() -> 直接打印  这是游戏帮助信息
#  • 类方法 show_top_score() -> 显示历史最高分
#  • 实例方法 start_game() -> 开始当前玩家的游戏
#         -   3.1 输出 玩家 xxx 开始游戏
#         -   3.2 使用随机数,生成 10 - 100 之间的随机数字作为本次游戏的得分
#         -   3.3 打印 玩家 xxx 本次游戏得分 xxx
#         -   3.4 判断本次游戏得分和最高分之间的关系
# 4. 主程序步骤: __main__
#     1 查看帮助信息
#     2 查看历史最高分
#     3 创建游戏对象，开始游戏
import random


class Game:
    top_score = 0#记录游戏的历史最高分

    def __init__(self,name):
        self.player_name = name

    @staticmethod
    def show_help():
        print('这是游戏帮助信息')

    @classmethod
    def show_top_score(cls):
        print(f"历史最高分是:{cls.top_score}")

    def start_game(self):
        print(f"玩家{self.player_name}开始游戏")
        score = random.randint(10,100)
        print(f'玩家{self.player_name}本次得分:{score}')
        if score > Game.top_score:
            print(f'恭喜玩家{self.player_name}打破游戏最高分{Game.top_score}记录,得分{score}')
            Game.top_score = score



if __name__ == '__main__':
    Game.show_help()
    Game.show_top_score()
    zs = Game('张三')
    zs.start_game()

    ls = Game('李四')
    ls.start_game()

    ww = Game('王五')
    ww.start_game()
```