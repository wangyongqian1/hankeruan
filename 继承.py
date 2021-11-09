'''
手机
'''
# import time
# class OldPhone:
#     __brand=""
#
#     def setBrand(self,brand):
#         if brand=="":
#             print("品牌不能为空")
#         else:
#             self.__brand=brand
#
#     def getBrand(self):
#         return self.__brand
#
#     def call(self,number):
#         print("正在给",number,"打电话")
#
# class NewPhone(OldPhone):
#     pass
#
#     def call(self,number):
#         print("语音拨号中")
#         for i in range(4):
#             print(".",end="")
#             time.sleep(1)
#         super().call(number)
#
#     def showNewPhone(self):
#         print("品牌为：",self.getBrand(),"的手机很好用")
#
# n=NewPhone()
# n.setBrand("华为")
# n.showNewPhone()
# n.call("12345678901")

'''
厨师
'''
# class ChuShi:
#     __name=""
#     __age=0
#
#     def setName(self,name):
#         if name=="":
#             print("姓名不能为空")
#         else:
#             self.__name=name
#
#     def getName(self):
#         return self.__name
#
#     def setAge(self,age):
#         if age<=0 or age>120:
#             print("年龄输入非法")
#         else:
#             self.__age=age
#
#     def getAge(self):
#         return self.__age
#
#     def zeng(self):
#         print("蒸饭")
#
#
# class Son(ChuShi):
#     pass
#
#     def chao(self):
#         print("炒菜")
#
# class GrandSon(Son):
#     pass
#
#     def ji(self):
#         super().zeng()
#         super().chao()
#
#     def show(self):
#         print("姓名为",self.getName(),"的厨师，今年",self.getAge(),"岁了")
#
# s=GrandSon()
# s.setName("张三")
# s.setAge(26)
# s.ji()
# s.show()

'''
i.	人：年龄，性别，姓名。
ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
'''
# class Person:
#     __age=0
#     __name = ""
#     __sex=""
#
#     def setSex(self,sex):
#         if sex !="男" and sex !="女":
#             print("你是人妖吗？")
#         else:
#             self.__sex=sex
#
#     def getSex(self):
#         return self.__sex
#
#     def setName(self,name):
#         if name=="":
#             print("姓名不能为空")
#         else:
#             self.__name=name
#
#     def getName(self):
#         return self.__name
#
#     def setAge(self,age):
#         if age<=0 or age>120:
#             print("年龄输入非法")
#         else:
#             self.__age=age
#
#     def getAge(self):
#         return self.__age
#
#
# class Worker(Person):
#     pass
#
#     def work(self):
#         print(self.getName(),"性别",self.getSex(),"今年",self.getAge(),"岁了，正在干活")
#
# w=Worker()
# w.setName("张三")
# w.setSex("男")
# w.setAge(43)
# w.work()
#
# class Student(Person):
#     __id=""
#
#     def setId(self,id):
#         if id=="":
#             print("学号不能为空")
#         else:
#             self.__id=id
#
#     def getId(self):
#         return self.__id
#
#     def work(self,ji):
#         print(self.getName(),"学号为",self.__id,"性别为",self.getSex(),"今年",self.getAge(),"岁了,正在",ji)
#
# s=Student()
# s.setId("s1")
# s.setName("李四")
# s.setSex("男")
# s.setAge(23)
# s.work("学习")
# s.work("唱歌")

'''
工商银行
'''
import random
import math
from 数据库.DBUtils import update
from 数据库.DBUtils import select
class Bank:
    __account=0
    __name=""
    __password=0
    __country=""
    __province=""
    __street=""
    __door=""
    __money=0
    __bank_name=""
    __account1=0

    def setAccount1(self,account1):
        if account1==None:
            print("账号不能为空")
        elif int(math.log10(account1) + 1) != 8:
            print("你的账号输入错误")
        else:
            self.__account1=account1

    def getAccount1(self):
        return self.__account1

    def setAccount(self,account):
        if account==None:
            print("账号不能为空")
        elif int(math.log10(account) + 1) != 8:
            print("你的账号输入错误")
        else:
            self.__account=account

    def getAccount(self):
        return self.__account

    def setName(self, name):
        if name =="":
            print("姓名不能为空")
        else:
            self.__name=name

    def getName(self):
        return self.__name

    def setPassword(self, password):
        if password==None:
            print("密码不能为空")
        elif int(math.log10(password) + 1) != 6:
            print("你的密码输入错误")
        else:
            self.__password=password

    def getPassword(self):
        return self.__password

    def setCountry(self, country):
        if country == "":
            print("国籍不能为空")
        else:
            self.__country=country

    def getCountry(self):
        return self.__country

    def setProvince(self, province):
        if province == "":
            print("省份不能为空")
        else:
            self.__province=province

    def getProvince(self):
        return self.__province

    def setStreet(self, street):
        if street == "":
            print("街道不能为空")
        else:
            self.__street=street

    def getStreet(self):
        return self.__street

    def setDoor(self, door):
        if door == "":
            print("门牌号不能为空")
        else:
            self.__door=door

    def getDoor(self):
        return self.__door

    def setMoney(self, money):
        if money<0:
            print("你的存款金额输入错误")
        else:
            self.__money=money

    def getMoney(self):
        return self.__money

    def setBankname(self, bank_name):
        if bank_name == "":
            print("开户行不能为空")
        else:
            self.__bank_name=bank_name

    def getBankname(self):
        return self.__bank_name

    def showbank(self):
        print("*************************************************")
        print("*           中国工商银行                          *")
        print("*           账户管理系统                          *")
        print("*************************************************")
        print(" ")
        print("*1.开户                                          *")
        print("*2.存钱                                          *")
        print("*3.取钱                                          *")
        print("*4.转账                                          *")
        print("*5.查询                                          *")
        print("*6.欢迎下次光临                                    *")
        print("*************************************************")
        sql = "select * from bank"
        param = []
        data = select(sql, param, mode="all")
        for i in data:
            print(i)

    def kaihu(self):
        sql = "select count(*) from bank"
        param = []
        data = select(sql, param, mode="one")
        if data[0] > 100:
            print("本银行已满，请到其他银行开户")
        sql1 = "select * from bank where account=%s"
        param1 = [self.__account]
        data1 = select(sql1, param1, mode="one")
        if data1 != None:
            print("用户已存在")
        else:
            sql2 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param2 = [self.__account, self.__name, self.__password, self.__country, self.__province
                , self.__street, self.__door, self.__money, self.__bank_name]
            update(sql2, param2)
            print("开户成功，以下是你的个人信息")
            sql2 = "select * from bank where account=%s"
            param2 = [self.__account]
            data2 = select(sql2, param2, mode="one")
            info = '''
                                        ------------个人信息------------
                                                    用户名:%s
                                                    账户:%s
                                                    密码:******
                                                    国籍:%s
                                                    省份:%s
                                                    街道:%s
                                                    门牌号:%s
                                                    存款余额:%s
                                                    开户行:%s
                                     '''
            print(info % (data2[0], data2[1], data2[3], data2[4], data2[5], data2[6], data2[7], data2[8]))

    def cunqian(self):
        sql = "select * from bank where account=%s"
        param = [self.__account]
        data = select(sql, param, mode="one")
        if data != None:
            sql1 = "update bank set money=%s where account=%s"
            money = data[7] + self.__money
            param1 = [money, self.__account]
            update(sql1, param1)
            sql2 = "select * from bank where account=%s"
            param2 = [self.__account]
            data2 = select(sql2, param2, mode="one")

            info = '''
                                ------------存钱信息------------
                                            账号:%s
                                            存款余额:%s
                               '''
            print(info % (data2[1], data2[7]))
        else:
            print("用户不存在")


    def quqian(self):
        sql = "select * from bank where account=%s"
        param = [self.__account]
        data = select(sql, param, mode="one")
        if data != None:
            sql1 = "select * from bank where account=%s and password=%s"
            param1 = [self.__account, self.__password]
            data1 = select(sql1, param1, mode="one")
            if data1 != None:
                if self.__money > data[7]:
                    print("钱不够")
                else:
                    sql2 = "update bank set money=%s where account=%s and password=%s"
                    money = data[7] - self.__money
                    param2 = [money, self.__account, self.__password]
                    update(sql2, param2)
                    sql3 = "select * from bank where account=%s and password=%s"
                    param3 = [self.__account, self.__password]
                    data3 = select(sql3, param3, mode="one")
                    info = '''
                                        ------------取钱信息------------
                                                    账号:%s
                                                    存款余额:%s
                                       '''
                    print(info % (data3[1], data3[7]))
            else:
                print("密码输入错误")
        else:
            print("账号不存在")



    def zhuanzhang(self):
        sql = "select * from bank where account=%s"
        param = [self.__account]
        data = select(sql, param, mode="one")
        param1 = [account1]
        data1 = select(sql, param1, mode="one")
        if data != None and data1 != None:
            sql2 = "select * from bank where account=%s and password=%s"
            param2 = [self.__account, self.__password]
            data2 = select(sql2, param2, mode="one")
            if data2 != None:
                if data[7] >= self.__money:
                    sql2 = "update bank set money=%s where account=%s and password=%s"
                    money1 = data[7] - self.__money
                    param2 = [money1, self.__account, self.__password]
                    update(sql2, param2)
                    sql3 = "update bank set money=%s where account=%s"
                    money2 = data1[7] + self.__money
                    param3 = [money2, self.__account1]
                    update(sql3, param3)
                    sql4 = "select * from bank where account=%s and password=%s"
                    param4 = [self.__account, self.__password]
                    data3 = select(sql4, param4, mode="one")
                    sql5 = "select * from bank where account=%s"
                    param5 = [self.__account1]
                    data4 = select(sql5, param5, mode="one")
                    info = '''
                                            ------------转账信息------------
                                                        转出账号:%s
                                                        密码:******
                                                        存款余额:%s
                                                        转入账号:%s
                                                        存款余额:%s
                                       '''
                    print(info % (data3[1], data3[7], data4[1], data4[7]))
                else:
                    print("钱不够")
            else:
                print("密码输入错误")
        else:
            print("转出或转入的账号不存在")


    def chaxun(self):
        sql = "select * from bank where account=%s"
        param = [self.__account]
        data = select(sql, param, mode="one")
        print()
        if data != None:
            sql1 = "select * from bank where account=%s and password=%s"
            param1 = [self.__account, self.__password]
            data1 = select(sql1, param1, mode="one")
            if data1 != None:
                info = '''
                                                    ------------个人信息------------
                                                                用户名:%s
                                                                账号:%s
                                                                密码:******
                                                                国籍:%s
                                                                省份:%s
                                                                街道:%s
                                                                门牌号:%s
                                                                存款余额:%s
                                                                开户行:%s
                                                 '''
                print(info % (data[0], data[1], data[3], data[4], data[5], data[6], data[7], data[8]))
            else:
                print("密码输入错误")
        else:
            print("账号不存在")


while True:
    b = Bank()
    b.showbank()
    a = int(input("请输入你要办理的业务"))
    if a == 1:
        print("开户")
        account = random.randint(10000000, 99999999)
        b.setAccount(account)
        name = input("请输入你的姓名")
        b.setName(name)
        password = input("请输入你的密码")
        if password=="":
            password=None
        else:
            password=int(password)
        b.setPassword(password)
        print("请输入你的详细信息")
        country = input("\t\t请输入你的国籍")
        b.setCountry(country)
        province = input("\t\t请输入你的省份")
        b.setProvince(province)
        street = input("\t\t请输入你的街道")
        b.setStreet(street)
        door = input("\t\t请输入你的门牌号")
        b.setDoor(door)
        b.setMoney(1000)
        b.setBankname("中国工商银行")
        b.kaihu()
    elif a == 2:
        print("存钱")
        account = input("请输入你的账号")
        if account=="":
            account=None
        else:
            account=int(account)
        b.setAccount(account)
        money = int(input("请输入你要存取的金额"))
        b.setMoney(money)
        b.cunqian()
    elif a == 3:
        print("取钱")
        account = input("请输入你的账号")
        if account=="":
            account=None
        else:
            account=int(account)
        b.setAccount(account)
        password = input("请输入你的密码")
        if password=="":
            password=None
        else:
            password=int(password)
        b.setPassword(password)
        money = int(input("请输入你要取出的金额"))
        b.setMoney(money)
        b.quqian()
    elif a == 4:
        print("转账")
        account = input("请输入你的转出账号")
        if account=="":
            account=None
        else:
            account=int(account)
        b.setAccount(account)
        account1 = input("请输入你的转入账号")
        if account1=="":
            account1=None
        else:
            account1=int(account1)
        b.setAccount1(account1)
        password = int(input("请输入你的密码"))
        if password=="":
            password=None
        else:
            password=int(password)
        b.setPassword(password)
        money = int(input("请输入你要转出的金额"))
        b.setMoney(money)
        if account == account1:
            print("输入的转出账号与转入账号不能相同")
        else:
            b.zhuanzhang()
    elif a == 5:
        print("查询")
        account = input("请输入你的账号")
        if account=="":
            account=None
        else:
            account=int(account)
        b.setAccount(account)
        password = input("请输入你的密码")
        if password=="":
            password=None
        else:
            password=int(password)
        b.setPassword(password)
        b.chaxun()
    elif a == 6:
        print("欢迎下次光临")
        break


