#!/usr/bin/evn python
#coding:utf-8

#处理 小型xml文档

import  xml.dom.minidom
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
#打开xml文档
dom = xml.dom.minidom.parse('demo.xml')

#得到文档元素对象
root = dom.documentElement

cc=dom.getElementsByTagName('text')

for c in cc:
   # print c.firstChild.data
    f = file("sentence.txt","a+")
    f.write(c.firstChild.data)
    f.write("\n")
    f.close()
'''

def extractSome(fpath,wpath):
    dom = xml.dom.minidom.parse(fpath)
    root = dom.documentElement
    cc = dom.getElementsByTagName('sentence')
    for c in cc:
        # print c.firstChild.data
        f = file(wpath, "a+")
        print c.firstChild.data

      #  f.write(c.firstChild.data)
        #f.write("\n")
        f.close()

def eachFile(filepath,wpath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        extractSome(child,wpath)



if __name__=="__main__":
    eachFile("demo\\","sentence.txt")