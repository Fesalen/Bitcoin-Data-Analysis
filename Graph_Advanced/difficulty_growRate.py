import csv
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot

#读取CSV文件数据
filename = 'C:/Users/wfw/Desktop/difficulty_rate.csv'
with open(filename) as f: #打开这个文件，并将结果文件对象存储在f中
    reader = csv.reader(f)  #创建一个阅读器reader
    header_row = next(reader) #返回文件中的下一行
    heights, allNums = [], []      #声明存储日期，最值的列表
    for row in reader:
        height = int(row[0])
        heights.append(height)

        addnum = float(row[1])
        allNums.append(addnum)

host = host_subplot(111)
plt.rcParams['font.sans-serif']=['SimHei']
host.set_xlabel("区块高度")
host.set_ylabel("难度值增长率(%)")


p1, = host.plot(heights, allNums, label='难度值增长率')

leg = plt.legend()

host.yaxis.get_label().set_color(color='black')
leg.texts[0].set_color(p1.get_color())

plt.scatter(68544, 3.02222222222222, color='b')
plt.annotate("(#361346, 3.02222%)", xy=(68544, 3.02222222222222), xytext=(20, -30), textcoords='offset points', size=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.scatter(435456, -0.0189731667975383, color='b')
plt.annotate("(#435456, -0.01897%)", xy=(435456, -0.0189731667975383), xytext=(-20, -20), textcoords='offset points', size=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()


