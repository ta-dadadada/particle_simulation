# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 更新する内容
def _update_plot(i, fig, im):
    rad = math.radians(i)

    # 前回のフレーム内容を一旦削除
    if len(im) > 0:
        im[0].remove()
        im.pop()

    im.append(plt.scatter(math.cos(rad), math.sin(rad)))

fig =  plt.figure()

# グラフを中央に表示
ax = fig.add_subplot(1,1,1)

# グラフの目盛範囲設定
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])

im = [] # フレーム更新の際に前回のプロットを削除するために用意

# アニメーション作成
ani = animation.FuncAnimation(fig, _update_plot, fargs = (fig, im),
        frames = 360, interval = 1)

# 表示
plt.show()
