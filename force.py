# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import numpy.random as rnd

from particle import Particle


class Force:
    @staticmethod
    def calc(particle):
        raise NotImplementedError()


def square_distance(pos1, pos2):
    return np.sum(np.power(pos1 - pos2, 2))


def generate_sq_dist_list(positions):
    item_num = len(positions)
    return [[square_distance(positions[i], positions[j]) for j in range(item_num)] for i in range(item_num)]


class SorfcoreForce(Force):
    disk_radi = 0.1

    @staticmethod
    def calc_one(position, tar):
        item_num = len(position)
        f = [position[tar] - position[i] if square_distance(position[tar], position[i]) < SorfcoreForce.disk_radi ** 2
             else [0, 0] for i in range(item_num)]
        return np.sum(f, axis=0)

    @staticmethod
    def calc(particle):
        position = particle.get_position()
        item_num = len(position)
        f = [SorfcoreForce.calc_one(position, i) for i in range(item_num)]
        return np.array(f)


if __name__ == '__main__':
    from particle_updater import *
    from particle_plotter import *
    p = Particle(4, 2)
    ParticleRandomInitializer.update(p)
    pos = p.get_position()
    print(pos)
    print(SorfcoreForce.calc(p))
