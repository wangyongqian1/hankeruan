# f=open(file="baidu_x_system.log",mode="r+",encoding="utf-8")
# data=f.readlines()
# count,count1,count2,count3=0,0,0,0
# b=0
# for i in data:
#     a=i[0:13]
#     print(a)
#     b+=1
#     if a=="10.155.24.132":
#         count+=1
#     if a=="16.155.34.132":
#         count1+=1
#     if a=="56.78.35.131 ":
#         count2+=1
#     if a=="46.76.185.36 ":
#         count3+=1
# print("10.155.24.132出现",count,"次，16.155.34.132出现",count1,"次，56.78.35.131出现",count2,"次，46.76.185.36出现",count3,"次")
# print(b)


# import re
# ips={}
# log=open(file="baidu_x_system.log",mode="r+",encoding="utf-8")
# for i in log:
#     ip=re.search('(\d+.){3}\d+',i)
#     print(ip)
#     if ip:
#         ip=ip.group()
#         ips[ip]=ips.get(ip,0)+1
# print(ips)

f=open(file="baidu_x_system.log",mode="r+",encoding="utf-8")
d=f.readlines()
list=[]
for i in d:
    list.append(i[0:13])
for j in list:
    print(j,"=>","{}".format(list.count(j)))
    while True:
        if j in list:
            list.remove(j)
        else:
            break