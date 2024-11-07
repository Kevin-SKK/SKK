## Day04 作业

## 简答题

### 1. 简述 局部变量和全局变量的特点?

```
局部变量:
局部变量定义在函数内部，在函数外部无法访问。
只能在定义它的函数内部使用，出了这个函数就被销毁了，不再占用内存空间。
局部变量只在函数被调用时才会存在，并在函数执行完毕后被销毁。
不同函数可以使用相同名称的局部变量，彼此之间不会产生冲突。

全局变量：
全局变量定义在函数外部，在整个程序中均可访问。
在程序的任何地方都可以使用全局变量。
全局变量在程序执行期间一直存在，直到程序退出或者被显式删除。
不同函数可以使用和修改相同的全局变量，因此需要特别注意全局变量的值的变化情况，以免引起意料不到的错误。
```

### 2. python中可变类型数据有哪些？不可变类型数据有哪些?

```yacas
可变数据类型:
列表(list), 字典(dict),集合(set)
不可变数据类型:
数值类型(numbers), 字符串(string),元组(tuple)
```

### 3. 局部变量和全局变量

有如下代码：

```python
num = 10
def anum():
    num = 20
print(num)
```

请问这段代码最终输出的值是多少？

```yacas
20;输出函数在局部变量之外,因此不会受到局部变量的影响
```



## 代码题

### 题目1

定义一个函数func, 函数的功能如下:

1. 函数存在两个参数, 可以接收 姓名和 性别两个信息
2. 调用时如果传递性别信息, 则使用 传递的数据值
3. 如果不传递性别信息, 性别的值为 '保密'
4. 在函数内部打印 姓名和性别信息

```python
def func(name, gender='保密'):
    print('姓名:', name)
    print('性别:', gender)
func('a')
func('a', 'b')    
```



### 题目2（实操题）

#### 题干

定义一个可以用于同时求解3个数的和与差的函数。

#### 考察知识点

- 定义函数
- 调用函数

```python
def arith(a, b, c):
    add = a + b + c
    sub = a - b - c
    return add, sub


x = int(input('第一个数字:'))
y = int(input('第二个数字:'))
z = int(input('第三个数字:'))
print(f'三者的和与差是:{arith( x, y, z)}')
```



### 题目3（实操题）

#### 题干

思考一下，有这样的一个列表：

```properties
products = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 178},
    {"name": "usb电动小风扇", "price": 59},
    {"name": "遮阳伞", "price": 36}
]
sum_ = 0
for i in products:
    sum_ += i.get('price')
if sum_ <= 8000:
    print('能')
else:
    print('钱不够，不能完成所有商品的购买')

```

然后小明一共有8000块钱，那么他能不能买下这所有商品？如果能，请输出"能"，否则输出"钱不够，不能完成所有商品的购买"。

#### 考察知识点

- 列表

- 字典

- 条件判断



### ==[可选]==题目4（实操题）

#### 题干

从键盘上输入年、月，通过return关键字来写一个函数，并返回当前月份的天数，例如30、31等。【提示：`闰年就是能被4整除，且不能被100整除，或者能被400整除的年份。`】

#### 考察知识点

- 函数
- 判断

```Python
# 方案一:对年份判断
year = int(input('请输入年:'))
month = int(input('请输入月:'))


def day_of_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28


print(f'这个月有{day_of_month(year, month)}天')
# 方案二:取对应的索引
year = int(input('请输入年:'))
month = int(input('请输入月:'))


def day_of_month(year, month):
    day = (31, 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    return day[month - 1]


print(f'这个月有{day_of_month(year, month)}天')
```

