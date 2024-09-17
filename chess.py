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
    clickedPiece = chessBoard.pieceDict[int(clickPosition.getX())][int(clickPosition.getY())]
    if lastClicked != None:
        lastClicked.images[2].undraw()
        if (int(lastClicked.position.getX()) + int(lastClicked.position.getY())) % 2 == 1:
            lastClicked.images[0].draw(chessBoard.win)
        else:
            lastClicked.images[1].draw(chessBoard.win)
    if (int(clickPosition.getX()) + int(clickPosition.getY())) % 2 == 1:
        clickedPiece.images[0].undraw()
    else:
        clickedPiece.images[1].undraw()
    clickedPiece.images[2].draw(chessBoard.win)
    lastClicked = clickedPiece
chessBoard.win.close()