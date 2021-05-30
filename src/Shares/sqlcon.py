# -*- coding:utf-8 -*- 
"""
@Shares
@File    : SqlCon.py
@Time    : 2021/3/27 22:04
@Author  : gold312
@Software: PyCharm
@function：连接读取更新
"""
import datetime
import time

# import threading
import akshare as ak
import pandas as pd
import pymysql
import talib
from sqlalchemy import create_engine

# 声明数据库连接
# database = create_engine('mysql+pymysql://root:1qaz@WSX@localhost:3306/Shares?charset=utf8mb4')
# db = pymysql.connect(host="localhost", user="root", password="1qaz@WSX", database="awesome", charset="utf8mb4")
# cursor = db.cursor()

database = create_engine('mysql+pymysql://gold312:mltsh@192.168.32.8:3306/Shares?charset=utf8mb4')
db = pymysql.connect(host="192.168.32.8", user="gold312", password="mltsh", database="Shares", charset="utf8mb4")
cursor = db.cursor()


# 下载历史交易日期
def date():
    tool_trade_date_hist_sina_df = ak.tool_trade_date_hist_sina()
    sz = tool_trade_date_hist_sina_df
    sz.to_sql('data', database, if_exists='replace', index=True)


# 更新股票列表并存入数据库
def name():
    code_name = ak.stock_info_a_code_name()
    zm = code_name.copy()
    for a in range(len(zm)):
        lin = zm.iloc[a, 0]
        if lin[0] == '0' or lin[0] == '3':
            m = 'sz' + zm.iloc[a, 0]
            zm.iloc[a, 0] = m
        else:
            m = 'sh' + zm.iloc[a, 0]
            zm.iloc[a, 0] = m
    zm.to_sql('code_name', database, if_exists='replace', index=True)
    print("更新股票列表完成")


# 查找最后一条历史数据返回日期并增加一天
def rq(cname):
    # # 查询股票最后一条数据
    # df = pd.read_sql(cname, database)
    # # print(df)
    # # 参数 M 表示月份，Q 表示季度，A 表示年度，D 表示按天
    # temp = df.tail(1).iloc[0, 0].to_period('D') + 1
    sql = 'select * from ' + cname + ' order by date desc limit 1;'
    # print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    temp = (result[0][0] + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    # db.close()
    return str(temp)


# print(rq('sz000001'))
# 更新单条数据
def update(lin):
    tian = rq(lin)
    spot = ak.stock_zh_a_daily(lin, start_date=tian)
    spot.to_sql(lin, database, if_exists='append', index=True)
    print('更新', lin, '完成。', tian)


# 初始化单条数据
def initial(lin):
    spot = ak.stock_zh_a_daily(lin)
    spot.to_sql(lin, database, if_exists='replace', index=True)
    print('更新', lin, '完成。')


# 股票历史行情采集
def update_all_():
    start = time.time()
    name()
    cname = pd.read_sql('code_name', database, index_col='index')
    # print(cname)
    for a in range(len(cname)):
        code, soname = cname.iloc[a, 0], cname.iloc[a, 1]
        try:
            tian = rq(code)
            spot = ak.stock_zh_a_daily(code, start_date=tian)
            spot.to_sql(code, database, if_exists='append', index=True)
            print('更新', code, soname, '完成。', tian)
        except:
            try:
                spot = ak.stock_zh_a_daily(code)
                spot.to_sql(code, database, if_exists='replace', index=True)
                print('新发行股票', code, soname)
            except:
                print('今日新发股票，尚无历史数据', code, soname)
    end = time.time()
    print('更新全部完成', '耗时', int(end - start), '秒')


# 暂时无ID序列
def initial_all_():
    start = time.time()
    name()
    cname = pd.read_sql('code_name', database, index_col='index')
    # print(cname)
    for a in range(len(cname)):
        code, soname = cname.iloc[a, 0], cname.iloc[a, 1]
        try:
            spot = ak.stock_zh_a_daily(code)
            spot.to_sql(code, database, if_exists='replace', index=True)
            print('初始化', code, soname, '完成')
        except:
            print('今日新发股票，尚无历史数据', code, soname)
    end = time.time()
    print('初始化全部完成', '耗时', int(end - start), '秒')


# MACD筛选全部股票
def macd_all_():
    cname = pd.read_sql('code_name', database, index_col='index')
    # print(cname)
    for a in range(len(cname)):
        lin = cname.iloc[a, 0]
        df = pd.read_sql(lin, database)
        # open = df['open'].values
        # high = df['high'].values
        close = df['close'].values
        # low = df['low'].values
        # volume = df["volume"].values
        # integer = talib.CDL2CROWS(open, high, low, close)
        # # print(integer)
        # DIF组成的线叫做MACD线，DEA组成的线叫做Signal线，DIFF减DEA，得Hist
        macd, signal, hist = talib.MACD(close)
        ma_5 = talib.MA(close, 5)
        ma_10 = talib.MA(close, 10)
        # 金叉，且均线齐头排列，买入
        if macd[-2] < signal[-2] and macd[-1] > signal[-1] and ma_5[-1] > ma_10[-1]:
            print('选中', lin)
        # 死叉，或者，或者，或者均线空排下降，卖出
        elif macd[-1] > 0 and signal[-1] > 0 and macd[-2] > signal[-2] and macd[-1] < signal[-1] or ma_5[-1] < ma_10[
            -1]:
            print('淘汰', lin)


initial('sz300391')

# initial_all_()
# spot = ak.stock_zh_a_daily('sh689009')
# print(data[7360:7400]['trade_date'])
# print(code_name)
# spot.to_sql('sh689009', database, if_exists='append', index=True)
# print(spot)
