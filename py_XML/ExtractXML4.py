#!/usr/bin/evn python
#coding:utf-8
#处理大型xml文件   success
import xml.sax
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

'''
def insertfile(fpath, Wstr):
    f = file(fpath, "a+")
    f.write(Wstr)
    f.write("\n")
    f.close()

class xmlContentHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self.data = ""
        self.text = ""

    def startDocument(self):
        print("start ************")
    def endDocument(self):
        print("end ************")

    def startElement(self,name,attrs):
        self.data = name

    def characters(self,content):
        if self.data=="text":
            content =content.strip().replace("\n","").replace("\r","")
            if "" != content:
                print content
                insertfile("text.txt",content)

saxParser = xml.sax.make_parser()
handler = xmlContentHandler()
saxParser.setContentHandler(handler)
saxParser.parse("simplewiki.xml")
'''

def insertfile(fpath, Wstr):
    f = file(fpath, "a+")
    f.write(Wstr)
    f.write("\n")
    f.close()


class xmlContentHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self.data = ""
        self.text = ""

    def startDocument(self):
        print("start ************")
    def endDocument(self):
        print("end ************")

    def startElement(self,name,attrs):
        self.data = name

    def characters(self,content):
        if self.data=="sentence":
            content =content.strip().replace("\n","").replace("\r","")
            if "" != content:
                print content
                insertfile("sentence.txt",content)

saxParser = xml.sax.make_parser()
handler = xmlContentHandler()
saxParser.setContentHandler(handler)

filepath="demo\\"
pathDir = os.listdir(filepath)
for allDir in pathDir:
    child = os.path.join('%s%s' % (filepath, allDir))
    saxParser.parse(child)