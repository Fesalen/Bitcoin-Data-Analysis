#coding=gbk
import csv
from matplotlib import pyplot as plt
from datetime import datetime
from mpl_toolkits.axes_grid1 import host_subplot

#��ȡCSV�ļ�����
filename = 'C:/Users/wfw/Desktop/product_price.csv'
with open(filename) as f: #������ļ�����������ļ�����洢��f��
    reader = csv.reader(f)  #����һ���Ķ���reader
    header_row = next(reader) #�����ļ��е���һ��
    dates, outputs, prices = [], [], []      #�����洢���ڣ���ֵ���б�
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')  #����������ת��Ϊdatetime����
        # print(current_date)
        dates.append(current_date)

        output = float(row[2])
        outputs.append(output)

        price = float(row[1])
        prices.append(price)

host = host_subplot(111)
plt.rcParams['font.sans-serif']=['SimHei']
par = host.twinx()

host.set_xlabel("ʱ��")
host.set_ylabel("��Ԫ")
par.set_ylabel("��Ԫ")

p1, = host.plot(dates, outputs, label="ÿ��ƽ�����ױ��رҼ۸�")
p2, = par.plot(dates, prices, label="���رҼ۸�")

leg = plt.legend()

host.yaxis.get_label().set_color(color='black')
leg.texts[0].set_color(p1.get_color())

par.yaxis.get_label().set_color(color='black')
leg.texts[1].set_color(p2.get_color())

plt.show()


