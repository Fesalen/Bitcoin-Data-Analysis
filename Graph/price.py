# coding=gbk
import csv
from matplotlib import pyplot as plt
from datetime import datetime
from mpl_toolkits.axes_grid1 import host_subplot

#��ȡCSV�ļ�����
filename = 'C:/Users/wfw/Desktop/price.csv'
with open(filename) as f: #������ļ�����������ļ�����洢��f��
    reader = csv.reader(f)  #����һ���Ķ���reader
    header_row = next(reader) #�����ļ��е���һ��
    dates, addnums, prices = [], [], []      #�����洢���ڣ���ֵ���б�
    for row in reader:
        current_date = datetime.strptime(row[1], '%Y/%m/%d')  #����������ת��Ϊdatetime����
        # print(current_date)
        dates.append(current_date)

        addnum = float(row[0])
        addnums.append(addnum)

plt.rcParams['font.sans-serif']=['SimHei']
host = host_subplot(111)



host.set_xlabel("ʱ��")
host.set_ylabel("�۸�")

p1, = host.plot(dates, addnums, label="�۸�")

leg = plt.legend()

host.yaxis.get_label().set_color(color='black')
leg.texts[0].set_color(p1.get_color())



plt.show()


