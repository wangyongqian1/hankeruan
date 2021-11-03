'''
1.完成衣服销售数据的统计和分析
1.1计算总销售额
1.2计算平均每日销售数量
1.3 计算每个种类月销售量占比
'''
import xlrd
wb=xlrd.open_workbook(filename="C:\\Users\\Administrator\\Desktop\\day7\\任务\\2020年每个月的销售情况.xlsx",encoding_override=True)
sum1,sum2,sum3,count,count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
for i in range(1,13):
    st=wb.sheet_by_name("{}月".format(i))
    price=st.col_values(2)
    num=st.col_values(4)
    num1=st.col_values(0)
    for j in range(len(price)):
        if j>0 :
            sum1+=price[j]*num[j]
            sum1=round(sum1,1)
    print("{}月销售额是".format(i),sum1)
    sum2 = len(num[1:])
    num2=sum(num[1:])
    sum2+=sum2
    num2+=num2
    avg=round(num2/sum2,0)
    sum1+=sum1
    n=st.col_values(1)
    for k in range(len(n)):
        if n[k]=="羽绒服":
            count+=num[k]
        elif n[k]=="牛仔裤":
            count1+=num[k]
        elif n[k]=="风衣":
            count2+=num[k]
        elif n[k]=="皮草":
            count3+=num[k]
        elif n[k]=="T血":
            count4+=num[k]
        elif n[k]=="马甲":
            count5+=num[k]
        elif n[k]=="小西装":
            count6+=num[k]
        elif n[k]=="皮衣":
            count7+=num[k]
        elif n[k]=="衬衫":
            count8+=num[k]
        elif n[k]=="休闲裤":
            count9+=num[k]
        elif n[k]=="卫衣":
            count10+=num[k]
        elif n[k]=="棉衣":
            count11+=num[k]

    y = ('{:.2f}%'.format(count / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    z = ('{:.2f}%'.format(count1 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    f = ('{:.2f}%'.format(count2 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    p = ('{:.2f}%'.format(count3 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    t = ('{:.2f}%'.format(count4 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    m = ('{:.2f}%'.format(count5 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    x = ('{:.2f}%'.format(count6 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    c = ('{:.2f}%'.format(count7 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    s = ('{:.2f}%'.format(count8 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8+ count9 + count10 + count11) * 100))
    xxk = ('{:.2f}%'.format(count9 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 + count10 + count11) * 100))
    wy = ('{:.2f}%'.format(count10 / (count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 + count10 + count11) * 100))
    my = ('{:.2f}%'.format(count11 /(count + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 + count10 + count11) *100))
    print("{}月羽绒服月销售量占比是".format(i), y)
    print("{}月牛仔裤月销售量占比是".format(i), z)
    print("{}月风衣月销售量占比是".format(i), f)
    print("{}月皮草月销售量占比是".format(i), p)
    print("{}月T血月售量占比是".format(i), t)
    print("{}月马甲月销售量占比是".format(i), m)
    print("{}月小西装月销售量占比是".format(i), x)
    print("{}月皮衣月销售量占比是".format(i), c)
    print("{}月衬衫月销售量占比是".format(i), s)
    print("{}月休闲裤月销售量占比是".format(i), xxk)
    print("{}月卫衣月销售量占比是".format(i), wy)
    print("{}月棉衣月销售量占比是".format(i), my)
    print()
print("总销售额是",sum1)
print("平均每日销售数量是",avg)


