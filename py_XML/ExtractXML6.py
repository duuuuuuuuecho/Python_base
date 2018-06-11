#!/usr/bin/evn python
# coding:utf-8

import xml.etree.cElementTree as ET
import os
from nltk import sent_tokenize

#获取文章-摘要对
def getDom_summary(fpath):

    replace01File(fpath, '&', '')

    dom = ''
    dom1 = ''
    dom2 = ''
    sum = ''
    for event, elem in ET.iterparse(fpath, events=('start',)):
        if elem.tag == 'HEADLINE':
            sum = elem.text.replace('\n', '')
        if elem.tag == 'TEXT':
            dom1 = elem.text.replace('\n', '')
        if elem.tag == 'P':
            dom2 += elem.text.replace('\n', '')
        elem.clear()
    if len(dom1) == 0:
        dom = dom2
    else:
        dom = dom1

    
    sentences = sent_tokenize(sum)
    sum = '<d> <p> ' + ' '.join(['<s> ' + sentence + ' </s>' for sentence in sentences]) + ' </p> </d>'
    sentencess = sent_tokenize(dom)
    dom = '<d> <p> ' + ' '.join(['<s> ' + sentence + ' </s>' for sentence in sentencess]) + ' </p> </d>'

    sum = 'abstract=' + sum + '\t'
    dom = 'article=' + dom + '\n'




    return dom,sum

 #将字符串按行写入文件中
def insertfile(fpath, Wstr):
    f = file(fpath, "a+")
    f.write(Wstr)
    f.close()


#用字符串 str1替换 str0
def replace01File(fpath,str0,str1):
    try:
        lines = open(fpath,'r').readlines()
        flen = len(lines) - 1
        for i in range(flen):
            if str0 in lines[i]:
                lines[i] = lines[i].replace(str0,str1)
        open(fpath,'w').writelines(lines)
    except Exception,e:
        print e

#遍历整个文件夹
#写入文件
def  eachFile(filepath,wpath,i):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        if os.path.isdir(child):
            print i
            i = i + 1
            eachFile(child, wpath,i)
        else:
            print child
            a, b = getDom_summary(child)
            insertfile(wpath, b)
            insertfile(wpath, a)






if __name__=="__main__":
    fpath = 'data/duc2007'
    i = 1
    eachFile(fpath,'textdemo2.txt',i)

'''
    dom = ''
    dom1 = ''
    dom2 = ''
    sum = ''
    for event, elem in ET.iterparse(fpath, events=('start',)):
        if elem.tag == 'HEADLINE':
            sum = elem.text.replace('\n', '')
        if elem.tag == 'TEXT':
            dom1 = elem.text.replace('\n', '')
        if elem.tag == 'P':
            dom2 += elem.text.replace('\n', '')

    if len(dom1) == 0:
        dom = dom2
    else:
        dom = dom1

    print dom
'''

