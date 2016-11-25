#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-11-25 14:10

import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("绘制一个椭圆")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    color = 255, 255, 0
    position = 100, 300, 100, 200
    width = 10
    pygame.draw.ellipse(screen, color, position, width)

    pygame.display.update()