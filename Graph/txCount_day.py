import csv
from matplotlib import pyplot as plt
from datetime import datetime
from mpl_toolkits.axes_grid1 import host_subplot

#读取CSV文件数据
filename = 'C:/Users/wfw/Desktop/txcount_sum_day.csv'
with open(filename) as f: #打开这个文件，并将结果文件对象存储在f中
    reader = csv.reader(f)  #创建一个阅读器reader
    header_row = next(reader) #返回文件中的下一行
    dates, addnums, prices = [], [], []      #声明存储日期，最值的列表
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')  #将日期数据转换为datetime对象
        # print(current_date)
        dates.append(current_date)

        addnum = int(row[1])
        addnums.append(addnum)

plt.rcParams['font.sans-serif']=['SimHei']

host = host_subplot(111)



host.set_xlabel("时间")
host.set_ylabel("交易数量")

p1, = host.plot(dates, addnums, label="每日交易数")

leg = plt.legend()

host.yaxis.get_label().set_color(color='black')
leg.texts[0].set_color(p1.get_color())



plt.show()


