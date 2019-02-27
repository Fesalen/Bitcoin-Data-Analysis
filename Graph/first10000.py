#coding=gbk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Fixing random state for reproducibility
np.random.seed(19680801)

filename = 'C:/Users/wfw/Desktop/first10000.csv'
with open(filename) as f: #打开这个文件，并将结果文件对象存储在f中
    reader = csv.reader(f)  #创建一个阅读器reader
    header_row = next(reader) #返回文件中的下一行
    dates, outputs = [], []      #声明存储日期，最值的列表
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')  #将日期数据转换为datetime对象
        # print(current_date)
        dates.append(current_date)

        output = float(row[1])
        outputs.append(output)
matplotlib.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.sans-serif']=['SimHei']
fig, ax = plt.subplots()
ax.plot(dates, outputs, 'o')
ax.set_xlabel("时间")
ax.set_ylabel("交易比特币数量")
# ax.set_title('Using hyphen instead of Unicode minus')
plt.show()