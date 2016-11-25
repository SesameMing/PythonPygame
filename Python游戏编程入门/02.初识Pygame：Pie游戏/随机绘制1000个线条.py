#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-11-25 14:19
import sys
import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption(("随机绘制1000个线条"))

screen.fill((0, 0, 200))
i = 0
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    color = 100, 255, 200
    width = 1

    while i < 1000:
        print(i)
        x = random.randint(0, 600),  random.randint(0, 600)
        y = random.randint(0, 500),  random.randint(0, 500)
        pygame.draw.line(screen, color, x, y, width)

        pygame.display.update()
        i += 1
    pygame.display.update()