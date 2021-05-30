# -*- coding:utf-8 -*- 
"""
@Shares
@File    : ts01.py
@Time    : 2021/3/30 16:17
@Author  : gold312
@Software: PyCharm
@function：
"""
import pandas as pd
import talib
from sqlalchemy import create_engine

# import numpy as np

# talib.OBV?
# print(talib.get_functions())
# print(talib.get_function_groups())
# https://github.com/HuaRongSAO/talib-document
# 获取数据


database = create_engine('mysql+pymysql://root:1qaz@WSX@localhost:3306/Shares?charset=utf8mb4')


# df = pd.read_sql('sz000027', database)
#
# open_p = df['open'].values
# high_p = df['high'].values
# close_p = df['close'].values
# low_p = df['low'].values
# volume = df["volume"].values
# # print(open_p)
# open_p = open_p
# high = high_p
# close = close_p
# low = low_p
# print(close)
# print(np.array(close))

# macd, signal, hist = talib.MACD(close)

# df['EMA12'] = talib.EMA(close, timeperiod=6)
# df['EMA26'] = talib.EMA(np.array(close), timeperiod=12)
# ma_5 = talib.MA(close, 5)
# ma_20 = talib.MA(close, 20)
# print(df['EMA12'])
# print(df['EMA26'])
# print(macd)
# if macd[-1] < 0 and signal[-1] < 0 and macd[-2] < signal[-2] and macd[-1] > signal[-1] and ma_5[-1] > ma_20[-1]:
#     print('324234234')
# elif macd[-1] > 0 and signal[-1] > 0 and macd[-2] > signal[-2] and macd[-1] < signal[-1] or ma_5[-1] < ma_20[
#         -1]:
#     print('dsfsdfsdfsd')


def macd_all_():
    cname = pd.read_sql('code_name', database, index_col='index')
    # print(cname)
    for a in range(len(cname)):
        lin = cname.iloc[a, 0]
        df = pd.read_sql(lin, database)
        open = df['open'].values
        high = df['high'].values
        close = df['close'].values
        low = df['low'].values
        # volume = df["volume"].values
        integer = talib.CDL2CROWS(open, high, low, close)
        print(integer)
        # DIF组成的线叫做MACD线，DEA组成的线叫做Signal线，DIFF减DEA，得Hist
        # macd, signal, hist = talib.MACD(close)
        # ma_5 = talib.MA(close, 5)
        # ma_10 = talib.MA(close, 10)
        # # 金叉，且均线齐头排列，买入
        # if macd[-2] < signal[-2] and macd[-1] > signal[-1] and ma_5[-1] > ma_10[-1]:
        #     print('选中', lin)
        # # 死叉，或者，或者，或者均线空排下降，卖出
        # elif macd[-1] > 0 and signal[-1] > 0 and macd[-2] > signal[-2] and macd[-1] < signal[-1] or ma_5[-1] < ma_10[
        #     -1]:
        #     print('淘汰', lin)


macd_all_()
