import random
import math
from 数据库.DBUtils import update
from 数据库.DBUtils import select
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
bank={}
bank_name="中国工商银行"
money=0
sql = "select * from bank"
param = []
data=select(sql,param,mode="all")
for i in data:
    print(i)

def bankadd(account,name,password,country,province,street,door):
    sql = "select count(*) from bank"
    param = []
    data=select(sql,param,mode="one")
    if data[0]>100:
        return 3
    sql1="select * from bank where account=%s"
    param1=[account]
    data1=select(sql1,param1,mode="one")
    if data1 != None:
        return 2
    else:
        sql2 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [account, name, password, country, province, street, door, money, bank_name]
        update(sql2, param2)
        return 1

def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入你的姓名")
    password=int(input("请输入你的密码"))
    while int(math.log10(password)+1)!=6:
        password = int(input("请输入你的密码"))
    print("请输入你的详细信息")
    country=input("\t\t请输入你的国籍")
    province = input("\t\t请输入你的省份")
    street = input("\t\t请输入你的街道")
    door = input("\t\t请输入你的门牌号")
    num=bankadd(account, name, password, country, province, street, door)
    if num==1:
        print("开户成功，以下是你的个人信息")
        sql1 = "select * from bank where account=%s"
        param1 = [account]
        data = select(sql1, param1, mode="one")
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
        print(info % (data[0], data[1], data[3], data[4], data[5], data[6], data[7], data[8]))
    elif num==2:
        print("用户已存在")
    elif num==3:
        print("本银行已满，请到其他银行开户")

def bankmoneyadd(account):
    sql = "select * from bank where account=%s"
    param = [account]
    data = select(sql, param, mode="one")
    if data != None:
        money = int(input("请输入你要存取的金额"))
        sql1 = "update bank set money=%s where account=%s"
        money=data[7]+money
        param1 = [money,account]
        update(sql1, param1)
        return True
    else:
        return False
def moneyadd():
    account = int(input("请输入你的账号"))
    while int(math.log10(account) + 1) != 8:
        account = int(input("请输入你的账号"))
    num1=bankmoneyadd(account)
    if num1 == True:
        sql = "select * from bank where account=%s"
        param = [account]
        data = select(sql, param, mode="one")
        info = '''
                ------------存钱信息------------
                            账号:%s
                            存款余额:%s
               '''
        print(info % (data[1], data[7]))
    else:
        print("用户不存在")

def moneyqu():
    account = int(input("请输入你的账号"))
    while int(math.log10(account) + 1) != 8:
        account = int(input("请输入你的账号"))
    password = int(input("请输入你的密码"))
    while int(math.log10(password) + 1) != 6:
        password = int(input("请输入你的密码"))
    num1=bankmoneyqu(account,password)
    if num1 == 0:
        sql = "select * from bank where account=%s and password=%s"
        param = [account,password]
        data = select(sql, param, mode="one")
        info = '''
                ------------取钱信息------------
                            账号:%s
                            存款余额:%s
               '''
        print(info % (data[1], data[7]))
    elif num1 == 1:
        print("账号不存在")
    elif num1 == 2:
        print("密码不对")
    else:
        print("钱不够")

def bankmoneyqu(account,password):
    sql = "select * from bank where account=%s"
    param = [account]
    data = select(sql, param, mode="one")
    if data != None:
        money = int(input("请输入你要取出的金额"))
        sql1 = "select * from bank where account=%s and password=%s"
        param1 = [account,password]
        data1 = select(sql1, param1, mode="one")
        if data1 != None:
            if money > data[7]:
                return 3
            else:
                sql2 = "update bank set money=%s where account=%s and password=%s"
                money=data[7]-money
                param2 = [money,account, password]
                update(sql2, param2)
                return 0
        else:
            return 2
    else:
        return 1


def accountadd():
    account=int(input("请输入你要转出的账号"))
    while int(math.log10(account) + 1) != 8:
        account = int(input("请输入你要转出的账号"))
    account1=int(input("请输入你要转入的账号"))
    while int(math.log10(account1) + 1) != 8:
        account1 = int(input("请输入你要转入的账号"))
    if account == account1:
        print("输入的转出账号与转入账号不能相同")
    password = int(input("请输入你的密码"))
    while int(math.log10(password) + 1) != 6:
        password = int(input("请输入你的密码"))
    num3=bankaccountadd(account,account1,password)
    if num3==1:
        print("转出或转入的账号不存在")
    elif num3==2:
        print("密码输入错误")
    elif num3==3:
        print("钱不够")
    elif num3==0:
        sql = "select * from bank where account=%s and password=%s"
        param = [account, password]
        data = select(sql, param, mode="one")
        sql1 = "select * from bank where account=%s"
        param1 = [account1]
        data1 = select(sql1, param1, mode="one")
        info = '''
                    ------------转账信息------------
                                转出账号:%s
                                密码:******
                                存款余额:%s
                                转入账号:%s
                                存款余额:%s
               '''
        print(info % (data[1], data[7],data1[1], data1[7]))

def bankaccountadd(account,account1,password):
    sql = "select * from bank where account=%s"
    param = [account]
    data = select(sql, param, mode="one")
    print("s",data)
    param1 = [account1]
    data1 = select(sql, param1, mode="one")
    print("a",data1)
    if data != None and data1 != None:
        money = int(input("请输入你要转出的金额"))
        sql2 = "select * from bank where account=%s and password=%s"
        param2 = [account, password]
        data2 = select(sql2, param2, mode="one")
        if data2 != None:
            if data[7]>=money:
                sql2 = "update bank set money=%s where account=%s and password=%s"
                money1=data[7]-money
                param2 = [money1,account, password]
                update(sql2, param2)
                sql3 = "update bank set money=%s where account=%s"
                money2=data1[7]+money
                param3 = [money2, account1]
                update(sql3, param3)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def chaxun():
    account = int(input("请输入你的账号"))
    while int(math.log10(account) + 1) != 8:
        account = int(input("请输入你的账号"))
    password = int(input("请输入你的密码"))
    while int(math.log10(password) + 1) != 6:
        password = int(input("请输入你的密码"))
    num4 = bankchaxun(account, password)
    if num4==1:
        print("账号不存在")
    elif num4==2:
        print("密码输入错误")
    elif num4==0:
        sql = "select * from bank where account=%s and password=%s"
        param = [account,password]
        data = select(sql, param, mode="one")
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

def bankchaxun(account,password):
    sql = "select * from bank where account=%s"
    param = [account]
    data = select(sql, param, mode="one")
    print()
    if data != None:
        sql1 = "select * from bank where account=%s and password=%s"
        param1 = [account, password]
        data1 = select(sql1, param1, mode="one")
        if data1 != None:
            return 0
        else:
            return 2
    else:
        return 1


while True:
    a = int(input("请输入你要办理的业务"))
    if a==1:
        print("开户")
        useradd()
    elif a==2:
        print("存钱")
        moneyadd()
    elif a==3:
        print("取钱")
        moneyqu()
    elif a==4:
        print("转账")
        accountadd()
    elif a==5:
        print("查询")
        chaxun()
    elif a==6:
        print("欢迎下次光临")
        break