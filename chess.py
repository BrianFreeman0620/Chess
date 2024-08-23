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
    
    
class Board:
    def __init__(self):
        self.pieceDict = {"A":[], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []}
        for row in self.pieceDict:
            for column in range(1, 9):
                self.pieceDict[row].append(Piece((row, column)))
                
    def setBoard(self):
        for row in self.pieceDict:
            self.pieceDict[row][1] = Pawn((row, 2))
            self.pieceDict[row][1].setColor("white")
            self.pieceDict[row][1] = Pawn((row, 7))
            self.pieceDict[row][1].setColor("black")
                
    
                
chessBoard = Board()
chessBoard.setBoard()
print(chessBoard.pieceDict)