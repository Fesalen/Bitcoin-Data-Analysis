#python 画柱状图折线图
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

a=[32987817, 70930120, 90034148, 86136607, 67424130, 31355176, 8374451, 2149070, 209736, 21457, 94, 5]  #数据
b=[8.47, 18.21, 23.11, 22.11, 17.30, 8.05, 2.15, 0.55, 0.05, 0.0055, 0.000024, 0.0000013]
l=[i for i in range(12)]

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

fmt='%.2f%%'
yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=[u'0-0.00001',u'0.00001-0.0001',u'0.0001-0.001',u'0.001-0.01',u'0.01-0.1',u'0.1-1',u'1-10',u'10-100',u'100-1000',
    u'1000-10000',u'10000-100000',u'>100000']

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(l, b,'or-',label=u'百分比');
ax1.yaxis.set_major_formatter(yticks)
ax1.set_xticklabels(a, rotation=20) #横坐标刻度值旋转40度
for i,(_x,_y) in enumerate(zip(l,b)):
    plt.text(_x,_y,b[i],color='black',fontsize=10,)  #将数值显示在图形上
ax1.legend(loc=1)
ax1.set_ylim([0, 30]);
ax1.set_ylabel('百分比');
ax1.set_xlabel('比特币数量')
plt.legend(prop={'family':'SimHei','size':12}, loc='upper left')  #设置中文
ax2 = ax1.twinx() # this is the important function
plt.bar(l,a,alpha=0.3,color='blue',label=u'地址数量')
ax2.legend(loc=2)
ax2.set_ylim([0, 100000000])  #设置y轴取值范围
ax2.set_ylabel('地址数量')
plt.legend(prop={'family':'SimHei','size':12},loc="upper right")
plt.xticks(l,lx)
plt.show()
