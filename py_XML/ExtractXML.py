#coding=utf-8
#抽取<text>标签中的内容 存入txt文件中

#!!!      <text><\text>中不能换行

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xml.sax

class textHandle(xml.sax.ContentHandler):

    def __init__(self):
        self.Data = ""
        self.text = ""

    # 元素开始事件处理
    def startElement(self,tag ,attributes):
        self.Data = tag

    # 元素结束事件处理
    def endElement(self, tag):
        if self.Data == "text":
            print self.text
            '''
            f = file("text.txt","a+")
            f.write(self.text)
            f.write("\n")
            f.close()
            '''
        self.Data = ""

    # 内容事件处理
    def characters(self, content):
        if self.Data =="text":
            self.text = content

if __name__ == "__main__":
    #创建一个 XMLReader
    parser = xml.sax.make_parser()
    #turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    #重写ContextHandler
    Handler = textHandle()
    parser.setContentHandler(Handler)

    parser.parse("demo.xml")