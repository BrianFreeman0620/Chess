import graphics

class Piece:
    def __init__(self, startingPos):
        self.color = None
        self.topRight = graphics.Point(startingPos.getX() + .5, startingPos.getY() + .5)
        self.bottomLeft = graphics.Point(startingPos.getX() - .5, startingPos.getY() - .5)
        self.images = [graphics.Rectangle(self.topRight, self.bottomLeft), graphics.Rectangle(self.topRight, self.bottomLeft), graphics.Rectangle(self.topRight, self.bottomLeft)]
        self.images[0].setFill("white")
        self.images[1].setFill("black")
        self.images[2].setFill(graphics.color_rgb(0, 255, 0))
        self.position = startingPos
        self.type = None
        self.moved = False
        self.moves = {}
        
    def setColor(self, color):
        self.color = color
        
    def changePosition(self, newPosition):
        self.position = newPosition
        
    def possibleMoves(self):
        pass

class Bishop(Piece):
    def __init__(self,startingPos):
        self.color = None
        self.position = startingPos
        self.type = "bishop"
        self.moved = False
        self.moves = {}
    
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Bishop.png"), graphics.Image(self.position, "Chess_Images/WB_Bishop.png"), graphics.Image(self.position, "Chess_Images/WG_Bishop.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Bishop.png"), graphics.Image(self.position, "Chess_Images/BB_Bishop.png"), graphics.Image(self.position, "Chess_Images/BG_Bishop.png")] 

    def possibleMoves(self):
        self.moves = {}
        moveCount = 0
        for possibleDistance in range(1, 8):
            posX = self.position.getX() + possibleDistance
            negX = self.position.getX() - possibleDistance
            posY = self.position.getY() + possibleDistance
            negY = self.position.getY() - possibleDistance
            if posX < 8:
                if posY < 8:
                    self.moves[moveCount] = [graphics.Point(posX, posY), "upright", possibleDistance]
                    moveCount += 1
                if negY > -1:
                    self.moves[moveCount] = [graphics.Point(posX, negY), "downright", possibleDistance]
                    moveCount += 1
            if negX > -1:
                if posY < 8:
                    self.moves[moveCount] = [graphics.Point(negX, posY), "upleft", possibleDistance]
                    moveCount += 1
                if negY > -1:
                    self.moves[moveCount] = [graphics.Point(negX, negY), "downleft", possibleDistance]
                    moveCount += 1

class King(Piece):
    def __init__(self,startingPos):
        self.color = None
        self.position = startingPos
        self.type = "king"
        self.moved = False
        self.moves = {}
    
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_King.png"), graphics.Image(self.position, "Chess_Images/WB_King.png"), graphics.Image(self.position, "Chess_Images/WG_King.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_King.png"), graphics.Image(self.position, "Chess_Images/BB_King.png"), graphics.Image(self.position, "Chess_Images/BG_King.png")] 
    
    def possibleMoves(self):
        self.moves = {}
        moveCount = 0
        for xValues in range(-1, 2):
            for yValues in range(-1, 2):
                if xValues != 0 or yValues != 0:
                    newX = self.position.getX() + xValues
                    newY = self.position.getY() + yValues
                    if newX > -1 and newX < 8 and newY > -1 and newY < 8:
                        self.moves[moveCount] = [graphics.Point(newX, newY), "move", 1]
                        moveCount += 1
    
class Knight(Piece):
    def __init__(self,startingPos):
        self.color = None
        self.position = startingPos
        self.type = "knight"
        self.moved = False
        self.moves = {}
    
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Knight.png"), graphics.Image(self.position, "Chess_Images/WB_Knight.png"), graphics.Image(self.position, "Chess_Images/WG_Knight.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Knight.png"), graphics.Image(self.position, "Chess_Images/BB_Knight.png"), graphics.Image(self.position, "Chess_Images/BG_Knight.png")] 
    
    def possibleMoves(self):
        self.moves = {}
        moveCount = 0
        xValues = [-2, -1, 2, 1]
        yValues = [-2, -1, 2, 1]
        for listX in range(len(xValues)):
            for listY in range(len(yValues)):
                if (listX + listY) % 2 == 1:
                    newX = self.position.getX() + xValues[listX]
                    newY = self.position.getY() + yValues[listY]
                    if newX > -1 and newX < 8 and newY > -1 and newY < 8:
                        self.moves[moveCount] = [graphics.Point(newX, newY), "move", 1]
                        moveCount += 1
    
class Pawn(Piece):
    def __init__(self, startingPos):
        self.color = None
        self.position = startingPos
        self.type = "pawn"
        self.moved = False
        self.moves = {}
        
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Pawn.png"), graphics.Image(self.position, "Chess_Images/WB_Pawn.png"), graphics.Image(self.position, "Chess_Images/WG_Pawn.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Pawn.png"), graphics.Image(self.position, "Chess_Images/BB_Pawn.png"), graphics.Image(self.position, "Chess_Images/BG_Pawn.png")] 
     
    def possibleMoves(self):
        self.moves = {}
        if self.color == "white":
            sideMult = 1
        else:
            sideMult = -1
        self.moves[0] = [graphics.Point(self.position.getX(), self.position.getY() + sideMult), "move", 1]
        if not self.moved:
            self.moves[1] = [graphics.Point(self.position.getX(), self.position.getY() + 2 * sideMult), "move", 2]

class Queen(Piece):
    def __init__(self, startingPos):
        self.color = None
        self.position = startingPos
        self.type = "queen"
        self.moved = False
        self.moves = {}
        
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Queen.png"), graphics.Image(self.position, "Chess_Images/WB_Queen.png"), graphics.Image(self.position, "Chess_Images/WG_Queen.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Queen.png"), graphics.Image(self.position, "Chess_Images/BB_Queen.png"), graphics.Image(self.position, "Chess_Images/BG_Queen.png")] 
    
    def possibleMoves(self):
        self.moves = {}
        moveCount = 0
        for possibleDistance in range(1, 8):
            getX = self.position.getX()
            posX = self.position.getX() + possibleDistance
            negX = self.position.getX() - possibleDistance
            getY = self.position.getY()
            posY = self.position.getY() + possibleDistance
            negY = self.position.getY() - possibleDistance
            if posX < 8:
                self.moves[moveCount] = [graphics.Point(posX, getY), "right", possibleDistance]
                moveCount += 1
                if posY < 8:
                    self.moves[moveCount] = [graphics.Point(posX, posY), "upright", possibleDistance]
                    moveCount += 1
                if negY > -1:
                    self.moves[moveCount] = [graphics.Point(posX, negY), "downright", possibleDistance]
                    moveCount += 1
            if negX > -1:
                self.moves[moveCount] = [graphics.Point(negX, getY), "left", possibleDistance]
                moveCount += 1
                if posY < 8:
                    self.moves[moveCount] = [graphics.Point(negX, posY), "upleft", possibleDistance]
                    moveCount += 1
                if negY > -1:
                    self.moves[moveCount] = [graphics.Point(negX, negY), "downleft", possibleDistance]
                    moveCount += 1
            if posY < 8:
                self.moves[moveCount] = [graphics.Point(getX, posY), "up", possibleDistance]
                moveCount += 1
            if negY > -1:
                self.moves[moveCount] = [graphics.Point(getX, negY), "down", possibleDistance]
                moveCount += 1
    
class Rook(Piece):
    def __init__(self, startingPos):
        self.color = None
        self.position = startingPos
        self.type = "rook"
        self.moved = False
        self.moves = {}
        
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Rook.png"), graphics.Image(self.position, "Chess_Images/WB_Rook.png"), graphics.Image(self.position, "Chess_Images/WG_Rook.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Rook.png"), graphics.Image(self.position, "Chess_Images/BB_Rook.png"), graphics.Image(self.position, "Chess_Images/BG_Rook.png")] 
            
    def possibleMoves(self):
        self.moves = {}
        moveCount = 0
        for possibleDistance in range(1, 8):
            getX = self.position.getX()
            posX = self.position.getX() + possibleDistance
            negX = self.position.getX() - possibleDistance
            getY = self.position.getY()
            posY = self.position.getY() + possibleDistance
            negY = self.position.getY() - possibleDistance
            if posX < 8:
                self.moves[moveCount] = [graphics.Point(posX, getY), "right", possibleDistance]
                moveCount += 1
            if posY < 8:
                self.moves[moveCount] = [graphics.Point(getX, posY), "up", possibleDistance]
                moveCount += 1
            if negX > -1:
                self.moves[moveCount] = [graphics.Point(negX, getY), "left", possibleDistance]
                moveCount += 1
            if negY > -1: 
                self.moves[moveCount] = [graphics.Point(getX, negY), "down", possibleDistance]
                moveCount += 1
            