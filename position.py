import pygame

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
        return pygame.image.load("images\white_piece.png").convert_alpha()


class blackPiece(Piece):
    def position(self):
        return (self.X,self.Y)
    def image(self):
        return pygame.image.load("images\\black_piece.png").convert_alpha()



