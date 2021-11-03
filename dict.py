'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条
任务：打折：随机获得优惠券（9折10，5折5，1折2，面单1.
            单个商品打折9折10，5折5，1折2，面单1）

'''
# import  random
# #商品
# shop=[
#     ["刀",999],
#     ["斧子",200],
#     ["苹果",90000],
#     ["coco",150],
#     ["枸杞",900],
# ]
# #初始化余额
# money=random.randint(0,99999)
# print(money)
# #购物车
# mycart=[]
# #展示商品
# count1,count2,count3,count4,count5,count6,count7,count8=0,0,0,0,0,0,0,0
# while True:
#     for index,value in enumerate(shop):
#         print(index, ":", value)
#     chose=input("请输入商品编号")
#     if chose.isdigit():#str判断引号内是否为数字
#         chose=int(chose)#转换成整型
#         if chose <len(shop):#判断输入的内容是否小于列表的长度
#             if money>shop[chose][1]:#判断money是否大于商品的价格
#                 mycart.append(shop[chose])#把商品加入购物车
#                 print("恭喜你成功加入购物车")
#             else:
#                 print("穷鬼，去买其他商品")
#         else:
#             print("没有此商品")
#     elif chose=="q"or chose=="Q":
#         print("=================")
#         dazhe = random.randint(1, 8)
#         m = 0
#         for index, value in enumerate(mycart):
#             print(index, ":", value)
#             if dazhe == 1:
#                 count1 += 1
#                 if count1 <= 10:
#                     money = money - mycart[index][1] * 0.9  # money减去商品的价格
#                 print("恭喜你抽到所有商品打9折")
#             elif dazhe == 2:
#                 count2 += 1
#                 if count2 <= 5:
#                     money = money - mycart[index][1] * 0.5  # money减去商品的价格
#                 print("恭喜你抽到所有商品打5折")
#             elif dazhe == 3:
#                 count3 += 1
#                 if count3 <= 2:
#                     money = money - mycart[index][1] * 0.1  # money减去商品的价格
#                 print("恭喜你抽到所有商品打1折")
#             elif dazhe == 4:
#                 count4 += 1
#                 if count4 <= 1:
#                     money = money   # money减去商品的价格
#                 print("恭喜你抽到所有商品免单")
#             elif dazhe == 5:
#                 count5 += 1
#                 if count5 <= 10:
#                     m = mycart[0][1]
#                     if mycart[index][1] > m:
#                         m = mycart[index][1]
#                     money = money -mycart[index][1]+ m*0.1   # money减去商品的价格
#                 print("恭喜你抽到单个商品打9折")
#             elif dazhe == 6:
#                 count6 += 1
#                 if count6 <= 5:
#                     m = mycart[0][1]
#                     if mycart[index][1] > m:
#                         m = mycart[index][1]
#                     money = money -mycart[index][1]+ m * 0.5  # money减去商品的价格
#                 print("恭喜你抽到单个商品打5折")
#             elif dazhe == 7:
#                 count7 += 1
#                 if count7 <= 2:
#                     m = mycart[0][1]
#                     if mycart[index][1] > m:
#                         m = mycart[index][1]
#                     money = money -mycart[index][1]+ m * 0.9  # money减去商品的价格
#                 print("恭喜你抽到单个商品打1折")
#             elif dazhe == 8:
#                 count8 += 1
#                 if count8 <= 1:
#                     m = mycart[0][1]
#                     if mycart[index][1] > m:
#                         m = mycart[index][1]
#                     money = money -mycart[index][1]+ m # money减去商品的价格
#                 print("恭喜你抽到单个商品免单")
#         print("你的余额是",money)
#         mycart=[]
#
#     else:
#         print("别瞎弄")


'''
有下列人员数据库，请按要求实现
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
1.统计每个人的平均薪资
2.统计每个人的平均年龄
3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
4.统计公司男女人数
5.每个部门的人数
'''
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
# ]
#
# avg=0
# boy,girl=0,0
# for i,j in enumerate(names):
#     avg+=names[i][5]
# avg=avg/4
# print("每个人的平均薪资是",avg)
# avg1=0
# for i,j in enumerate(names):
#     avg1 += int(names[i][1])
# avg1=avg1/4
# print("每个人的平均年龄是", avg1)
# names.insert(5,["刘备","45","男","220","alibaba",500,"30"])
# print(names)
# for i,j in enumerate(names):
#     if names[i][2]=="男":
#         boy+=1
#     else:
#         girl+=1
# print("公司男员工有", boy,"人","女员工有",girl,"人")
# count1,count2,count3,count4=0,0,0,0
# for i,j in enumerate(names):
#     if names[i][6]=="50":
#         count1+=1
#     if names[i][6]=="60":
#         count2+=1
#     if names[i][6]=="10":
#         count3+=1
#     if names[i][6]=="30":
#         count4+=1
# print("部门编号为50的人数是", count1)
# print("部门编号为60的人数是", count2)
# print("部门编号为10的人数是", count3)
# print("部门编号为30的人数是", count4)

'''
现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
[罗恩, 23 ,35 ,44]
[哈利 ,60, 77 ,68 ,88, 90]
[赫敏, 97 ,99 ,89 ,91, 95, 90]
[马尔福 ,100, 85 ,90]
求每个人的总成绩？
'''
score=[
        ["罗恩", 23 ,35 ,44],
        ["哈利" ,60, 77 ,68 ,88, 90],
        ["赫敏", 97 ,99 ,89 ,91, 95, 90],
        ["马尔福" ,100, 85 ,90],
]

for i in range(len(score)):
    for j in range(len(score[i])):
        if j==0:
            sum=0
            continue
        else:
            sum+=score[i][j]
    print(score[i][0],"的总成绩是",sum)

'''
当输入是54321时，写出下面程序的执行结果
'''
# a=int(input("请输入一个数字"))
# while a !=0:
#     print(a%10)
#     a=a//10

'''
冒泡排序
'''
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
b=0
for i in range(0,len(a)-1):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            b=a[j]
            a[j]=a[j+1]
            a[j]=b
print(a)

