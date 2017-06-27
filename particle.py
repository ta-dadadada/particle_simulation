# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import numpy.random as rnd


# 更新する内容


class Particle:
    def __init__(self, patrticle_num=1, dim_num=2):
        self.num = patrticle_num
        self.position = np.zeros([patrticle_num, dim_num])
        self.velocity = np.zeros([patrticle_num, dim_num])

    def get_position(self):
        return self.position

    def put_positon(self, new_position):
        if self.position.shape != new_position.shape:
            print("put position: 入力が不正のためスキップ", self.position.shape, new_position.shape)
            return
        self.position = new_position

    def get_velocity(self):
        return self.velocity

    def put_velocity(self, new_velocity):
        if self.velocity.shape != new_velocity.shape:
            print("put velocity: 入力が不正のためスキップ", self.velocity.shape, new_velocity.shape)
            return
        self.velocity = new_velocity


if __name__ == '__main__':
    print("hello!")
