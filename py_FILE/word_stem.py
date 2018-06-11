#coding=utf-8
#得到词原的几种不同方法  比较

from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer

string = "called"

porter_stemmer = PorterStemmer()
a = porter_stemmer.stem(string)
print a

wordnet_lemmatizer = WordNetLemmatizer()
b = wordnet_lemmatizer.lemmatize(string)
print b

snowball_stemmer = SnowballStemmer("english")
c=snowball_stemmer.stem(string)
print c

st = LancasterStemmer()
d = st.stem(string)
print d