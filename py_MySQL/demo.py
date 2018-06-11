#coding=utf-8
# 筛选出 xml文件中 title标签中间的数据  将其依次存入数据库

#  成功
import MySQLdb
import  xml.dom.minidom

class Dealxml(object):

    def __init__(self,filepath):
        self.filepath=filepath

    def selectSTR(self):
        dom = xml.dom.minidom.parse(self.filepath)
        root = dom.documentElement
        cc = dom.getElementsByTagName('title')

        return cc

f_xml = Dealxml(r"demo.xml")
Q=f_xml.selectSTR()

for z in Q:
    print z.firstChild.data

conn = MySQLdb.connect(     #连接数据库
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='demo1',
)
cur = conn.cursor()

#数据插入数据库
sql ="insert into words values(%s,%s)"
i=1
for w in Q:
    param = (i,w.firstChild.data)
    cur.execute(sql,param)
    i=i+1



   # print i.firstChild.data


cur.close()             #关闭游标
conn.commit()           #提交事物，向数据库插入东西必须要这行代码，否则不会真正的进行插入
conn.close()            #关闭数据库连接