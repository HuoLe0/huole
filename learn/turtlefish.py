import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#定义乌龟类
class Turtle:
    def __init__(self):
        #初始体力
        self.power = 100
        #初始位置随机
        self.x = np.random.randint(0,10)
        self.y = np.random.randint(0,10)

    def move(self):
        #随机计算方向并移动到新的位置(x,y)
        new_x = self.x + np.random.choice([1,2,-1,-2])
        new_y = self.y + np.random.choice([1,2,-1,-2])
        #检查移动后是否超出场景x轴边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
        #检查移动后是否超出场景y轴边界
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        #体力消耗
        self.power -= 1
        #返回移动后的新位置
        return (self.x,self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


#定义鱼类
class Fish:
    def __init__(self):
        self.x = np.random.randint(0,10)
        self.y = np.random.randint(0,10)


    def move(self):
        #随机计算方向并移动到新的位置(x,y)
        new_x = self.x + np.random.choice([1,-1])
        new_y = self.y + np.random.choice([1,-1])
        # 检查移动后是否超出场景x轴边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        #返回移动后的新位置
        return (self.x,self.y)

#开始测试数据
turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)
tx = []
ty = []
fx = []
fy = []
while True:
    if not len(fish):
        print('鱼都吃完了，游戏结束')
        break
    if not turtle.power:
        print('乌龟体力耗尽，挂了')
        break

    #游戏开始
    #首先乌龟迈出第一步
    print("乌龟移动前坐标：", (turtle.x, turtle.y))  # 乌龟移动前
    turtle.move()
    print("乌龟移动后坐标：", (turtle.x, turtle.y))  # 乌龟移动后
    for item in fish:
        print("鱼移动前坐标：", (item.x, item.y))
        item.move()  # 感觉鱼的移动前后的坐标差有问题
        print("鱼移动后坐标：", (item.x, item.y))
        if item.x == turtle.x and item.y == turtle.y:
            turtle.eat()
            fish.remove(item)
            print("死了一只鱼")
            print("乌龟最新体力值为 %d" % turtle.power)