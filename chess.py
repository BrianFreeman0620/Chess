from board import Board
import graphics

gameEnd = False
lastClicked = None

chessBoard = Board()
chessBoard.setBoard()
chessBoard.imageBoard()
chessBoard.fixPossibleMoves()
while not gameEnd:
    currentClick = chessBoard.win.getMouse()
    clickPosition = graphics.Point(round(currentClick.getX()), round(currentClick.getY()))
    if lastClicked != None and not (clickPosition.getX() == lastClicked.position.getX() and clickPosition.getY() == lastClicked.position.getY()):
        legalMove = False
        for possibleMove in range(len(lastClicked.moves)):
            currentMove = lastClicked.moves[possibleMove][0]
            if currentMove.getX() == clickPosition.getX() and currentMove.getY() == clickPosition.getY():
                legalMove = True
        if legalMove:
            chessBoard.movePiece(chessBoard.pieceDict[int(lastClicked.position.getX())][int(lastClicked.position.getY())], clickPosition)
    lastClicked = chessBoard.selectPiece(clickPosition, lastClicked)
    chessBoard.fixPossibleMoves()
chessBoard.win.close()