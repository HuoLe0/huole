#*************************************************
#             猜数字小游戏，每轮有三次机会
#               （对004讲代码的修改）
#*************************************************
import easygui as g
import random
secret = random.randint(1,10)
count = 3
guess = g.integerbox(msg='不妨猜一下小甲鱼现在心里想的是哪个数字（1~10）：'\
                     ,title='数字小游戏',lowerbound=1,upperbound=10)
#lowerbound参数设置最小值，upperbound参数设置最大值
while count:
    if secret == guess:
        g.msgbox('恭喜你，猜对了!')
        break
    else:
        count -= 1
        if guess > secret:
            g.msgbox('大了，大了\n\n您还有%d次机会'%count)
        else:
            g.msgbox('小了，小了\n\n您还有%d次机会'%count)
        guess = g.integerbox(msg='不妨猜一下小甲鱼现在心里想的是哪个数字（1~10）：'\
                             ,title='数字小游戏',lowerbound=1,upperbound=10)
    if count == 1:
        break
if count == 1:
    if secret == guess:
        g.msgbox('恭喜你，猜对了!')
    else:
        g.msgbox('还是没猜对T_T\n\n次数用完了，游戏结束')
        g.msgbox('小甲鱼心中的数字是：%d'%secret)
