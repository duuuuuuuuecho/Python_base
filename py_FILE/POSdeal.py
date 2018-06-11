#coding=utf-8
#对句子进行词性分析

import nltk
from nltk.tokenize import word_tokenize                        #分词
from nltk.stem import SnowballStemmer                          #词原
from nltk.corpus import stopwords                              #停用词
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

'''
paragraph = "The first time I heard that song was in Hawaii on radio. I was just a kid, and loved it very much! What a fantastic song!"
sentences = sent_tokenizer.tokenize(paragraph)                  #分句
print sentences[0]
#for sen in sentences:
#   print sen

english_stopwords=stopwords.words('english')                  #去停用词
print english_stopwords
d_list = word_tokenize(sentences[0])
fword=[word for word in d_list if(word not in english_stopwords)]
print fword

tag = nltk.pos_tag(word_tokenize(paragraph))
st = LancasterStemmer()                      #获得词原型

for tag1 in tag :
    if tag1[1] == 'NN'or tag1[1]== 'NNS':
        print st.stem(tag1[0])
'''

#分句
def separateSent(sentence1):
    sent = sent_tokenizer.tokenize(sentence1)
    #返回一个list
    return sent


#分词  去掉一些无意义的符号
def separateWord(sentence1):
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    w_list=word_tokenize(sentence1)
    use_word=[word for word in w_list if not word in english_punctuations]
    return use_word


#去停用词表 ***************去了停用词后会打乱句子语序，干扰后期词性分析  error error error
def E_stopwords(sentence2):
    english_stopwords = stopwords.words('english')
    s_list=word_tokenize(sentence2)
    use_word=[word for word in s_list if(word not in english_stopwords)]
    return use_word        #list

#词性分析，选取NN+与VB+的词
#l_word是已经分词的list
def select_pos(l_word):
    tag = nltk.pos_tag(l_word)
    #获取词原型
    snowball_stemmer = SnowballStemmer("english")

    for tag1 in tag:
       # print tag1
        if (tag1[1]=='NN'or tag1[1]=='NNS'or tag1[1]=='NNP'or tag1[1]=='NNPS')and (tag1[0] != '['or tag1[0] != ']'):
            print snowball_stemmer.stem(tag1[0]),"  名词"
        elif tag1[1]=='VB'or tag1[1]=='VBD'or tag1[1]=='VBG'or tag1[1]=='VBN'or tag1[1]=='VBP'or tag1[1]=='VBZ':
            print snowball_stemmer.stem(tag1[0]),"  动词"

if __name__ == '__main__':
    paragraph = "[[File:Hw-augustus.jpg|thumb|120px|right|Roman Emperor [[Augustus Caesar]], after whom August is named]]" \
                "This month was first called ''[[Sextilis]]'' in [[Latin]], because it was the sixth month in the old [[Roman calendar]]. " \
                "The Roman calendar began in March about 735 BC with [[Romulus and Remus|Romulus]]. [[October]] was the eighth month. " \
                " August was the eighth month when January or February were added to the start of the year by King [[Numa Pompilius]] about 700 BC. Or," \
                " when those two months were moved from the end to the beginning of the year by the [[decemvirs]] about 450 BC (Roman writers disagree)." \
                " In [[153 BC]] [[January 1]] was determined as the beginning of the year." \
                " August is named for [[Augustus Caesar]] who became [[Roman consul]] in this month."
    A=separateSent(paragraph)
    for a in A:
       # B=E_stopwords(a)      error
        print a
        B=separateWord(a)
        select_pos(B)
