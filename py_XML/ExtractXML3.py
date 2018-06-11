#!/usr/bin/evn python
# coding:utf-8
#只能处理小型 xml文件


import xml.etree.cElementTree as ET


def insertfile(fpath, Wstr):
    f = file(fpath, "a+")
    f.write(Wstr)
    f.write("\n")
    f.close()


for event, elem in ET.iterparse('demo.xml', events=('end',)):
    if elem.tag == 'text':
        print(elem.text)
        #   insertfile("text.txt",elem.text)
    elem.clear()


