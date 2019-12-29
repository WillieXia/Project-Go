import copy 
from position import *

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
    def hasAlly(self, col, row, color):
        foundAlly = False
        if row != 0:
            if self.grid[row-1][col].color == color:
                foundAlly = True
        if row != 18:
            if self.grid[row+1][col].color == color:
                foundAlly = True
        if col != 0:
            if self.grid[row][col+1].color == color:
                foundAlly = True
        if col != 18:
            if self.grid[row][col-1].color == color:
                foundAlly = True
        return foundAlly

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
        elif (col == 18) and (0 < row < 18):
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
                           self.grid[x[0]][x[1]].color = None
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
                           self.grid[x[0]][x[1]].color = None

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
                           self.grid[x[0]][x[1]].color = None
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
                           self.grid[x[0]][x[1]].color = None
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
        temp = copy.deepcopy(self.gridOne)
        self.gridOne = copy.deepcopy(self.gridTwo)
        self.gridTwo = copy.deepcopy(self.grid)
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
        if not change and not self.checkLiberties(column,row) and not self.hasAlly(column, row, place.color):
            place.occupied = False
            place.color = None
            return False
        #self.printGrid(self.grid)
        if self.turn > 2: #Dealing with KO rule
           rowInc = 0
           same = True
           for x in self.gridOne:
               colInc = 0
               for y in x:
                   if self.grid[rowInc][colInc].occupied == y.occupied:
                       #if(self.grid[rowInc][colInc].occupied and y.occupied):
                       #    print(self.grid[rowInc][colInc].color)
                       #    print(y.color)
                       if self.grid[rowInc][colInc].color != y.color:
                           same = False
                   else:
                       same = False
                   colInc += 1
               rowInc += 1
           if same:
               self.grid = copy.deepcopy(self.gridTwo)
               self.gridTwo = copy.deepcopy(self.gridOne)
               self.gridOne = copy.deepcopy(temp)
               return False
           else:
               self.turn += 1
               return True
        else: 
            self.turn += 1
            return True

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




