import graphics
from piece import Bishop, King, Knight, Pawn, Piece, Queen, Rook

class Board:
    def __init__(self):
        self.pieceDict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        for row in self.pieceDict:
            for column in range(8):
                self.pieceDict[row].append(Piece(graphics.Point(row, column)))
    
    def setBoard(self):
        # Pawns
        for row in self.pieceDict:
            self.pieceDict[row][1] = Pawn(graphics.Point(row, 1))
            self.pieceDict[row][6] = Pawn(graphics.Point(row, 6))
        
        # Bishops
        self.pieceDict[2][0] = Bishop(graphics.Point(2,0))
        self.pieceDict[5][0] = Bishop(graphics.Point(5,0))
        self.pieceDict[2][7] = Bishop(graphics.Point(2,7))
        self.pieceDict[5][7] = Bishop(graphics.Point(5,7))
        
        # Kings
        self.pieceDict[4][0] = King(graphics.Point(4,0))
        self.pieceDict[4][7] = King(graphics.Point(4,7))
        
        # Knights
        self.pieceDict[1][0] = Knight(graphics.Point(1,0))
        self.pieceDict[6][0] = Knight(graphics.Point(6,0))
        self.pieceDict[1][7] = Knight(graphics.Point(1,7))
        self.pieceDict[6][7] = Knight(graphics.Point(6,7))
        
        # Queens
        self.pieceDict[3][0] = Queen(graphics.Point(3,0))
        self.pieceDict[3][7] = Queen(graphics.Point(3,7))
        
        # Rooks
        self.pieceDict[0][0] = Rook(graphics.Point(0,0))
        self.pieceDict[7][0] = Rook(graphics.Point(7,0))
        self.pieceDict[0][7] = Rook(graphics.Point(0,7))
        self.pieceDict[7][7] = Rook(graphics.Point(7,7))
        
        for piece in range(8):
            self.pieceDict[piece][0].setColor("white")
            self.pieceDict[piece][1].setColor("white")
            self.pieceDict[piece][6].setColor("black")
            self.pieceDict[piece][7].setColor("black")
            self.pieceDict[piece][0].setImages()
            self.pieceDict[piece][1].setImages()
            self.pieceDict[piece][6].setImages()
            self.pieceDict[piece][7].setImages()
                
    def imageBoard(self):
        self.win = graphics.GraphWin("Chess Board", 360, 360)
        self.win.setCoords(-6, -6, 12, 12)
        for row in self.pieceDict:
            for column in range(8):
                if (row + column) % 2 == 1:
                    self.pieceDict[row][column].images[0].draw(self.win)
                else:
                    self.pieceDict[row][column].images[1].draw(self.win)
        
    def fixPossibleMoves(self):
        for row in range(0, 8):
            for column in range(0, 8):
                currentPiece = self.pieceDict[row][column]
                currentPiece.possibleMoves()
                if currentPiece.type != None and currentPiece.type != "knight":
                    newMoves = []
                    maxDistance = {}
                    for possibleMove in currentPiece.moves:
                        if currentPiece.color != self.pieceDict[int(currentPiece.moves[possibleMove][0].getX())][int(currentPiece.moves[possibleMove][0].getY())].color:
                            if not currentPiece.moves[possibleMove][1] in maxDistance or currentPiece.type == "king":
                                newMoves.append(currentPiece.moves[possibleMove])
                        else:
                            maxDistance[currentPiece.moves[possibleMove][1]] = currentPiece.moves[possibleMove][2]
                    currentPiece.moves = newMoves
                if currentPiece.type != None:
                    print(currentPiece.type + str(currentPiece.moves) + "\n")