import random
import math
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
bank={'q': {'account': 77902180, 'password': 123456, 'country': 'd', 'province': 'f', 'street': 'g', 'door': '1', 'money': 0, 'bank_name': '中国工商银行'}, 's': {'account': 12345678, 'password': 123456, 'country': 't', 'province': 'a', 'street': 'f', 'door': '5', 'money': 0, 'bank_name': '中国工商银行'}}
bank_name="中国工商银行"
print(bank)

def bankadd(account,name,password,country,province,street,door):
    if len(bank)>100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
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
        info='''
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
        print(info%(name,account,country,province,street,door,bank[name]["money"],bank_name))
    elif num==2:
        print("用户已存在")
    elif num==3:
        print("本银行已满，请到其他银行开户")

def bankmoneyadd(account):
    name=""
    for key,values in bank.items():
        if account==bank[key]["account"]:
            name=key
            money = int(input("请输入你要存取的金额"))
            bank[name]["money"]+=money
            return True
    if name=="":
        return False
def moneyadd():
    account = int(input("请输入你的账号"))
    while int(math.log10(account) + 1) != 8:
        account = int(input("请输入你的账号"))
    num1=bankmoneyadd(account)
    if num1 == True:
        for key, values in bank.items():
            if account == bank[key]["account"]:
                name = key
        info = '''
                   ------------个人信息------------
                               账号:%s               
                               密码：*****
                               存款余额：%s
               '''

        print(info % (account, bank[name]["money"]))
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
        for key, values in bank.items():
            if account==bank[key]["account"]:
                name = key
        info = '''
               ------------个人信息------------
                           账号:%s               
                           密码：*****
                           存款余额：%s
               '''

        print(info % (account, bank[name]["money"]))
    elif num1 == 1:
        print("账号不存在")
    elif num1 == 2:
        print("密码不对")
    else:
        print("钱不够")

def bankmoneyqu(account,password):
    name=""
    for key, values in bank.items():
        if account==bank[key]["account"]:
            name = key
    if name=="":
        return 1
    if password == bank[name]["password"]:
        money = int(input("请输入你要取出的金额"))
        if money > bank[name]["money"]:
            return 3
        else:
            bank[name]["money"] = bank[name]["money"] - money
            return 0
    else:
        return 2


def accountadd():
    account=int(input("请输入你要转出的账号"))
    while int(math.log10(account) + 1) != 8:
        account = int(input("请输入你要转出的账号"))
    account1=int(input("请输入你要转入的账号"))
    while int(math.log10(account1) + 1) != 8:
        account1 = int(input("请输入你要转入的账号"))
    if account != account1:
        for key, values in bank.items():
            if account==bank[key]["account"]:
                name = key
            if account1==bank[key]["account"]:
                name1 = key
    else:
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
        for key, values in bank.items():
            if account==bank[key]["account"]:
                name = key
            if account1==bank[key]["account"]:
                name1 = key
        info = '''
                   ------------个人信息------------
                           转出用户性名:%s               
                           密码：*****
                           转出账号:%s
                           转出账号余额：%s
                           开户行名称：%s
                           转入用户性名:%s               
                           转入账号:%s
                           转入账号余额：%s
               '''

        print(info % (name,account,bank[name]["money"],bank_name,name1,account1,bank[name1]["money"]))


def bankaccountadd(account,account1,password):
    name,name1="",""
    for key, values in bank.items():
        if account==bank[key]["account"]:
            name=key
        if account1==bank[key]["account"]:
            name1 = key
    money = int(input("请输入你要转出的金额"))
    if name == "":
        return 1
    if name1 == "":
        return 1
    if password == bank[name]['password']:
        if money <= bank[name]['money']:
            bank[name]['money'] = bank[name]['money'] - money
            bank[name1]['money'] = bank[name1]['money'] + money
            return 0
        else:
            return 3
    if password != bank[name]['password']:
        return 2





def select():
    account = int(input("请输入你的账号"))
    while int(math.log10(account) + 1) != 8:
        account = int(input("请输入你的账号"))
    password = int(input("请输入你的密码"))
    while int(math.log10(password) + 1) != 6:
        password = int(input("请输入你的密码"))
    num4 = bankselect(account, password)
    if num4==1:
        print("账号不存在")
    elif num4==2:
        print("密码输入错误")
    elif num4==0:
        for key, values in bank.items():
            if account==bank[key]["account"]:
                name = key
        info = '''
                          ------------个人信息------------
                          用户名:%s
                          账号：%s
                          密码：******
                          国籍：%s
                          省份：%s
                          街道：%s
                          门牌号：%s
                          余额：%s
                          开户行名称：%s
               '''

        print(info % (name, bank[name]['account'], bank[name]['country'], bank[name]['province'],
                      bank[name]['street'], bank[name]['door'], bank[name]["money"], bank_name))


def bankselect(account,password):
    name = ""
    for key,values in bank.items():
        if account==bank[key]["account"]:
            name=key
    if name=="":
        return 1
    if password==bank[name]["password"]:
        return 0
    else:
        return 2


while True:
    a = int(input("请输入你要办理的业务"))
    if a==1:
        print("开户")
        useradd()
        print(bank)
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
        select()
    elif a==6:
        print("欢迎下次光临")
        break