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
    """粒子の位置をランダムに変える."""
    @staticmethod
    def update(particle, range_max=1.0, range_min=0.0):
        size = particle.get_position().shape
        new_position = rnd.random(size) * (range_max - range_min) + range_min
        particle.put_positon(new_position)


class PeriodicBound(ParticleUpdater):
    @staticmethod
    def update(particle, box_length=1.0):
        old_position = particle.get_position()
        new_position = old_position - np.floor(old_position / box_length) * box_length
        particle.put_positon(new_position)


class ParticleFlower(ParticleUpdater):
    @staticmethod
    def update(particle, speed=[0.1, 0]):
        new_position = particle.get_position() + speed
        particle.put_positon(new_position)
        PeriodicBound.update(particle)


class ParticleRandomInitializer(ParticleUpdater):
    @staticmethod
    def update(particle, box_length=1.0, velocity_loc=0.0, velocity_scale=1.0):
        size = particle.get_position().shape
        new_position = rnd.random(size) * box_length
        particle.put_positon(new_position)
        new_velocity = rnd.normal(loc=velocity_loc, scale=velocity_scale, size=size)
        particle.put_velocity(new_velocity)


class ParticlePromoter(ParticleUpdater):
    dt = 0.1
    @staticmethod
    def update(particle):
        new_position = particle.get_position() + particle.get_velocity() * ParticlePromoter.dt
        particle.put_positon(new_position)
        PeriodicBound.update(particle)
