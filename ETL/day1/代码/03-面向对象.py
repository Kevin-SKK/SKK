import random


class Dog:
    def __init__(self):
        self.leg = 4
        self.age = random.randint(0, 20)


xiaohei = Dog()
print(xiaohei.age)
xiaobai = Dog()
print(xiaobai.age)