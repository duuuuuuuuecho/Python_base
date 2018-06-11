#!/usr/bin/evn python
# coding:utf-8


import xml.etree.cElementTree as ET
import os
from nltk import sent_tokenize

#获取文章-摘要对
def getDom_summary(fpath):
    dom = ''
    sum = ''
    for event, elem in ET.iterparse(fpath, events=('start',)):
        if elem.tag == 'headline':
            sum = elem.text.replace('\n', '')
        if elem.tag == 'p':
            dom += elem.text.replace('\n', '')

        elem.clear()

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


#遍历整个文件夹
#写入文件
def  eachFile(filepath,wpath,i):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        if judgeRfile(allDir):
            child = os.path.join(filepath, allDir)
            if os.path.isdir(child):
                print i
                i = i + 1
                eachFile(child, wpath,i)
            else:
                a, b = getDom_summary(child)
                insertfile(wpath, b)
                insertfile(wpath, a)
        else:

            continue



#判断文件是否是想要的文件
def judgeRfile(fpath):
    name = fpath;
    if name[0] == 'R':
        return True
    else :
        return False


if __name__=="__main__":
    i = 1
    eachFile('data/raw_topics/','textdemo1.txt',i)

    '''
    body = "Fifty-seven people spent Christmas aboard a cruise ship that has become stuck in the ice in a remote region off the coast of Antarctica and rescue vessels are at least two days away, Australian maritime officials told ABC News.The Russian-operated Akademik Shokalskiy, an ice-strengthened vessel built in 1984 for oceanographic research, became stuck in the ice about 1,500 nautical miles from Hobart, Tasmania, and issued a satellite distress call early this morning,  Andrea Hayward-Maher of the Australian Maritime Safety Authority said.  We  ve been in touch with the master of the vessel, who says they are beset by ice,   spokeswoman Hayward-Maher said.   They are basically trapped or stuck in the ice and can  t move.  Passengers are believed to have enough provisions to wait out their rescue. One passenger tweeted that all on board were fine and their   spirits high.    We  re in the ice like the explorers of old! All are well and spirits are high. Happy Christmas,   Australian professor Chris Turney tweeted.The ship is too far from land to send aircraft or normal rescue vessels, Hayward-Maher said. Three ships with ice-breaking capabilities in the region have   been tasked with helping,   but they are all a two-day sail from the stuck vessel,   she added.  This is quite a complex and lengthy search-and-rescue operation because of the remote location of the area,   Hayward-Maher said.Of the 57 souls on board, 22 are crewmen and 35 are passengers. The ship cruised to the site of a 1911-1914 expedition of British explorer Sir Douglas Mawson, according to Expeditions Online, a travel agency that sells tickets for the cruise."
    sentences = sent_tokenize(body)
    body = '<d> <p> ' + ' '.join(['<s> ' + sentence + ' </s>' for sentence in sentences]) + ' </p> </d>'
    print body
    '''

    '''
    a,b = getDom_summary('demo.xml')
    insertfile('textdemo1.txt',a)
    insertfile('textdemo1.txt',b)
    '''

