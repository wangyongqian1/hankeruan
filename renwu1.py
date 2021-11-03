'''
1、实现输入10个数字，并打印10个数的求和结果
2、从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
# num1=int(input("请输入第1个数字"))
# num2=int(input("请输入第2个数字"))
# num3=int(input("请输入第3个数字"))
# num4=int(input("请输入第4个数字"))
# num5=int(input("请输入第5个数字"))
# num6=int(input("请输入第6个数字"))
# num7=int(input("请输入第7个数字"))
# num8=int(input("请输入第8个数字"))
# num9=int(input("请输入第9个数字"))
# num10=int(input("请输入第10个数字"))
# sum=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10
# avg=sum/10
# max=max(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)
# print("10个数的和是",sum)

# i=1
# sum=0
# avg=0
# while i <= 10:
#     num = int(input('请输入第{}个数:'.format(i)))
#     if i == 1:
#         max = min = num
#
#     else:
#         if num < min:
#             min = num
#         elif num > max:
#             max = num
#     i+=1
#     sum+=num
#     avg=sum/10
# print("10个数的和是",sum)
# print("最大的数是",max,"10个数的和是",sum,"平均数是",avg)

'''
使用random模块，如何产生 50~150之间的数
'''
# import random
# randint=random.randint(50,150)
# print(randint)

'''
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
# a=int(input("请输入三角形的第1边"))
# b=int(input("请输入三角形的第2边"))
# c=int(input("请输入三角形的第3边"))
# while a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
#     print("可以形成三角形")
#     if a==b or a==c or b==c:
#         print("形成等腰三角形")
#         break
#     elif a==b==c:
#         print("形成等边三角形")
#         break
#     elif a+b>c and a+c>b and b+c>a:
#         print("形成普通三角形")
#         break
#     else:
#         print("不能形成普通三角形")
#         break

'''
有以下两个数，使用+，-号实现两个数的调换。
A=56
B=78
实现效果：
A=78
B=56
'''

# A=56
# B=78
# A=A+B
# B=A-B
# A=A-B
# print("A=",A)
# print("B=",B)


'''
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''

# import time
# count=0
# i=0
# user = input("请输入用户名")
# if user == "root":
#     password = input("请输入密码")
#     while count<2:
#         if password == "admin":
#             print("登录成功")
#             break
#         else:
#             print("你的密码输入错误，请重新输入")
#             password = input("请输入密码")
#             count += 1
#             if password == "admin":
#                 print("登录成功")
#                 break
#             if count == 2:
#                 print("你已经连续三次密码输入错误，系统被锁定")
#                 time.sleep(60)
# else:
#     print("你的用户名输入错误，请重新输入")
#     user = input("请输入用户名")
#     while True:
#         if user == "root":
#             password = input("请输入密码")
#             while count < 2:
#                 if password == "admin":
#                     print("登录成功")
#                     break
#                 else:
#                     print("你的密码输入错误，请重新输入")
#                     password = input("请输入密码")
#                     count += 1
#                     if password == "admin":
#                         print("登录成功")
#                         break
#                     if count == 2:
#                         print("你已经连续三次密码输入错误，系统被锁定")
#                         time.sleep(60)
          


'''
编程使用"*"实现打印三角形
'''

i=1
while i<=7:
    print((7-i)*" ",i*"* ")
    i+=1


'''
使用while循环实现NxN乘法表的打印
'''
# i=int(input("请输入第1个数字"))
# j=int(input("请输入第2个数字"))
# sum=0
# for a in range(1,i+1):
#     for b in range(1,j+1):
#         if b<=a:
#             print(b,"*",a,"=",a*b,end="\t")
#     print()

'''
编程实现99乘法表的倒叙打印
'''


# i=9
# sum=0
# while i>=1:
#     j=1
#     while j<=i:
#         sum=j*i
#         print(j,"*",i,"=",sum,end='\t')
#         j += 1
#     print()
#     i -= 1


'''
一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
'''

# h=-20
# a=3
# b=-2
# day=0
# while h<0:
#     h+=a
#     h+=b
#     day+=1
#     if h>=0:
#         print(day,'天能出来')
#         break



'''
标识符	    是否合法	标识符	是否合法
char		        Cy%ty	
Oax_li		        $123	
fLul		        3_3 	
BYTE		        T_T	
'''


# while True:
#     str=input('请输入变量名')
#     if str=='exit':
#         print('变量名不合法')
#         break
#     if str[0].isalpha() or str[0]=='_':
#         for i in str[1:]:
#             if not (i.isalnum() or i == '_'):
#                 print("变量名",str,"不合法")
#                 break
#         else:
#             print("变量名",str,"合法")
#     else:
#         print("变量名",str,"不合法")


'''
开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出
1.	添加计数打印功能
2.	添加次数金币功能和锁定系统功能。
'''


# import random
# randint=random.randint(10,20)
# print(randint)
# i=5
# count=0
# while i>=0 :
#     if i == 0 :
#         i1 = int(input("请输入你要充值的金币"))
#         i = i + i1
#         count = 0
#         num=int(input("请输入你要猜的数字"))
#     elif i>0:
#         num = int(input("请输入你要猜的数字"))
#     else:
#         print("你的金币为0，如果想要继续猜，需要充值金币")
#     if num==randint:
#         i = i + 1
#         count=0
#         print("恭喜你猜对了,你现在有",i,"枚金币","你还有",3-count,"次机会")
#         break
#     elif num>randint:
#         if count < 2:
#             i = i - 1
#             count = count + 1
#             print("猜大了,你现在有",i,"枚金币","你还有",3-count,"次机会")
#         else:
#             print("你已经猜错3次了，系统被锁定")
#             time.sleep(60)
#             break
#     elif num<randint:
#         if count<2:
#             i = i - 1
#             count = count + 1
#             print("猜小了,你现在有",i,"枚金币","你还有",3-count,"次机会")
#         else:
#             print("你已经猜错3次了，不能继续猜了")
#             break
#     else:
#         print("猜错了，继续猜")


'''
用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''

j=1
sum=0
for i in range(1,21):
    j=j*i
    sum+=j
print(sum)




