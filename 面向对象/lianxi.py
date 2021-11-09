'''
定义一个空调类和对应的测试类
'''
# import time
#
# class Kongtiao:
#     __brand=""
#     __price=0
#
#     def setBrand(self,brand):
#         if brand=="":
#             print("空调的品牌不能为空")
#         else:
#             self.__brand=brand
#
#     def getBrand(self):
#         return self.__brand
#
#     def setPrice(self,price):
#         if price<0:
#             print("空调的价格输入错误")
#         else:
#             self.__price=price
#
#     def getPrice(self):
#         return self.__price
#
#     def showkongtiao(self):
#         print(self.__brand,"空调的价格是",self.__price)
#
#     def start(self):
#         print("空调开机了")
#
#     def stop(self,t):
#         time.sleep(t*60)
#         print("空调将在",t,"分钟后自动关闭")
#
# k=Kongtiao()
# k.setBrand("海尔")
# k.setPrice(2000)
# k.showkongtiao()
# k.start()
# k.stop(1)

'''
定义一个学生类和对应的测试类
'''
# class Student:
#     __name=""
#     __age=0
#
#     def setName(self,name):
#         if name=="":
#             print("学生姓名不能为空")
#         else:
#             self.__name=name
#
#     def getName(self):
#         return self.__name
#
#     def setAge(self,age):
#         if age<=0 or age>30:
#             print("学生的年龄输入错误")
#         else:
#             self.__age=age
#
#     def getAge(self):
#         return self.__age
#
#     def showstudent(self):
#         print("大家好，我叫",self.__name,"，今年",self.__age,"岁了！")
#
#     def bi(self,Student):
#         if self.__age>student.getAge():
#             print("我比同桌大",self.__age-student.getAge(),"岁！")
#         elif self.__age<student.getAge():
#             print("我比同桌小",student.getAge()-self.__age,"岁！")
#         else:
#             print("我和同桌一样大！")
#
# s=Student()
# s.setName("张三")
# s.setAge(19)
# s.showstudent()
# s1=Student()
# s1.setName("李四")
# s1.setAge(21)
# s.bi(s1)

'''
打电话业务逻辑
'''
# class Person:
#     __name=""
#     __sex=""
#     __age=""
#     __huafei=0.0
#     __brand=""
#     __rongliang=0
#     __screen=0.0
#     __waittime=0
#     __score=0
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
#     def setSex(self,sex):
#         if sex !="男" and sex !="女":
#             print("你是人妖吗？")
#         elif sex=="":
#             print("性别不能为空")
#         else:
#             self.__sex=sex
#
#     def getSex(self):
#         return self.__sex
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
#     def setHuafei(self,huafei):
#         if huafei<0:
#             print("话费输入非法")
#         else:
#             self.__huafei=huafei
#
#     def getHuafei(self):
#         return self.__huafei
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
#     def setRongliang(self, rongliang):
#         if rongliang <= 0:
#             print("容量输入非法")
#         else:
#             self.__rongliang=rongliang
#
#     def getRongliang(self):
#         return self.__rongliang
#
#     def setScreen(self, screen):
#         if screen<=0:
#             print("屏幕输入非法")
#         else:
#             self.__screen=screen
#
#     def getScreen(self):
#         return self.__screen
#
#     def setWaittime(self, waittime):
#         if waittime <= 0:
#             print("待机时间输入非法")
#         else:
#             self.__waittime=waittime
#
#     def getWaittime(self):
#         return self.__waittime
#
#     def setScore(self, score):
#         if score<0:
#             print("积分输入非法")
#         else:
#             self.__score=score
#
#     def getScore(self):
#         return self.__score
#
#     def duanxin(self,neirong):
#         print(self.__name,"发送短信",neirong)
#
#     def phone(self,num,t):
#         if num=="":
#             print("手机号码不能为空")
#         if self.__huafei<1:
#             print("手机欠费")
#         if num !="" and self.__huafei>1:
#             print("手机已拨通")
#         if t>0 and t<=10:
#             s=self.__huafei-t
#             self.setHuafei(s)
#             j=t*15
#             self.setScore(j)
#         elif t>10 and t<=20:
#             s = self.__huafei - t*0.8
#             self.setHuafei(s)
#             j=t*39
#             self.setScore(j)
#         else:
#             s = self.__huafei - t * 0.65
#             self.setHuafei(s)
#             j = t * 48
#             self.setScore(j)
#
#     def showperson(self):
#         print(self.__name,"，性别是",self.__sex,"，年龄是",self.__age,"，所拥有的手机剩余话费是",self.__huafei,
#               "，手机品牌是",self.__brand,"，手机电池容量是",self.__rongliang,"V，手机屏幕大小是",self.__screen,
#               "寸，手机最大待机时长是",self.__waittime,"小时，所拥有的积分是",self.__score)
#
# p = Person()
# name=input("请输入你的姓名")
# p.setName(name)
# sex=input("请输入你的性别")
# p.setSex(sex)
# age=int(input("请输入你的年龄"))
# p.setAge(age)
# huafei=float(input("请输入你所拥有的手机剩余话费"))
# p.setHuafei(huafei)
# brand=input("请输入你的手机品牌")
# p.setBrand(brand)
# rongliang=int(input("请输入你的手机电池容量"))
# p.setRongliang(rongliang)
# screen=float(input("请输入你的手机屏幕大小"))
# p.setScreen(screen)
# waittime=int(input("请输入你的手机最大待机时长"))
# p.setWaittime(waittime)
# score=int(input("请输入你所拥有的积分"))
# p.setScore(score)
# p.showperson()
# while True:
#     a = int(input("请选择你要办理的业务"))
#     if a==1:
#         print("发短信")
#         n=input("请输入你要发送的短信内容")
#         p.duanxin(n)
#     else:
#         print("打电话")
#         p.phone("12345678901",12)
#         p.showperson()

'''
i.	定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
行为：学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名），编程（要求参数传入写代码的行数）
，数的求和（要求参数用变长参数来做，返回求和结果）
'''
# class Student:
#     __sid=0
#     __name=""
#     __age=0
#     __sex=""
#     __height=0.00
#     __weight=0
#     __score=0
#     __address=""
#     __phone=""
#
#     def setSid(self,sid):
#         if sid==0:
#             print("学号输入非法")
#         else:
#             self.__sid=sid
#
#     def getSid(self):
#         return self.__sid
#
#     def setName(self, name):
#         if name=="":
#             print("姓名不能为空")
#         else:
#             self.__name=name
#
#     def getName(self):
#         return self.__name
#
#     def setSex(self,sex):
#         if sex !="男" and sex !="女":
#             print("你是人妖吗？")
#         elif sex=="":
#             print("性别不能为空")
#         else:
#             self.__sex=sex
#
#     def getSex(self):
#         return self.__sex
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
#     def setHeight(self,height):
#         if height<=0 or height>2.4:
#             print("身高输入非法")
#         else:
#             self.__height=height
#
#     def getHeight(self):
#         return self.__height
#
#     def setWeight(self,weight):
#         if weight<=0 or weight>400:
#             print("体重输入非法")
#         else:
#             self.__weight=weight
#
#     def getWeight(self):
#         return self.__weight
#
#     def setScore(self,score):
#         if score<=0 or score>100:
#             print("成绩输入非法")
#         else:
#             self.__score=score
#     def getScore(self):
#         return self.__score
#
#     def setAddress(self,address):
#         if address=="":
#             print("地址不能为空")
#         else:
#             self.__address=address
#
#     def getAddress(self):
#         return self.__address
#
#     def setPhone(self,phone):
#         if phone=="" :
#             print("电话号码不能为空")
#         elif len(phone) != 11:
#             print("电话号码输入非法")
#         else:
#             self.__phone=phone
#
#     def getPhone(self):
#         return self.__phone
#
#     def study(self,hour):
#         print(self.__name,"学习了",hour,"个小时")
#
#     def play(self,game):
#         print(self.__name,"玩了",game,"游戏")
#
#     def bian(self,line):
#         print(self.__name,"写了",line,"行代码")
#     def he(self,*sum):
#         sum1=0
#         for i in sum:
#             sum1+=i
#         print(self.__name,"求出",sum,"的和是",sum1)
#
#     def showstudent(self):
#         print("学号",self.__sid,"，姓名",self.__name,"，性别",self.__sex,"，年龄",self.__age,"，身高",self.__height,"米，体重"
#               ,self.__weight,"kg，成绩",self.__score,"分，地址",self.__address,"，电话号码",self.__phone)
#
# s=Student()
# sid=int(input("请输入你的学号"))
# s.setSid(sid)
# name=input("请输入你的姓名")
# s.setName(name)
# sex=input("请输入你的性别")
# s.setSex(sex)
# age=int(input("请输入你的年龄"))
# s.setAge(age)
# height=float(input("请输入你的身高"))
# s.setHeight(height)
# weight=int(input("请输入你的体重"))
# s.setWeight(weight)
# score=int(input("请输入你的成绩"))
# s.setScore(score)
# address=input("请输入你的地址")
# s.setAddress(address)
# phone=input("请输入你的电话号码")
# s.setPhone(phone)
# s.showstudent()
# s.study(8)
# s.play("吃鸡")
# s.bian(2)
# s.he(1,13,5)

'''
车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。功能：跑（要求参数传入车的具体功能，比如越野，赛车）
'''
# class Car:
#     __brand=""
#     __num=0
#     __color=""
#     __weight=0.00
#     __you=0.00
#
#     def setBrand(self,brand):
#         if brand=="":
#             print("车型号不能为空")
#         else:
#             self.__brand=brand
#
#     def getBrand(self):
#        return self.__brand
#
#     def setNum(self, num):
#         if num <=1:
#             print("车轮数输入非法")
#         else:
#             self.__num=num
#
#     def getNum(self):
#         return self.__num
#
#     def setColor(self, color):
#         if color == "":
#             print("车身颜色不能为空")
#         else:
#             self.__color=color
#
#     def getColor(self):
#         return self.__color
#
#     def setWeight(self, weight):
#         if weight<0 or weight>20:
#             print("车重量输入非法")
#         else:
#             self.__weight=weight
#
#     def getWeight(self):
#         return self.__weight
#
#     def setYou(self, you):
#         if you<0 or you>100:
#             print("油箱存储大小输入非法")
#         else:
#             self.__you=you
#
#     def getYou(self):
#         return self.__brand
#
#     def run(self,gong):
#         print(self.__brand,"可以",gong)
#
#     def showcar(self):
#         print(self.__brand,"有",self.__num,"个车轮，车身颜色",self.__color,",车重量",self.__weight,"吨，油箱可以存储",self.__you,"升的油")
#
# c=Car()
# c.setBrand("法拉利")
# c.setNum(4)
# c.setColor("红色")
# c.setWeight(4)
# c.setYou(50)
# c.showcar()
# c.run("赛车")
# c1=Car()
# c1.setBrand("宝马")
# c1.run("赛车")
# c2=Car()
# c2.setBrand("铃木")
# c2.run("越野")
# c3=Car()
# c3.setBrand("五菱")
# c3.run("运输")
# c4=Car()
# c4.setBrand("拖拉机")
# c4.run("种地")

'''
笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公。
'''
# class Computer:
#     __xinghao=""
#     __waittime=0
#     __color=""
#     __weight=0.00
#     __cpu=""
#     __neicun=0
#     __yingpan=0
#
#     def setXinghao(self,xinghao):
#         if xinghao=="":
#             print("型号不能为空")
#         else:
#             self.__xinghao=xinghao
#
#     def getXinghao(self):
#         return self.__xinghao
#
#     def setWaittime(self,waittime):
#         if waittime<=0:
#             print("待机时间输入非法")
#         else:
#             self.__waittime=waittime
#
#     def getWaittime(self):
#         return self.__waittime
#
#     def setColor(self, color):
#         if color == "":
#             print("颜色不能为空")
#         else:
#             self.__color=color
#
#     def getColor(self):
#         return self.__color
#
#     def setWeight(self, weight):
#         if weight<=0 or weight>30:
#             print("重量输入非法")
#         else:
#             self.__weight=weight
#
#     def getWeight(self):
#         return self.__weight
#
#     def setCpu(self, cpu):
#         if cpu == "":
#             print("cpu型号不能为空")
#         else:
#             self.__cpu=cpu
#
#     def getCpu(self):
#         return self.__cpu
#
#     def setNeicun(self, nenicun):
#         if nenicun<0:
#             print("内存大小输入非法")
#         else:
#             self.__neicun=nenicun
#
#     def getNeicun(self):
#         return self.__neicun
#
#     def setYingpan(self, yingpan):
#         if yingpan<=0:
#             print("硬盘大小输入非法")
#         else:
#             self.__yingpan=yingpan
#
#     def getYingpan(self):
#         return self.__yingpan
#
#     def play(self, game):
#         print("使用笔记本电脑可以打",game)
#
#     def work(self, name):
#         print("使用笔记本电脑可以",name)
#
#     def showcomputer(self):
#         print("笔记本电脑的型号是",self.__xinghao,",待机时间",self.__waittime,"小时，颜色是",self.__color,"，重量是",
#               self.__weight,"cpu型号是",self.__cpu,"kg，内存大小是",self.__neicun,"G，硬盘大小是",self.__yingpan,"G")
#
# c=Computer()
# c.setXinghao("联想T430")
# c.setWaittime(48)
# c.setColor("黑色")
# c.setWeight(20.55)
# c.setCpu("英特尔")
# c.setNeicun(128)
# c.setYingpan(64)
# c.showcomputer()
# c.play("王者荣耀")
# c.work("开发软件")

'''
猴子类：属性：类别，性别，身体颜色，体重。行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
'''
class Monkey:
    __lei=""
    __sex=""
    __color=""
    __weight=0

    def setLei(self,lei):
        if lei=="":
            print("类别不能为空")
        else:
            self.__lei=lei

    def getLei(self):
        return self.__lei

    def setSex(self,sex):
        if sex !="雌性" and sex !="雄性":
            print("你是猴妖吗")
        else:
            self.__sex=sex

    def getSex(self):
        return self.__sex

    def setColor(self,color):
        if color=="":
            print("身体颜色不能为空")
        else:
            self.__color=color

    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        if weight<=0 or weight>100:
            print("体重输入非法")
        else:
            self.__weight=weight

    def getWeight(self):
        return self.__weight

    def huo(self,kind):
        print(self.__lei,"可以使用",kind,"造火")

    def study(self,data):
        for i in range(len(data)):
            print(self.__lei, "可以学习", data[i])

    def showmonkey(self):
        print(self.__lei,"是",self.__sex,"，身体颜色是",self.__color,"，体重是",self.__weight,"kg")

m=Monkey()
m.setLei("猩猩")
m.setSex("雄性")
m.setColor("黑色")
m.setWeight(100)
m.showmonkey()
m.huo("木头")
data=["爬树","剥香蕉"]
m.study(data)
