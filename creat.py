#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 创建一个表
def creat():
    # 打开数据库连接
    db = pymysql.connect(db='drone', host='rm-f8z114v7643f9t5c45o.mysql.rds.aliyuncs.com', user='root', passwd='601121423ZabY', port=3306)
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # 如果数据表已经存在使用 execute() 方法删除表。
    cursor.execute("DROP TABLE IF EXISTS TEST")
    # 创建数据表SQL语句
    sql = """CREATE TABLE TEST (
         id int(11) NOT NULL,
         longitude VARCHAR(20),
         latitude VARCHAR(20))"""
    cursor.execute(sql)
    # 关闭数据库连接
    db.close()


# 往列表中添加数据
def insert(val):
    db = pymysql.connect(db='drone', host='rm-f8z114v7643f9t5c45o.mysql.rds.aliyuncs.com', user='root', passwd='601121423ZabY', port=3306)
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    sql = "INSERT INTO TEST(id, \
           longitude, latitude) \
           VALUES (%s, %s, %s)"
    try:
        # 执行sql语句
        cursor.executemany(sql,val)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback() 
    # 关闭数据库连接
    db.close()


val = ((1, 120.1417465209961, 30.254547119140625), (2, 121.1417465209961, 31.254547119140625), (3, 124.1417465209961, 34.254547119140625))
creat()
insert(val)