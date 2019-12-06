# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:22:29 2019

@author: Guest1
"""

import pygame

pygame.init()

class Board: #The overall board. Each intersection is represented by a "Placement" class.
    def __init__(self, board):
        self.grid = board
    def placePiece(self, positionX, positionY, colorPiece):
        column = round((positionX - 231)/52)
        row = round((positionY - 31)/52)
        place = self.grid[row][column]
        place.occupied = True
        if(colorPiece): 
           place.Piece = whitePiece(place.X-22,place.Y-22)
           place.color = True
        else:
           place.Piece = blackPiece(place.X-28,place.Y-28)
           place.color = False
        return place.Piece
    #Helper Check Functions
    def checkRight(self, col, row, colorPiece):
        if self.grid[row][col+1].occupied:
            if colorPiece != self.grid[row][col+1].color:
                return True
        return False
    def checkLeft(self, col, row, colorPiece):
        if self.grid[row][col-1].occupied:
            if colorPiece != self.grid[row][col-1].color:
                return True
        return False
    def checkUp(self, col, row, colorPiece):
        if self.grid[row+1][col].occupied:
            if colorPiece != self.grid[row+1][col].color:
                return True
        return False
    def checkDown(self, col, row, colorPiece):
        if self.grid[row-1][col].occupied:
            if colorPiece != self.grid[row-1][col].color:
                return True
        return False
    def checkPlacable(self, positionX, positionY, colorPiece):
        col = round((positionX - 231)/52)
        row = round((positionY - 31)/52)
        placable = True
        if (0 < row < 18) and (0 < col < 18):
           if self.checkRight(col, row, colorPiece) and self.checkLeft(col, row, colorPiece) and \
                self.checkDown(col, row, colorPiece) and self.checkUp(col, row, colorPiece):
                   placable = False
        elif (row == 0) and (0 < col < 18):
           if self.checkRight(col, row, colorPiece) and self.checkLeft(col, row, colorPiece) and \
                self.checkDown(col, row, colorPiece):
                   placable = False
        elif (row == 18) and (0 < col < 18):
           if self.checkRight(col, row, colorPiece) and self.checkLeft(col, row, colorPiece) and \
                self.checkUp(col, row, colorPiece):
                   placable = False
        elif (col == 0) and (0 < row < 18):
           if self.checkRight(col, row, colorPiece) and self.checkDown(col, row, colorPiece) and \
               self.checkUp(col, row, colorPiece):
                   placable = False
        elif (col == 18) and (0 < col < 18):
           if self.checkDown(col, row, colorPiece) and self.checkLeft(col, row, colorPiece) and \
               self.checkUp(col, row, colorPiece):
                   placable = False
        elif (col == 0) and (row == 0):
           if self.checkRight(col, row, colorPiece) and self.checkDown(col, row, colorPiece):
                   placable = False
        elif (col == 18) and (row == 0):
           if self.checkLeft(col, row, colorPiece) and self.checkDown(col, row, colorPiece):
                   placable = False
        elif (col == 0) and (row == 18):
           if self.checkRight(col, row, colorPiece) and self.checkUp(col, row, colorPiece):
                   placable = False
        elif (col == 18) and (row == 18):
           if self.checkLeft(col, row, colorPiece) and self.checkUp(col, row, colorPiece):
                   placable = False
        if(not placable or self.grid[row][col].occupied):
            return False
        return True

class Placement:
    def __init__(self, positionX, positionY):
        self.X = positionX
        self.Y = positionY
        self.occupied = False
        self.Piece = None
        self.color = None

class Piece:
    def __init__(self, positionX, positionY):
        self.X = positionX
        self.Y = positionY


class whitePiece(Piece):
    def position(self):
        return (self.X,self.Y)
    def image(self):
        return pygame.image.load("white_piece.png").convert_alpha()


class blackPiece(Piece):
    def position(self):
        return (self.X,self.Y)
    def image(self):
        return pygame.image.load("black_piece.png").convert_alpha()
       

class whitePlayer:
    def __init__(self):
        self.score = 0

class blackPlayer:
    def __init__(self):
        self.score = 0

#Setting up the image of the board
displayDimensions = (1400,1000)
display = pygame.display.set_mode(displayDimensions)
background_image = pygame.image.load("go_board.png")
display.fill([255,255,255])
display.blit(background_image, [200, 0])

initBoard = []
count = 0

columnY = 31
for column in range(0,19):
    singleRow = []
    columnX = 231
    for row in range(0,19):
        place = Placement(columnX,columnY)
        singleRow.append(place)
        columnX += 52
    initBoard.append(singleRow)
    columnY += 52

board = Board(initBoard)   

gameover = False
whiteTurn = False #False is for black, true for white
while not gameover:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coord = pygame.mouse.get_pos()
            #Check if mouse is in board and place isn't occupied
            if ((abs(coord[0]-231))%52 <= 10  or (abs(coord[0]-231))%52 > 42) and ((abs(coord[1]-31)%52 <= 10)  \
                or (abs(coord[1]-31))%52 > 42) and coord[0] > 200 and coord[0] < 1180 and coord[1] > 29 and coord[1] < 970 \
                and board.checkPlacable(coord[0],coord[1],whiteTurn):
                    if whiteTurn:
                        piece = board.placePiece(coord[0],coord[1], True)
                        display.blit(piece.image(), piece.position())
                        whiteTurn = False

                    else:
                        piece = board.placePiece(coord[0],coord[1], False)     
                        display.blit(piece.image(), piece.position())
                        whiteTurn = True