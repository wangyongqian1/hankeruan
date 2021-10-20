'''
开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出
'''
import random
randint=random.randint(10,20)
print(randint)
i=5
count=0
while i>=0 :
    if i == 0 :
        i1 = int(input("请输入你要充值的金币"))
        i = i + i1
        count = 0
        num=int(input("请输入你要猜的数字"))
    elif i>0:
        num = int(input("请输入你要猜的数字"))
    else:
        print("你的金币为0，如果想要继续猜，需要充值金币")
    if num==randint:
        print("恭喜你猜对了")
        i=i+1
        break
    elif num>randint:
        if count < 2:
            print("猜大了")
            i = i - 1
            count = count + 1
        else:
            print("你已经猜错3次了，不能继续猜了")
            break
    elif num<randint:
        if count<2:
            print("猜小了")
            i=i-1
            count=count+1
        else:
            print("你已经猜错3次了，不能继续猜了")
            break
    else:
        print("猜错了，继续猜")

