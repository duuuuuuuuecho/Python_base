#coding=utf-8
import matplotlib.pyplot as plt
from numpy import *
import MySQLdb

data_spa=zeros((150,220))
data_spa_1=zeros((33000,2))


conn = MySQLdb.connect(     #连接数据库
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='NN_VB_relationship',
)
cur = conn.cursor()

idall = 281
id =1
while id < 282:
    sqli ="select * from n_v_ship where id=%s"%id
    #print sqli
    cur.execute(sqli)
    i = cur.fetchone()
    y = i[0]
    x = i[1]
    #print i[0],i[1]
    data_spa[x,y]=1
    id = id + 1

cur.close()             #关闭游标
conn.commit()           #提交事物，向数据库插入东西必须要这行代码，否则不会真正的进行插入
conn.close()            #关闭数据库连接


for x in range(0,150,1):
    for y in range(0,220,1):
        if data_spa[x,y]==1:
            data_spa_1[220*x+y,0]=x
            data_spa_1[220*x+y,1]=y

fig = plt.figure()
ax1 = fig.add_subplot(111)
#设置标题
ax1.set_title('Noun and Verb -- Scatter Plot')
#设置X轴标签
plt.xlabel(' -------------------Verb-------------------')
#设置Y轴标签
plt.ylabel(' -------------------Noun-------------------')
#画散点图
ax1.scatter(x=data_spa_1[:,0],y=data_spa_1[:,1],c = 'r',marker = 'o')
#设置图标
plt.legend('x1')
#显示所画的图
plt.show()
