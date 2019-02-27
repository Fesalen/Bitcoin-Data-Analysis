import csv
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot

#读取CSV文件数据
filename = 'C:/Users/wfw/Desktop/allsum.csv'
with open(filename) as f: #打开这个文件，并将结果文件对象存储在f中
    reader = csv.reader(f)  #创建一个阅读器reader
    header_row = next(reader) #返回文件中的下一行
    heights, allNums = [], []      #声明存储日期，最值的列表
    for row in reader:
        height = int(row[0])
        heights.append(height)

        addnum = float(row[1])
        allNums.append(addnum)

plt.rcParams['font.sans-serif']=['SimHei']

host = host_subplot(111)

host.set_xlabel("区块高度")
host.set_ylabel("地址数量")


p1, = host.plot(heights, allNums, label='地址总量')

leg = plt.legend()

host.yaxis.get_label().set_color(color='black')
leg.texts[0].set_color(p1.get_color())

plt.show()


