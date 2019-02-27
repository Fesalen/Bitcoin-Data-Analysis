# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

fig = plt.figure()
po_annotation = []
for i in range(0, 10):
    x = i
    y = x ** 2
    point, = plt.plot(x, y, 'o')
    annotation = plt.annotate(('x=' + str(x), 'y=' + str(y)), xy=(x + 0.1, y + 0.1), xycoords='data',
                              xytext=(x + 0.7, y + 0.7),
                              textcoords='data', horizontalalignment="left",
                              bbox=dict(boxstyle="round", facecolor="w", edgecolor="0.5", alpha=0.9)
                              )
    annotation.set_visible(False)
    po_annotation.append([point, annotation])


def on_move(event):
    visibility_changed = False
    for point, annotation in po_annotation:
        should_be_visible = (point.contains(event)[0] == True)
        # print(point.contains(event)[0])

        if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)

    if visibility_changed:
        plt.draw()


on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
