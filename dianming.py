'''
随机点名然后处罚遍数
#优化代码：只有一个input 进行判断 1or2 生成人名or几遍    q or Q退出  输入其他的直接锁死time.sleep(10)睡10秒
'''
import random
while True:
    list = ["法外狂徒", "小李子", "汤老师", "郭达", "强森", "抖森", "小罗伯特", "汉弗莱", "兰尼斯特", "千纸鹤"]
    index = input("请输入一个数字或字母")
    if index == "1":
        dint=int(random.randint(0,len(list)-1))
        print(list[dint])
    elif index == "2":
        num=int(random.randint(0,10))
        print("处罚了", num, "遍")
    elif index == "q" or index == "Q":
        print("退出系统")
        break
    else:
        print("退出系统")
        break




