# coding:utf-8
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)# 创建窗口

def create_scales(height):
    red_scale_surface = pygame.surface.Surface((640, height))#  Surface((width, height), flags=0, depth=0, masks=None)
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface = pygame.surface.Surface((640, height))
    for x in range(640):
        c = int((x/640.)*255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)# 存储矩形, Rect(left, top, width, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)# 画出一个矩形，rect(Surface, color, Rect, width=0)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface

red_scale, green_scale, blue_scale = create_scales(80)

color = [127, 127, 127]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((0, 0, 0))

    screen.blit(red_scale, (0, 00))
    screen.blit(green_scale, (0, 00))
    screen.blit(blue_scale, (0, 00))

    x, y = pygame.mouse.get_pos()# 获得鼠标位置

    if pygame.mouse.get_pos():
        for component in range(3):
            if y > component*80 and y < (component+1)*80:
                color[component] = int((x/639.)*255.)
        pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))

    for component in range(3):
        pos = (int((color[component]/255.)*639), component*80+40)
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

    pygame.display.update()