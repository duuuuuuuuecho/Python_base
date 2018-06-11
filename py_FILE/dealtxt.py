#coding=utf-8

def insertfile(fpath, Wstr):              #将字符串按行写入文件中
    f = file(fpath, "a+")
    f.write(Wstr)
    f.close()

def wordNumb(str):                         #统计一行中的单词数 按照空格区分
    num = str.split(' ')
    return len(num)

def removeWord(str,word):
    strall = str.split(' ')
    for str1 in strall:
        if str1 == word :
            print '**************************'
        else :
            print str1


def extractSentence(file1,file2,max):       #将file1中句子单词数大于 max 的句子写入file2中
    f = open(file1)
    line = f.readline()
    id = 1
    while line:
        if wordNumb(line) > max:
            insertfile(file2, line),
            print id, ": ok"
        else:
            print id, ": error"
        line = f.readline()
        id = id + 1
    f.close()

#if __name__ == "__main__":
   #extractSentence('text.txt','demo.txt',5)
