#coding=utf-8
import xml.dom.minidom


class Dealxml(object):

    def __init__(self,filepath):
        self.filepath=filepath

    def selectSTR(self):
        dom = xml.dom.minidom.parse(self.filepath)
        root = dom.documentElement
        cc = dom.getElementsByTagName('title')

        return cc


'''
#打开xml文档
#dom = xml.dom.minidom.parse('simplewiki-latest-pages-articles.xml')
dom = xml.dom.minidom.parse('demo.xml')

#得到文档元素对象
root = dom.documentElement
cc = dom.getElementsByTagName('title')


for i in cc:
    print i.firstChild.data
'''

'''
cc=dom.getElementsByTagName('caption')
c1=cc[0]
print c1.firstChild.data

c2=cc[1]
print c2.firstChild.data

c3=cc[2]
print c3.firstChild.data'''

