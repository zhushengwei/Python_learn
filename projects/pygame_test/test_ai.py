SCREEN_SIZE = (640, 480)
NEST_POSITION = (320, 240)
ANT_COUNT = 20
NEST_SIZE = 100.

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from random import randint, choice

def run():
    pygame.init()


    while True:


        pygame.display.update()