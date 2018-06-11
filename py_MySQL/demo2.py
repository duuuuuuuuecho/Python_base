#coding=utf-8
#!/usr/bin/python
#    success 存入数据库

import sys             #处理非法输入编码问题    26-28行
reload(sys)
sys.setdefaultencoding('utf-8')

import xml.sax
import MySQLdb
import re

class CountryHandler(xml.sax.ContentHandler):


    def insertMysql(self,stringtxt):
        conn = MySQLdb.connect(  # 连接数据库
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='thesaurus',
        )

        cur = conn.cursor()

        line1=re.sub("<.*?>", "", stringtxt)
        line1=line1.strip()
        line2=line1.decode('ascii','ignore')                     #忽略非法输入
        if line2:
            sql = "insert into Entrys(entry) values(%s)"
            param = (line2)
            cur.execute(sql,[param])

        #sql = "insert into wordss values(%s,%s)"
        #param = (num,stringtxt)
        #cur.execute(sql,param)

        cur.close()
        conn.commit()
        conn.close()

    def __init__(self):
     self.CurrentData = ""
     self.title = ""



# 元素开始事件处理
    def startElement(self, tag, attributes):
      self.CurrentData = tag

# 元素结束事件处理

    def endElement(self,tag):
      if self.CurrentData == "title":
          print  self.title
          self.insertMysql(self.title)

      self.CurrentData = ""

# 内容事件处理
    def characters(self, content):
      if self.CurrentData == "title":
          self.title = content

if __name__ == "__main__":
# 创建一个 XMLReader
    parser = xml.sax.make_parser()
# turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# 重写 ContextHandler
    Handler = CountryHandler()
    parser.setContentHandler(Handler)

    parser.parse("simplewiki-latest-pages-articles.xml")



