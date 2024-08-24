import graphics
from piece import Pawn, Piece, Rook

class Board:
    def __init__(self):
        self.pieceDict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        for row in self.pieceDict:
            for column in range(8):
                self.pieceDict[row].append(Piece(graphics.Point(row, column)))
        self.image = graphics.Image(graphics.Point(3.5, 3.5), "Chess_Images/Chess_Board.png")
    
    def setBoard(self):
        # Pawns
        for row in self.pieceDict:
            self.pieceDict[row][1] = Pawn(graphics.Point(row, 1))
            self.pieceDict[row][1].setColor("white")
            self.pieceDict[row][6] = Pawn(graphics.Point(row, 6))
            self.pieceDict[row][6].setColor("black")
            self.pieceDict[row][1].setImages()
            self.pieceDict[row][6].setImages()
        
        # Rooks
        self.pieceDict[0][0] = Rook(graphics.Point(0,0))
        self.pieceDict[0][0].setColor("white")
        self.pieceDict[7][0] = Rook(graphics.Point(7,0))
        self.pieceDict[7][0].setColor("white")
        self.pieceDict[0][7] = Rook(graphics.Point(0,7))
        self.pieceDict[0][7].setColor("black")
        self.pieceDict[7][7] = Rook(graphics.Point(7,7))
        self.pieceDict[7][7].setColor("black")
        self.pieceDict[0][0].setImages()
        self.pieceDict[7][0].setImages()
        self.pieceDict[0][7].setImages()
        self.pieceDict[7][7].setImages()
        
        print(self.pieceDict)
                
    def imageBoard(self):
        self.win = graphics.GraphWin("Chess Board", 360, 360)
        self.win.setCoords(-6, -6, 12, 12)
        self.image.draw(self.win)
        for row in self.pieceDict:
            for column in range(8):
                if not self.pieceDict[row][column].color == None:
                    if (row + column) % 2 == 1:
                        self.pieceDict[row][column].images[0].draw(self.win)
                    else:
                        self.pieceDict[row][column].images[1].draw(self.win)
        self.win.getMouse()
        self.win.close()