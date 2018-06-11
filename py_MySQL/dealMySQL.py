#coding=utf-8
import MySQLdb

conn = MySQLdb.connect(     #连接数据库
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='demo1',
)


cur = conn.cursor()     #通过获取到的数据库连接conn下的cursor()方法来创建游标。

# 创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据--------------------------------------------------------------------------------------------------------
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

#sqli="insert into student values(%s,%s,%s,%s)"
#cur.execute(sqli,('3','Huhu','2 year 1 class','7'))

#一次插入多条记录
#sqli="insert into student values(%s,%s,%s,%s)"
#cur.executemany(sqli,[
#    ('3','Tom','1 year 1 class','6'),
#    ('3','Jack','2 year 1 class','7'),
#    ('3','Yaheng','2 year 2 class','7'),
#    ])

#--------------------------------------------------------------------------------------------------------------------

#查询数据
#cur.execute("select * from student")
#cur.fetchone()

#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")





cur.close()             #关闭游标
conn.commit()           #提交事物，向数据库插入东西必须要这行代码，否则不会真正的进行插入
conn.close()            #关闭数据库连接




