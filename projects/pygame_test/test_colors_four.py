# coding:utf-8
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
        for _ in xrange(100):# range([start,] stop[, step])，
            # 根据start与stop指定的范围以及step设定的步长，
            # 生成一个序列。用法与range完全相同，
            # 所不同的是生成的不是一个数组，而是一个生成器。
            # >> > range(5)
            # [0, 1, 2, 3, 4]
            # >> > range(1, 5)
            # [1, 2, 3, 4]
            # >> > range(0, 6, 2)
            # [0, 2, 4]
            # >> > xrange(5)
            # xrange(5)
            # >> > list(xrange(5))
            # [0, 1, 2, 3, 4]
            # >> > xrange(1, 5)
            # xrange(1, 5)
            # >> > list(xrange(1, 5))
            # [1, 2, 3, 4]
            # >> > xrange(0, 6, 2)
            # xrange(0, 6, 2)
            # >> > list(xrange(0, 6, 2))
            # [0, 2, 4]
            rand_pos = (randint(0, 639), randint(0, 479))
            screen.set_at(rand_pos, rand_col)

        pygame.display.update()