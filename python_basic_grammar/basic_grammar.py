#coding=utf-8


# ************************************************************************************ 基础语法
#------------------------------   判断语句
# score = 9
# if score >= 90:
#     print "优秀"
# elif score >= 60:
#     print "良好"
# else:
#     print "差"

#------------------------------   循环
# for i in range(100):
#     print "Item",i
#     print "Item {0}".format(i)
#     print "Item {0} {1}".format(i,"nihao ")

#------------------------------   定义函数
# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
# print max(1,100)

# #------------------------------   面向对象
#
# class Hello:
#
#     def __init__(self,name):
#         self.name = name
#
#     def sayh(self):
#         print "hello {0}".format(self.name)
#
# #------------------------------   继承
# class Hello_a(Hello):
#
#     def __init__(self,name):
#         Hello.__init__(self,name)
#
#     def say_thing(self):
#         print "good luck ",self.name
#
#
# b = Hello_a("nihao")
# b.say_thing()

# #------------------------------   引入py文件
# import mylib
# h = mylib.Hello()
# h.say_thing("呦吼")

# #------------------------------   切片
# c1 = "nihaoxidian"
# print c1[0]
# print c1[:3]
# print c1[2:8]



# ************************************************************************************ 列表 元祖 集合 字典
'''
列表
list = []
'''
# student = ["小明","小红","小杜","小王"]
# print student[2]

'''
元祖
tuple = ()
*** 元祖只能读取，不能修改内容
'''
# student = ("小明","小红","小杜","小王")
# print student[2]

'''
集合
set(元素)
'''
# a = set("asdfghjklasghkfd")
# b = set("dfgert")
# #交集
# x = a & b
# print x
# #并集
# y = a | b
# print y
# #差集
# z = a - b
# print z
# #去重
# a = set(a)
# print a

'''
字典
zidian = {'name':'小杜','home':'西安','like':'girl'}

字典：表示一整个事情，分别包括各方面具体信息。
'''
# boy = {'name':'小杜','home':'西安','like':'girl'}
# print boy['name']
# #增加
# boy['sex'] = 'man'
# print boy['sex']

# ************************************************************************************ pickle（腌制）
# 需要将对象持久性存储，不丢失对象类型和数据
# 先将对象序列化，使用的时候在恢复数据
# 序列化的过程 称为pickle

# import pickle
# #dumps(object) 将对象序列化
# a = ["niaho ","shiyanshi","student"]
# b = pickle.dumps(a)
# #print b
#
# #loads(object) 将对象恢复
# c = pickle.loads(b)
# #print c
#
# #dump(object,file) 将对象序列化后存储到文件里
# a_new =("nihao","woaini","zhongguo")
# f1 = file('1.pk1','wb')
# pickle.dump(a_new,f1,True)
# f1.close()
#
# #load(file)  将数据恢复
# f2 = file('1.pk1','rb')
# d = pickle.load(f2)
# f2.close()
# print d





