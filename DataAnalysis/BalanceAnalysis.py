
#coding=gbk
# coding: unicode_escape
import pandas as pd

df=pd.read_csv(r'C:\Users\wfw\Desktop\address\parms Test10.csv',encoding="gbk")
# print(df)
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())

import matplotlib.pyplot as plt
# df.hist(bins=50)
# plt.show()
plt.rcParams['font.sans-serif']=['SimHei']

#�������
corr_matrix = df.corr()
#�۸�Ϊ�����
print(corr_matrix['�۸�'].sort_values(ascending=False)) #0.816310

# #ɢ��ͼ
# df.plot(kind="scatter", x="���׷�",y="�۸�")
# plt.show()
