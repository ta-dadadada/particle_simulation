# -*- coding: UTF-8 -*-
from particle import *
from particle_updater import *
from particle_plotter import *


class System:
    def __init__(self, particle, p_updater):
        self.particle = particle
        self.p_updater = p_updater

    def run(self):
        p = self.particle
        ParticleRandomInitializer.update(p)
        p_plotter = ParticlePlotter(p, self.p_updater)
        p_plotter.run()


if __name__ == '__main__':
    s = System(Particle(64, 2), LangevinUpdater)
    s.run()
