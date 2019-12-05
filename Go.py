# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:22:29 2019

@author: Guest1
"""

import pygame

pygame.init()

class Board:
    def __init__(self):
        self.grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

class whitePiece:
    def __init__(self):
        self.image = pygame.image.load("white_piece.png")

displayDimensions = (1000,1000)
display = pygame.display.set_mode(displayDimensions)

clock = pygame.time.Clock()
background_image = pygame.image.load("go_board.png")



gameover = False

display.blit(background_image, [0, 0])
board = Board()
while not gameover:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    if(pygame.mouse.get_pressed()[0]):
        coord = pygame.mouse.get_pos()
        white = pygame.image.load("white_piece.png").convert_alpha()
        
        display.blit(white, (coord[0]-24,coord[1]-20))

    if(pygame.mouse.get_pressed()[2]):
        coord = pygame.mouse.get_pos()
        black = pygame.image.load("black_piece.png").convert_alpha()
        
        display.blit(black, (coord[0]-28, coord[1]-28))