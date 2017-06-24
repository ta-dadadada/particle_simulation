# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import numpy.random as rnd
# my modules
import particle as pc
from particle import Particle
import particle_updater as pup
from particle_updater import ParticleUpdater


class ParticlePlotter(Particle):
    """(x, y)をプロット."""

    def __init__(self, particle, particle_updater):

        self.particle = particle
        self.particle_updater = particle_updater
        fig = plt.figure()
        self.fig = fig

        # グラフを中央に表示
        ax = fig.add_subplot(1, 1, 1)

        # グラフの目盛範囲設定
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        self.ax = ax

    def _update_plot(self, i, fig, im):
        # 前回のフレーム内容を一旦削除
        if len(im) > 0:
            im[0].remove()
            im.pop()
        self.particle_updater.update(self.particle)
        x = self.particle.get_position()[:, 0]
        y = self.particle.get_position()[:, 1]
        im.append(plt.scatter(x, y))
        return self.particle.get_position()

    def run(self):
        im = []  # フレーム更新の際に前回のプロットを削除するために用意

        # アニメーション作成
        ani = animation.FuncAnimation(self.fig, self._update_plot, fargs=(self.fig, im),
                                      frames=10, interval=100)

        # 表示
        plt.show()


if __name__ == '__main__':
    p_plotter = ParticlePlotter(pc.Particle(25), pup.ParticleRandomizer)
    p_plotter.run()
