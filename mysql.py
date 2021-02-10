#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 定义两个列表存储经纬度
longitude = []
latitude = []

# 定义查询函数，查询经纬度
def query():
   # 打开数据库
   db = pymysql.connect(db='drone', host='rm-f8z114v7643f9t5c45o.mysql.rds.aliyuncs.com', user='root', passwd='601121423ZabY', port=3306)
   # 获取操作游标
   cursor = db.cursor()
   sql = "SELECT longitude, latitude FROM drone_coordinate_his_t"
   try:
      # 执行数据库操作
      cursor.execute(sql)
      # 获取列表
      results = cursor.fetchall()
      for result in results:
         longitude.append(result[0])
         latitude.append(result[1])
   except:
      print ("Error: unable to fetch data")
   # 关闭数据库连接
   db.close()

query()
print(longitude)
