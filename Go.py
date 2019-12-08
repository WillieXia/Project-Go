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
        self.gridOne = board
        self.gridTwo = board
        self.turn = 0
    def refreshScreen(self, display, background_image):
        display.blit(background_image, [200, 0])
        for x in self.grid:
            for y in x:
                if(y.occupied == True):
                    display.blit(y.Piece.image(), y.Piece.position())
    #Helper Check Functions
    def checkRight(self, col, row):
        if self.grid[row][col+1].occupied:
            return True
        return False #Return True if space is occupied, False if not Occupied
    def checkLeft(self, col, row):
        if self.grid[row][col-1].occupied:
            return True
        return False
    def checkUp(self, col, row):
        if self.grid[row-1][col].occupied:
            return True
        return False
    def checkDown(self, col, row):
        if self.grid[row+1][col].occupied:
            return True
        return False
    def checkLiberties(self, col, row):
        placable = True
        if (0 < row < 18) and (0 < col < 18):
           if self.checkRight(col, row) and self.checkLeft(col, row) and \
                self.checkDown(col, row) and self.checkUp(col, row):
                   placable = False
        elif (row == 0) and (0 < col < 18): #Corner cases
           if self.checkRight(col, row) and self.checkLeft(col, row) and \
                self.checkDown(col, row):
                   placable = False
        elif (row == 18) and (0 < col < 18):
           if self.checkRight(col, row) and self.checkLeft(col, row) and \
                self.checkUp(col, row):
                   placable = False
        elif (col == 0) and (0 < row < 18):
           if self.checkRight(col, row) and self.checkDown(col, row) and \
               self.checkUp(col, row):
                   placable = False
        elif (col == 18) and (0 < col < 18):
           if self.checkDown(col, row) and self.checkLeft(col, row) and \
               self.checkUp(col, row):
                   placable = False
        elif (col == 0) and (row == 0):
           if self.checkRight(col, row) and self.checkDown(col, row):
                   placable = False
        elif (col == 18) and (row == 0):
           if self.checkLeft(col, row) and self.checkDown(col, row):
                   placable = False
        elif (col == 0) and (row == 18):
           if self.checkRight(col, row) and self.checkUp(col, row):
                   placable = False
        elif (col == 18) and (row == 18):
           if self.checkLeft(col, row) and self.checkUp(col, row):
                   placable = False
        return placable #Return true if at least one liberty, false if no liberty
    def checkOccupied(self, positionX, positionY):
        col = round((positionX - 231)/52)
        row = round((positionY - 31)/52)
        return self.grid[row][col].occupied
    def findAllyPath(self, place, usedPoints):
        usedPoints.add((place.row, place.col))
        rightCheck = True
        leftCheck = True
        upCheck = True
        downCheck = True
        if(not self.checkLiberties(place.col, place.row)):
            if(place.col != 18):
                nextPiece = self.grid[place.row][place.col+1]
                if nextPiece.color == place.color and (nextPiece.row,nextPiece.col) not in usedPoints:
                    rightCheck =  self.findAllyPath(nextPiece, usedPoints)
                else: rightCheck = False
            else: rightCheck = False
            if(place.col != 0):
                nextPiece = self.grid[place.row][place.col-1]
                if nextPiece.color == place.color and (nextPiece.row,nextPiece.col) not in usedPoints:
                    leftCheck =  self.findAllyPath(nextPiece, usedPoints)
                else: leftCheck = False
            else: leftCheck = False
            if(place.row != 0):
                nextPiece = self.grid[place.row-1][place.col]
                if nextPiece.color == place.color and (nextPiece.row,nextPiece.col) not in usedPoints:
                    upCheck = self.findAllyPath(nextPiece, usedPoints)
                else: upCheck = False
            else: upCheck = False
            if(place.row != 18):
                nextPiece = self.grid[place.row+1][place.col]
                if nextPiece.color == place.color and (nextPiece.row,nextPiece.col) not in usedPoints:
                    downCheck = self.findAllyPath(nextPiece, usedPoints) 
                else: downCheck = False
            else: downCheck = False
        else:
            return True
        if(rightCheck or leftCheck or upCheck or downCheck):
            return True
        else: return False
    def checkCapture(self, col, row, colorPiece):
        captureOccured = False
        if col != 18:
           if self.checkRight(col, row) and self.grid[row][col+1].color != colorPiece:
               safe = self.checkLiberties(col+1, row) #Check for open space
               if(not safe):
                   usedPoints = set()
                   avoidElim = self.findAllyPath(self.grid[row][col+1], usedPoints)
                   if(not avoidElim):
                       captureOccured = True
                       for x in usedPoints:
                           self.grid[x[0]][x[1]].occupied = False
        if col != 0:
            if self.checkLeft(col, row) and self.grid[row][col-1].color != colorPiece:
               safe = self.checkLiberties(col-1, row) #Check for open space
               if(not safe):
                   usedPoints = set()
                   avoidElim = self.findAllyPath(self.grid[row][col-1], usedPoints)
                   if(not avoidElim):
                       captureOccured = True
                       for x in usedPoints:
                           self.grid[x[0]][x[1]].occupied = False

        if row != 0:
            if self.checkUp(col, row) and self.grid[row-1][col].color != colorPiece:
               safe = self.checkLiberties(col, row-1) #Check for open space
               if(not safe):
                   usedPoints = set()
                   avoidElim = self.findAllyPath(self.grid[row-1][col], usedPoints)
                   if(not avoidElim):
                       captureOccured = True
                       for x in usedPoints:
                           self.grid[x[0]][x[1]].occupied = False
        if row != 18:
            if self.checkDown(col, row) and self.grid[row+1][col].color != colorPiece:
               safe = self.checkLiberties(col, row+1) #Check for open space
               if(not safe):
                   usedPoints = set()
                   avoidElim = self.findAllyPath(self.grid[row+1][col], usedPoints)
                   if(not avoidElim):
                       captureOccured = True
                       for x in usedPoints:
                           self.grid[x[0]][x[1]].occupied = False
        if captureOccured:
            return True
        else:
            return False
    def checkAlly(self, row, col, color):
        if row != 18:
            if self.grid[row+1][col].color == color:
                return True
        if row != 0:
            if self.grid[row-1][col].color == color:
                return True
        if col != 0:
            if self.grid[row][col-1].color == color:
                return True
        if col != 18:
            if self.grid[row][col+1].color == color:
                return True
        return False

    def placePiece(self, positionX, positionY, colorPiece):
        #self.printGrid(self.gridOne)
        #self.gridOne = self.gridTwo.copy()
        #self.printGrid(self.gridOne)
        #self.gridTwo = self.grid.copy()
        
        self.printGrid(self.gridTwo)
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
        change = self.checkCapture(column, row, colorPiece)
        if not change and not self.checkLiberties(column,row) \
            and not self.checkAlly(row, column, place.color):
            place.occupied = False
        self.printGrid(self.grid)
        #if self.turn > 2: #Dealing with KO rule
        #    if self.grid == self.gridOne:
        #        self.grid = self.gridTwo
        self.turn += 1
           
    def printGrid(self, grid):
        for x in grid:
            row = ""
            for y in x:
                if(y.occupied):
                    if(y.color):
                        row += "W "
                    else:
                        row += "B "
                else:
                    row += "_ "
            print(row)


class Placement:
    def __init__(self, positionX, positionY):
        self.X = positionX
        self.Y = positionY
        self.occupied = False
        self.Piece = None
        self.color = None
        self.col = round((positionX - 231)/52)
        self.row = round((positionY - 31)/52)

class Piece:
    def __init__(self, positionX, positionY):
        self.X = positionX
        self.Y = positionY
        #self.libertyUp = True
        #self.libertyDown = True
        #self.libertyLeft = True
        #self.libertyRight = True


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
                and not board.checkOccupied(coord[0],coord[1]):
                    if whiteTurn:
                        board.placePiece(coord[0],coord[1], True)
                        whiteTurn = False
                    else:
                        board.placePiece(coord[0],coord[1], False)     
                        whiteTurn = True
            board.refreshScreen(display, background_image)