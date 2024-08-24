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