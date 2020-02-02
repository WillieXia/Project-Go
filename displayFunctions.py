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

def displayPass(display):
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Pass", True, [0,0,0])
    textRect = text.get_rect()  
    textRect.center = (40,80) 
    display.blit(text, textRect)

def passConfirmation(display):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Are you sure?", True, [0,0,0])
    textRect = text.get_rect()  
    textRect.center = (100,110) 
    display.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Yes        No", True, [0,0,0])
    textRect = text.get_rect()  
    textRect.center = (100,140) 
    display.blit(text, textRect)
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render("(Double Tap)", True, [0,0,0])
    textRect = text.get_rect()  
    textRect.center = (100,155) 
    display.blit(text, textRect)
