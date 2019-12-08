GO PROJECT

This is my personal approach on creating a GO (Wei Qi, 围棋) game.
I was interested in working on this personal project, as GO has been
a game that I've played as a kid with my family. And I was especially
inspired by the AlphaGO movie. GO is by far the most intricate, beautiful
board game in the world, and I thought it would be a great way to
dwelve into the world of GO by first hand coding it on my own. 

Although GO may seem as a super simple UI on the surface level, the 
complexity and uniqueness of the game that makes the backend program
of the game so much more difficult than other games, like Chess. Coding
GO is a way for me to learn and practice my algorithms, while also
learning to use a library in python, pygame.


"""
This is for myself to keep track of programming my program
"""
STRUCTURE
-Build board UI (Board background image to Ju Rao)
-Divide dimensions of board into a placement class
-Program mouse cursor to react to each placement on the board

ALGORITHM
-KO RULE: State of the board can not be what it was previously 
(Easy: Just compare intended move state with previous state of board)
-(COMPLETED) Capture: Use a Dijkstra's pathfinder algorithm at a starting point, and recursively
check if the opposite color is captured
-(COMPLETED) Placement in Captured Area: This will be a little difficult, since I originally
intended to check piece placements based on liberties. However, you can still
place pieces in captured area if it will capitalize with other pieces.
(Strategy still in progress)
-Forbidden Points: Players can't play on a forbidden point, a point that won't
allows 0 liberties or capture potential
(Strategy still in progress)
-Area calculation: This will also be difficult, as we have to determine the color
that a respective empty area is granted to. We also have to check if an area is
even captured.
(Strategy still in progress)

OTHER FEATURES
-Website Implementation
-Animations





def checkRight(self, col, row, colorPiece):
        if self.grid[row][col+1].occupied:
            if colorPiece != self.grid[row][col+1].color:
                return True
        return False #Return true if enemy, false if ally
    def checkLeft(self, col, row, colorPiece):
        if self.grid[row][col-1].occupied:
            if colorPiece != self.grid[row][col-1].color:
                return True
        return False
    def checkUp(self, col, row, colorPiece):
        if self.grid[row-1][col].occupied:
            if colorPiece != self.grid[row+1][col].color:
                return True
        return False
    def checkDown(self, col, row, colorPiece):
        if self.grid[row+1][col].occupied:
            if colorPiece != self.grid[row-1][col].color:
                return True
        return False
    def checkOccupied(self, positionX, positionY):
        col = round((positionX - 231)/52)
        row = round((positionY - 31)/52)
        return self.grid[row][col].occupied
    def checkLiberties(self, col, row, colorPiece):
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
        return placable #Return true if at least one allies, false if all enemy / boundary