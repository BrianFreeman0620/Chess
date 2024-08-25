import graphics

class Piece:
    def __init__(self, startingPos):
        self.color = None
        self.position = startingPos
        self.type = None
        
    def setColor(self, color):
        self.color = color
        
    def changePosition(self, newPosition):
        self.position = newPosition

class Bishop(Piece):
    def __init__(self,startingPos):
        self.color = None
        self.position = startingPos
        self.type = "bishop"
    
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Bishop.png"), graphics.Image(self.position, "Chess_Images/WB_Bishop.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Bishop.png"), graphics.Image(self.position, "Chess_Images/BB_Bishop.png")] 

class King(Piece):
    def __init__(self,startingPos):
        self.color = None
        self.position = startingPos
        self.type = "king"
    
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_King.png"), graphics.Image(self.position, "Chess_Images/WB_King.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_King.png"), graphics.Image(self.position, "Chess_Images/BB_King.png")] 

class Knight(Piece):
    def __init__(self,startingPos):
        self.color = None
        self.position = startingPos
        self.type = "knight"
    
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Knight.png"), graphics.Image(self.position, "Chess_Images/WB_Knight.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Knight.png"), graphics.Image(self.position, "Chess_Images/BB_Knight.png")] 
        
class Pawn(Piece):
    def __init__(self, startingPos):
        self.color = None
        self.position = startingPos
        self.type = "pawn"
        
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Pawn.png"), graphics.Image(self.position, "Chess_Images/WB_Pawn.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Pawn.png"), graphics.Image(self.position, "Chess_Images/BB_Pawn.png")] 
            
class Rook(Piece):
    def __init__(self, startingPos):
        self.color = None
        self.position = startingPos
        self.type = "rook"
        
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Rook.png"), graphics.Image(self.position, "Chess_Images/WB_Rook.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Rook.png"), graphics.Image(self.position, "Chess_Images/BB_Rook.png")] 
            
class Queen(Piece):
    def __init__(self, startingPos):
        self.color = None
        self.position = startingPos
        self.type = "queen"
        
    def setImages(self):
        if self.color == "white":
            self.images = [graphics.Image(self.position, "Chess_Images/WW_Queen.png"), graphics.Image(self.position, "Chess_Images/WB_Queen.png")] 
        else:
            self.images = [graphics.Image(self.position, "Chess_Images/BW_Queen.png"), graphics.Image(self.position, "Chess_Images/BB_Queen.png")] 