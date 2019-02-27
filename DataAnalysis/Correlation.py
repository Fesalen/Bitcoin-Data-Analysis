
#-*- coding : utf-8 -*-
# coding: unicode_escape
import pandas as pd

df=pd.read_csv(r'C:\Users\wfw\Desktop\parms1.csv',encoding="gbk")
# print(df)
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())

import matplotlib.pyplot as plt
# df.hist(bins=50)
# plt.show()
plt.rcParams['font.sans-serif']=['SimHei']

#计算关联
corr_matrix = df.corr()
#价格为因变量
print(corr_matrix['价格'].sort_values(ascending=False)) #0.816310

#散点图
df.plot(kind="scatter", x="交易费",y="价格")
plt.show()
