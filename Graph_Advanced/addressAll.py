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

plt.plot([396535, 396535], [0, 100000324], 'r--')
plt.scatter(396535, 100000324, color='b')
plt.annotate("(#396535,100000324)", xy=(396535, 100000324), xytext=(-100, 5), textcoords='offset points')

plt.plot([212665, 212665], [0, 5294904], 'r--')
plt.scatter(212665, 5294904, color='b')
plt.annotate("(#212665,5294904)", xy=(212665, 5294904), xytext=(-50, 10), textcoords='offset points')

plt.plot([505569, 505569], [0, 336316467], 'r--')
plt.scatter(505569, 336316467, color='b')
plt.annotate("(#505569,336316467)", xy=(505569, 336316467), xytext=(-95, 10), textcoords='offset points')

plt.show()


