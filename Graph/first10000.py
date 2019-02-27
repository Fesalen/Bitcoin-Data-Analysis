#coding=gbk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Fixing random state for reproducibility
np.random.seed(19680801)

filename = 'C:/Users/wfw/Desktop/first10000.csv'
with open(filename) as f: #������ļ�����������ļ�����洢��f��
    reader = csv.reader(f)  #����һ���Ķ���reader
    header_row = next(reader) #�����ļ��е���һ��
    dates, outputs = [], []      #�����洢���ڣ���ֵ���б�
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')  #����������ת��Ϊdatetime����
        # print(current_date)
        dates.append(current_date)

        output = float(row[1])
        outputs.append(output)
matplotlib.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.sans-serif']=['SimHei']
fig, ax = plt.subplots()
ax.plot(dates, outputs, 'o')
ax.set_xlabel("ʱ��")
ax.set_ylabel("���ױ��ر�����")
# ax.set_title('Using hyphen instead of Unicode minus')
plt.show()