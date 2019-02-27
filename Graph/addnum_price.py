import csv
from matplotlib import pyplot as plt
from datetime import datetime
from mpl_toolkits.axes_grid1 import host_subplot

#读取CSV文件数据
filename = 'C:/Users/wfw/Desktop/addnum_price.csv'
with open(filename) as f: #打开这个文件，并将结果文件对象存储在f中
    reader = csv.reader(f)  #创建一个阅读器reader
    header_row = next(reader) #返回文件中的下一行
    dates, addnums, prices = [], [], []      #声明存储日期，最值的列表
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y/%m/%d')  #将日期数据转换为datetime对象
        # print(current_date)
        dates.append(current_date)

        addnum = float(row[1])
        addnums.append(addnum)

        if row[2] != '':
            price = float(row[2])
            prices.append(price)

host = host_subplot(111)
plt.rcParams['font.sans-serif']=['SimHei']

par = host.twinx()

host.set_xlabel("时间")
host.set_ylabel("每日比特币新增地址个数")
par.set_ylabel("比特币价格/单位：美元")

p1, = host.plot(dates, addnums, label="每日比特币新增地址个数")
p2, = par.plot(dates, prices, label="比特币价格")

leg = plt.legend()

host.yaxis.get_label().set_color(color='black')
leg.texts[0].set_color(p1.get_color())

par.yaxis.get_label().set_color(color='black')
leg.texts[1].set_color(p2.get_color())

plt.show()


