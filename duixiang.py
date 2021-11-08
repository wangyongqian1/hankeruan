'''
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体
'''
# class Cup:
#     __high=0
#     __rongji=0.0
#     __color=""
#     __cailiao=""
#
#     def setHigh(self,high):
#         if high<0 or high>40:
#             print("水杯的高度非法")
#         else:
#             self.__high=high
#
#     def getHigh(self):
#         return self.__high
#
#     def setRongji(self,rongji):
#         if rongji<0 or rongji>5.0:
#             print("水杯的容积非法")
#         else:
#             self.__rongji=rongji
#
#     def getRongji(self):
#         return self.__rongji
#
#     def setColor(self, color):
#         if color =="" :
#          print("水杯的颜色不能为空")
#         else:
#             self.__color=color
#
#     def getColor(self):
#         return self.__color
#
#     def setCailiao(self, cailiao):
#         if cailiao =="":
#             print("水杯的材料不能为空")
#         else:
#             self.__cailiao=cailiao
#
#     def getCailiao(self):
#         return self.__cailiao
#
#     def cun(self):
#         print("水杯可以存放",self.__rongji,"升的水")
#
#     def showcup(self):
#         print("水杯的高度是",self.__high,"cm，容积是",self.__rongji,"升，颜色是",self.__color,"材质是",self.__cailiao)
#
# c =Cup()
# c.setHigh(20)
# c.setRongji(2.5)
# c.setCailiao("不锈钢")
# c.setColor("白色")
# c.cun()
# c.showcup()

'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
'''
# class Computer:
#     __screen=0.0
#     __price=0
#     __cpu=""
#     __neicun=0
#     __waittime=0
#
#     def setScreen(self,screen):
#         if screen<0 or screen>100:
#             print("笔记本电脑屏幕大小的非法")
#         else:
#             self.__screen=screen
#
#     def getScreen(self):
#         return self.__screen
#
#     def setPrice(self,price):
#         if price<0:
#             print("笔记本电脑的价格非法")
#         else:
#             self.__price=price
#
#     def getPrice(self):
#         return self.__price
#
#     def setCpu(self, cpu):
#         if cpu =="" :
#             print("笔记本电脑的cpu非法")
#         else:
#             self.__cpu=cpu
#
#     def getCpu(self):
#         return self.__cpu
#
#     def setNeicun(self, neicun):
#         if neicun<0:
#             print("笔记本电脑的内存大小非法")
#         else:
#             self.__neicun=neicun
#
#     def getNeicun(self):
#         return self.__neicun
#
#     def setWaittime(self, waittime):
#         if waittime<0:
#             print("笔记本电脑的待机时长非法")
#         else:
#             self.__waittime=waittime
#
#     def getWaittime(self):
#         return self.__neicun
#
#     def write(self,name,num):
#         print(name,"使用笔记本电脑一分钟可以打",num,"个字")
#
#     def game(self,name,hour):
#         print(name,"使用笔记本电脑可以打",hour,"个小时的游戏")
#
#     def shipin(self,name,kind):
#         print(name,"使用笔记本电脑可以看",name,"视频")
#
#     def showcomputer(self):
#         print("笔记本电脑的屏幕大小是",self.__screen,"英寸，价格是",self.__price,"元，","cpu型号是",self.__cpu,"，内存大小是",
#               self.__neicun,"G，待机时长是",self.__waittime,"小时")
#
# co =Computer()
# co.setScreen(15.6)
# co.setPrice(3650)
# co.setCpu("英特尔")
# co.setNeicun(256)
# co.setWaittime(24)
# co.write("张三",200)
# co.game("张三",8)
# co.shipin("张三","腾讯")
# co.showcomputer()

'''
中国工商银行系统
'''
import random
import math
import pymysql
from DBUtils import update
from DBUtils import select
class bank:
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
        if int(math.log10(account1) + 1) != 8:
            print("你的账号输入错误")
        else:
            self.__account1=account1

    def getAccount1(self):
        return self.__account1

    def setAccount(self,account):
        if int(math.log10(account) + 1) != 8:
            print("你的账号输入错误")
        else:
            self.__account=account

    def getAccount(self):
        return self.__account

    def setName(self, name):
        if name =="":
            print("你的姓名输入错误")
        else:
            self.__name=name

    def getName(self):
        return self.__name

    def setPassword(self, password):
        if int(math.log10(password) + 1) != 6:
            print("你的密码输入错误")
        else:
            self.__password=password

    def getPassword(self):
        return self.__password

    def setCountry(self, country):
        if country == "":
            print("你的国籍输入错误")
        else:
            self.__country=country

    def getCountry(self):
        return self.__country

    def setProvince(self, province):
        if province == "":
            print("你的省份输入错误")
        else:
            self.__province=province

    def getProvince(self):
        return self.__province

    def setStreet(self, street):
        if street == "":
            print("你的街道输入错误")
        else:
            self.__street=street

    def getStreet(self):
        return self.__street

    def setDoor(self, door):
        if door == "":
            print("你的门牌号输入错误")
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
            print("你的开户行输入错误")
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
            sql3 = "select * from bank where account=%s"
            param3 = [self.__account]
            data3 = select(sql3, param3, mode="one")
            info = '''
                                ------------存钱信息------------
                                            账号:%s
                                            存款余额:%s
                               '''
            print(info % (data3[1], data3[7]))
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
    b = bank()
    b.showbank()
    a = int(input("请输入你要办理的业务"))
    if a == 1:
        print("开户")
        account = random.randint(10000000, 99999999)
        b.setAccount(account)
        name = input("请输入你的姓名")
        b.setName(name)
        password = int(input("请输入你的密码"))
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
        account = int(input("请输入你的账号"))
        b.setAccount(account)
        money = int(input("请输入你要存取的金额"))
        b.setMoney(money)
        b.cunqian()
    elif a == 3:
        print("取钱")
        account = int(input("请输入你的账号"))
        b.setAccount(account)
        password = int(input("请输入你的密码"))
        b.setPassword(password)
        money = int(input("请输入你要取出的金额"))
        b.setMoney(money)
        b.quqian()
    elif a == 4:
        print("转账")
        account = int(input("请输入你的转出账号"))
        b.setAccount(account)
        account1 = int(input("请输入你的转入账号"))
        b.setAccount1(account1)
        password = int(input("请输入你的密码"))
        b.setPassword(password)
        money = int(input("请输入你要转出的金额"))
        b.setMoney(money)
        if account == account1:
            print("输入的转出账号与转入账号不能相同")
        else:
            b.zhuanzhang()
    elif a == 5:
        print("查询")
        account = int(input("请输入你的账号"))
        b.setAccount(account)
        password = int(input("请输入你的密码"))
        b.setPassword(password)
        b.chaxun()
    elif a == 6:
        print("欢迎下次光临")
        break
