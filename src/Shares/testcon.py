# -*- coding:utf-8 -*- 
"""
@Shares
@File    : testcon.py
@Time    : 2021/3/30 17:10
@Author  : gold312
@Software: PyCharm
@function： 测试连接读取等
"""
import datetime
import time

import akshare as ak
import pandas as pd
# import talib
# from talib import MA_Type
import pymysql
from sqlalchemy import create_engine

start1 = time.time()
database = pymysql.connect(host="localhost", user="root", password="1qaz@WSX", database="awesome", charset="utf8mb4")
# 格式：pymysql.connect("MySQL服务器地址", "用户名", "密码", "数据库名", charset='utf8')
cursor = database.cursor()
# sql = "SELECT company, date, sum(weight)FROM data where company = '李四粮食' group by date ;"
sql1 = "SELECT count(*) FROM sz000001;"
sql2 = "select * from sz000001 order by date desc limit 1;"
cursor.execute(sql2)
result = cursor.fetchall()
a = str((result[0][0] + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
spot = ak.stock_zh_a_daily('sz000001', start_date=a)
print(spot)
# print(result[0][0])
database.close()
end1 = time.time()
print(end1 - start1, '秒')

start2 = time.time()
database1 = create_engine('mysql+pymysql://root:1qaz@WSX@localhost:3306/awesome?charset=utf8mb4')

df = pd.read_sql('sz000001', database1)
# for i in df.iterrows():
#     print(i)
# print(df)
# 参数 M 表示月份，Q 表示季度，A 表示年度，D 表示按天
# temp = df.tail(1).iloc[0, 0].to_period('D') + 1
spot = ak.stock_zh_a_daily('sz000016')
print(len(spot) + 1)
spot['ID'] = range(1, len(spot) + 1)
spot = spot[['ID', 'open', 'high', 'low', 'close', 'volume', 'outstanding_share', 'turnover', 'date']]
print(spot)
# spot.to_sql('sz0000013', database1,  if_exists='replace', index=True)
pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20210301', periods=6))
# test = pd.read_sql('sz000001', database1)
# print(spot)
end2 = time.time()
print(end2 - start2, '秒')
#
#
#
# # tool_trade_date_hist_sina_df = ak.tool_trade_date_hist_sina()
# code_name = ak.stock_info_a_code_name()
# # data = tool_trade_date_hist_sina_df
#
#
# # spot = ak.stock_zh_a_daily('sh600000', start_date='2021-03-26')
# # print(spot)
# # print(data[7360:7400]['trade_date'])
# # print(code_name)
# # code_name.to_sql('test3', database, if_exists='append', index=True)
# # data.to_sql('data', database, index=True)
#
#
# def rq(cname):
#     # 查询股票最后一条数据
#     df = pd.read_sql(cname, database)
#     # print(df)
#     # 参数 M 表示月份，Q 表示季度，A 表示年度，D 表示按天
#     temp = df.tail(1).iloc[0, 0].to_period('D') + 1
#     return str(temp)
#
#
# # 股票历史行情采集
# def lscj():
#     cname = pd.read_sql('code_name', database, index_col='index')
#     for a in range(27):
#         lin = cname.iloc[a, 0]
#         print(lin)
#         date = rq(lin)
#         print(date)
#         try:
#             spot = ak.stock_zh_a_daily(lin, start_date=date)
#             spot.to_sql(lin, database, if_exists='append', index=True)
#         except:
#             print('新发行股票', cname.iloc[a, 0])
#
#
# def name():
#     zm = code_name.copy()
#     for a in range(len(zm)):
#         lin = zm.iloc[a, 0]
#         if lin[0] == '0' or lin[0] == '3':
#             m = 'sz' + zm.iloc[a, 0]
#             zm.iloc[a, 0] = m
#         else:
#             m = 'sh' + zm.iloc[a, 0]
#             zm.iloc[a, 0] = m
#     zm.to_sql('code_name', database, if_exists='append', index=True)
#
#
# # print(type(rq('sz000001')))
# # date = rq('sz000001')
# # print(date)
# #
# # srt = '2021-03-25'
# # print(type(srt))
# # lscj()
#
# # print(talib.get_functions())
#
#
# # # 股票历史行情采集 1、日期问题2、股票名称问题
# # def lscj():
# #     zm = code_name.copy()
# #     for a in range(len(zm)):
# #         lin = zm.iloc[a, 0]
# #         print(type(lin))
# #         try:
# #             if lin[0] == '0' or lin[0] == '3':
# #                 m = 'sz' + zm.iloc[a, 0]
# #                 zm.iloc[a, 0] = m
# #                 print(type(zm))
# #                 # spot = ak.stock_zh_a_daily(zm.iloc[a, 0])
# #                 # spot.to_sql(zm.iloc[a, 0], database, if_exists='append', index=True)
# #             else:
# #                 m = 'sh' + zm.iloc[a, 0]
# #                 zm.iloc[a, 0] = m
# #
# #                 # spot = ak.stock_zh_a_daily(zm.iloc[a, 0])
# #                 # spot.to_sql(zm.iloc[a, 0], database, if_exists='append', index=True)
# #         except:
# #             print(zm.iloc[a, 0])
# #             pass
