# coding:utf-8
background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

x = 0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))
    screen.blit(sprite, (x,100))

    x+=0.1

    if x>640.:
        x = 0.

    clock = pygame.time.Clock()
    time_passed = clock.tick()
    time_passed = clock.tick(30)
    #第二行的意识是返回一个上次调用的时间（以毫秒计）；第三行非常有用，在每一个循环中加上它

    pygame.display.update()