# -*- coding:utf-8 -*- 
"""
@Office
@File    : ch06.py
@Time    : 2020/2/14 13:43
@Author  : gold312
@Software: PyCharm
@function：对MySQL进行增删改查
"""
import pymysql

database = pymysql.connect(host="localhost", user="root", password="1qaz@WSX", database="test", charset="utf8mb4")
# database = pymysql.connect("localhost", "root", "1qaz@WSX", "test", charset='utf8')
# 格式：pymysql.connect("MySQL服务器地址", "用户名", "密码", "数据库名", charset='utf8')
cursor = database.cursor()
# 初始化指针


# # 增
#
# # 格式："INSERT INTO 表名 (字段1,字段2,字段3) VALUES (内容1,内容2,内容3);"
# sql = "INSERT INTO data (date,company,province,price,weight) VALUES ('2019-9-20','河北粮食','河北','2200','45.1');"
# cursor.execute(sql)
# database.commit()  # 对存储的数据修改后，需要commit
# database.close()
#
# # 改
# # 格式："UPDATE 表名 SET 字段1=内容1,字段2=内容2  WHERE 条件;"
#
# sql = "UPDATE data SET date='2018-09-21' WHERE DATE='2019-09-20';"
# cursor.execute(sql)
# database.commit()  # 对存储的数据修改后，需要commit
# database.close()

# 查
# 基础语法："SELECT 字段 FROM 表名 WHERE 条件"

sql = "SELECT company, date, sum(weight)FROM data where company = '李四粮食' group by date ;"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
database.close()

# # 删
# # 格式："DELETE FROM 表名 WHERE 条件;" 条件的写法 ：字段=内容
#
# sql = "DELETE FROM data WHERE date='2018-09-21';"
# cursor.execute(sql)
# database.commit()  # 对存储的数据修改后，需要commit
# database.close()
