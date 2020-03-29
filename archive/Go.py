"""
Created on Wed Nov  28 23:22:29 2019

@author: Willie Xia
"""

import pygame
from displayFunctions import *
from board import *

pygame.init()     

class whitePlayer:
    def __init__(self):
        self.score = 0


class blackPlayer:
    def __init__(self):
        self.score = 0

#Setting up the image of the board
displayDimensions = (1400,1000)
display = pygame.display.set_mode(displayDimensions)
background_image = pygame.image.load("images\go_board.png")
display.fill([255,255,255])
display.blit(background_image, [200, 0])

#Initializing and creating an empty board
initBoard = []
count = 0

columnY = 31
for column in range(0,19): #Setting up the board by pixel seperation
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
displayTurn(display, board.turn)
notAnswered = False
while not gameover:
    display.blit(pygame.transform.scale(pygame.image.load("images\help_button.jpg"),[50,50]),[0,0])
    display.blit(pygame.transform.scale(pygame.image.load("images\end_button.jpg").convert_alpha(),[50,50]),[60,0])
    displayPass(display)
    if notAnswered:
        passConfirmation(display)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coord = pygame.mouse.get_pos()
            if notAnswered:
                if(30<coord[0]<80 and 100<coord[1]<150):
                    notAnswered = False
                    board.turn += 1
                    whiteTurn = not whiteTurn
                    continue
                elif(130<coord[0]<170 and 100<coord[1]<150):
                    notAnswered = False
                    continue
                else:
                    continue
            if(0<coord[0]<50 and 0<coord[1]<50):
                printInstructions = True
                while printInstructions:
                    displayInstruction(display, "This is how to play")
                    printInstructions = False
                continue
            if(60<coord[0]<110 and 0<coord[1]<50):
                gameover = True
            if(10<coord[0]<70 and 50<coord[1]<110):
                notAnswered = True         
                continue
            #Check if mouse is in board and place isn't occupied
            if ((abs(coord[0]-231))%52 <= 12  or (abs(coord[0]-231))%52 > 40) and ((abs(coord[1]-31)%52 <= 12)  \
                or (abs(coord[1]-31))%52 > 40) and coord[0] > 200 and coord[0] < 1180 and coord[1] > 29 and coord[1] < 970 \
                and not board.checkOccupied(coord[0],coord[1]):
                    checkTurn = board.turn + 2
                    if whiteTurn and checkTurn%2 == 1:
                        check = board.placePiece(coord[0],coord[1], True)
                        if check:
                            whiteTurn = False
                    elif not whiteTurn and checkTurn%2 == 0:
                        check = board.placePiece(coord[0],coord[1], False) 
                        if check:
                            whiteTurn = True
            display.fill([255,255,255])
            board.refreshScreen(display, background_image)
            displayTurn(display, board.turn)
pygame.quit()
