#coding=utf-8
#依存句法分析
#将句子进行句法分析  抽取出相互有关系的名词与动词 存入数据库 success

from nltk.stem import SnowballStemmer                          #词原
from nltk.parse.stanford import StanfordDependencyParser
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#定义全局变量  用于数据库
#    noun            verb        ship
#id  word        id  word      nid   vid
#**  ****        **  ****      **    **
#**  ****        **  ****      **    **
#**  ****        **  ****      **    **
#**  ****        **  ****      **    **
NID = 1
VID = 1

'''
eng_parser = StanfordDependencyParser("D:\stanford\stanfordnltk\stanford-parser.jar","D:\stanford\stanfordnltk\stanford-parser-3.6.0-models.jar")
res = list(eng_parser.parse(" ".split()))      #返回list


for row in res[0].triples():
    print(row)
'''

def sentenceAnalysis(sentence1):
    eng_parser = StanfordDependencyParser("D:\stanford\stanfordnltk\stanford-parser.jar",
                                          "D:\stanford\stanfordnltk\stanford-parser-3.6.0-models.jar")
    res = list(eng_parser.parse(sentence1.split()))  # 返回list
    return res

#判断名词
def judgeNN(str1):
    if str1 == 'NN' or str1 == 'NNS' or str1 == 'NNP' or str1 == 'NNPS' :
        return True
    else:
        return False

#判断动词
def judgeVB(str2):
    if str2 == 'VB' or str2 == 'VBD' or str2 == 'VBG' or str2 == 'VBN'or str2 == 'VBZ':
        return True
    else:
        return False

#获得词的原型
def Realword(rword):
    snowball_stemmer = SnowballStemmer("english")
    return snowball_stemmer.stem(rword)

#数据库操作
def insertMysql(Nword,Vword):
    global NID
    global VID

    conn = MySQLdb.connect(  # 连接数据库
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='NN_VB_relationship',
    )

    cur = conn.cursor()

    def exist_no_n(word):  # 判断单词是否存在在noun表中
        sqli = "select * from noun where word='" + word + "'"
        cur.execute(sqli)
        if cur.fetchone():
            return True
        else:
            return False

    def exist_no_v(word):  # 判断单词是否存在在verb表中
        sqli ="select * from verb where word='" + word + "'"
        cur.execute(sqli)
        if cur.fetchone():
            return True
        else:
            return False
    '''
    def insertdata_N(id1, word, id2):  # 给noun插数据
        sqli = "insert into noun values(%s,%s,%s)"
        id11 = id1
        word1 = "'" + word + "'"
        id22 = id2
        cur.execute(sqli, (id11, word1, id22))

    def insertdata_V(id1, word, id2):  # 给verb插数据
        sqli = "insert into verb values(%s,%s,%s)"
        id11 =  id1
        word1 = "'" + word + "'"
        id22 =  id2
        cur.execute(sqli, (id11, word1, id22))
    '''

    def insertdata_n(id1, word):        # 给noun插数据
        sqli = "insert into noun values(%s,%s)"
        id11 = id1
        cur.execute(sqli, (id11, word))

    def insertdata_v(id1, word):        # 给verb插数据
        sqli = "insert into verb values(%s,%s)"
        id11 = id1
        cur.execute(sqli, (id11, word))

    def insertship(id1,id2):             #加关系
        sqli = "insert into n_v_ship values(%s,%s)"
        cur.execute(sqli,(id1,id2))


    def n_exist_id(word):                # 名词单词存在，返回id
        sqli ="select id from noun where word='" + word + "'"
        cur.execute(sqli)
        i = cur.fetchone()
        return i[0]

    def v_exist_id(word):                # 动词单词存在，返回id
        sqli ="select id from verb where word='" + word + "'"
        cur.execute(sqli)
        i = cur.fetchone()
        return i[0]




    if exist_no_n(Nword):
        if exist_no_v(Vword):
            print ("都存在，good boy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("n存在")
            print NID,"   ",VID
            id0=n_exist_id(Nword)
            insertdata_v(VID,Vword)
            insertship(id0, VID)
            VID = VID + 1
    else:
        if exist_no_v(Vword):
            print("v存在")
            print NID, "   ", VID
            id0=v_exist_id(Vword)
            insertdata_n(NID,Nword)
            insertship(NID, id0)
            NID = NID + 1
        else:
            print("两个都不存在")
            print NID, "   ", VID
            insertdata_n(NID, Nword)
            insertdata_v(VID, Vword)
            insertship(NID,VID)
            NID = NID + 1
            VID = VID + 1



    cur.close()  # 关闭游标
    conn.commit()  # 提交事物，向数据库插入东西必须要这行代码，否则不会真正的进行插入
    conn.close()  # 关闭数据库连接

def readfile(fpath):
    f = open(fpath)
    line = f.readline()
    while line:
        print line
        result = sentenceAnalysis(line)
        for row in result[0].triples():
            #print (row)

            if judgeNN(row[0][1]) and judgeVB(row[2][1]):
                print "名词>> ",Realword(row[0][0]),"  动词>> ",Realword(row[2][0])
                NounW=Realword(row[0][0])
                VerbW=Realword(row[2][0])
                insertMysql(NounW,VerbW)
            elif judgeVB(row[0][1]) and judgeNN(row[2][1]):
                print "动词>> ",Realword(row[0][0]),"  名词>> ", Realword(row[2][0])
                NounW = Realword(row[2][0])
                VerbW = Realword(row[0][0])
                insertMysql(NounW, VerbW)
            else:
                continue

        line = f.readline()

if __name__ == "__main__":
    readfile("100sentence.txt")