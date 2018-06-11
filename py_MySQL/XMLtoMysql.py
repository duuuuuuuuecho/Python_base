#coding=utf-8
#内存溢出     @#$#$@%@^%$&#$&^$&(*%^@#%@



import MySQLdb
import  xml.dom.minidom             #一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里

class Dealxml(object):

    def __init__(self,filepath):
        self.filepath=filepath

    def selectSTR(self):
        dom = xml.dom.minidom.parse(self.filepath)
        root = dom.documentElement
        cc = dom.getElementsByTagName('title')

        return cc

conn = MySQLdb.connect(     #连接数据库
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='entry',
)
cur = conn.cursor()

f_xml = Dealxml(r"simplewiki-latest-pages-articles.xml")
Q=f_xml.selectSTR()

#数据插入数据库
sql ="insert into thesaurus values(%s,%s)"
i=1
for w in Q:
    param = (i,w.firstChild.data)
    cur.execute(sql,param)
    i=i+1


cur.close()             #关闭游标
conn.commit()           #提交事物，向数据库插入东西必须要这行代码，否则不会真正的进行插入
conn.close()            #关闭数据库连接




