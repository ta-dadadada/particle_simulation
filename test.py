# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import numpy.random as rnd
# 更新する内容


def _update_plot(i, fig, im):
  rad = math.radians(i)

  # 前回のフレーム内容を一旦削除
  if len(im) > 0:
    im[0].remove()
    im.pop()

  x = np.array([rnd.randint(10) for i in range(10)])
  y = np.array([rnd.randint(10) for i in range(10)])

  im.append(plt.scatter(x, y))


fig = plt.figure()

# グラフを中央に表示
ax = fig.add_subplot(1, 1, 1)

# グラフの目盛範囲設定
ax.set_xlim([-1, 10])
ax.set_ylim([-1, 10])

im = []  # フレーム更新の際に前回のプロットを削除するために用意

# アニメーション作成
ani = animation.FuncAnimation(fig, _update_plot, fargs=(fig, im),
                              frames=1000, interval=100)

# 表示
plt.show()
