# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:22:29 2019

@author: Guest1
"""

import pygame

pygame.init()

class Board(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


displayDimensions = (800,800)
display = pygame.display.set_mode(displayDimensions)

clock = pygame.time.Clock()
background_image = pygame.image.load("go_board.png").convert()

gameover = False

clock_tick_rate=20
while(gameover==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    display.blit(background_image, [0, 0])
    print("0")
    pygame.display.flip()
    clock.tick(clock_tick_rate)