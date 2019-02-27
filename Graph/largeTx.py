#python 画柱状图折线图
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

a=[44,1744,6971,256,106,301,42,426,110]  #数据
b=[0.44,17.44,69.71,2.56,1.06,3.01,0.42,4.26,1.10]
l=[i for i in range(9)]

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

fmt='%.2f%%'
yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=[u'2010',u'2011',u'2012',u'2013',u'2014',u'2015',u'2016',u'2017',u'2018']

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(l, b,'or-',label=u'百分比');
ax1.yaxis.set_major_formatter(yticks)
# ax1.set_xticklabels(a, rotation=20) #横坐标刻度值旋转40度
for i,(_x,_y) in enumerate(zip(l,b)):
    plt.text(_x,_y,b[i],color='black',fontsize=10,)  #将数值显示在图形上
ax1.legend(loc=1)
ax1.set_ylim([0, 80]);
ax1.set_ylabel('百分比');
ax1.set_xlabel('时间')
plt.legend(prop={'family':'SimHei','size':12}, loc='upper left')  #设置中文
ax2 = ax1.twinx() # this is the important function
plt.bar(l,a,alpha=0.3,color='blue',label=u'大额交易数量')
ax2.legend(loc=2)
ax2.set_ylim([0, 8000])  #设置y轴取值范围
ax2.set_ylabel('交易数量')
plt.legend(prop={'family':'SimHei','size':12},loc="upper right")
plt.xticks(l,lx)
plt.show()
