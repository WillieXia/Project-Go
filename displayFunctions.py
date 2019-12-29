import pygame

def displayTurn(display, turn):
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render('Turn: '+str(turn), True, [0,0,0])
    textRect = text.get_rect()  
    textRect.center = (1300,20) 
    display.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', 30)
    color = ""
    if turn%2 == 1:
        color += "White"
    else:
        color += "Black"
    text = font.render(color + '\'s Turn', True, [0,0,0])
    textRect = text.get_rect()  
    textRect.center = (1300,50) 
    display.blit(text, textRect)

def displayInstruction(display, text):
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(text, True, [0,0,0])
    textRect = text.get_rect()  
    textRect.center = (0,30) 
    display.blit(text, textRect)
