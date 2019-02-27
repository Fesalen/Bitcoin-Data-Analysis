import csv
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot

#读取CSV文件数据
filename = 'C:/Users/wfw/Desktop/difficulty.csv'
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
host.set_ylabel("难度值")


p1, = host.plot(heights, allNums, label='难度值')

leg = plt.legend()

host.yaxis.get_label().set_color(color='black')
leg.texts[0].set_color(p1.get_color())

# plt.plot([32255, 32255], [0, 1], 'r--')
plt.scatter(32255, 1, color='b')
plt.annotate("(#32255,1)", xy=(32255, 1), xytext=(-20, 5), textcoords='offset points')

# plt.plot([264994, 264994], [0, 267731249.5], 'r--')
plt.scatter(264994, 267731249.5, color='b')
plt.annotate("(#264994,267731249)", xy=(264994, 267731249.5), xytext=(-60, 10), textcoords='offset points')

# plt.plot([361346, 361346], [0, 49692386355], 'r--')
plt.scatter(361346, 49692386355, color='b')
plt.annotate("(#361346,49692386355)", xy=(361346, 49692386355), xytext=(-80, 30), textcoords='offset points',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# plt.plot([439641, 439641], [0, 281800917193.195], 'r--')
plt.scatter(439641, 281800917193.195, color='b')
plt.annotate("(#439641,281800917193)", xy=(439641, 281800917193.195), xytext=(-80, 50), textcoords='offset points',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()


