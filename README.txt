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
-(COMPLETED) KO RULE: State of the board can not be what it was previously 
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
-Implement a try again feature when piece tries to make an invalid play instead of wasting turn

OTHER FEATURES
-Website Implementation
-Animations





