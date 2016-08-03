# coding:utf-8

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
# 导入一些常用函数和常量
from sys import exit
# 想SYS模块接一个exit函数用来退出程序

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
# 创建一个窗口
pygame.display.set_caption('Hello, World!')
# 设置窗口标题

background = pygame.image.load(background_image_filename).convert()
# convert函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件（事实上因为 它太常用了，如果你不写pygame也会帮你做）
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
# convert_alpha相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。
# 加载并转换图像

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    screen.blit(background, (0, 0))
    # blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用update更新一下，否则画面一片漆黑
    # 将背景图画上去

    x, y = pygame.mouse.get_pos()
    # 获取鼠标位置
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height() / 2
    # 计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    # 把光标画上去

    pygame.display.update()
    # 刷新一下图片