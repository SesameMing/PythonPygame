#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-11-25 10:31
import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Drawing Circles")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    # draw a circle
    color = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10
    pygame.draw.circle(screen, color, position, radius, width)

    pygame.display.update()