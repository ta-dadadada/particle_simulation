# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import numpy.random as rnd


# 更新する内容


class Particle:
    def __init__(self, patrticle_num=1, dim_num=3):
        self.num = patrticle_num
        self.position = np.zeros([patrticle_num, dim_num])
        self.velocity = np.zeros([patrticle_num, dim_num])

    def get_position(self):
        return self.position

    def put_positon(self, new_position):
        self.position = new_position

    def get_velocity(self):
        return self.velocity

    def put_velocity(self, new_velocity):
        self.velocity = new_velocity


if __name__ == '__main__':
    print("hello!")
