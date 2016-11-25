#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-11-25 10:05

import sys
import pygame
from pygame.locals import *
white = 255, 255, 255
blue = 0, 0, 255
pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode((600, 500))  # 获取对显示系统的访问，并且创建一个窗口

myfont = pygame.font.Font(None, 60)  # 创建一个字体对象，第一个参数是字体，第二个参数是字体大小
textImage = myfont.render("Hello Pygame", True, white)  # 把文字当做一个图像来绘制。

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)  # 清除屏幕
    screen.blit(textImage, (100, 100))  # 绘制
    pygame.display.update()  # 刷新显示
