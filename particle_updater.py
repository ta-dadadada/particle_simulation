# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import numpy.random as rnd

from particle import Particle


class ParticleUpdater:
    @staticmethod
    def update(particle):
        raise NotImplementedError()


class ParticleRandomizer(ParticleUpdater):
    @staticmethod
    def update(particle, range_max=1.0, range_min=0.0):
        size = particle.get_position().shape
        new_position = rnd.random(size) * (range_max - range_min) + range_min
        particle.put_positon(new_position)
