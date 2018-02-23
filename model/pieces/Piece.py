from model.board.Square import Square
from abc import ABCMeta, abstractmethod

class Piece:

    __metaclass__ = ABCMeta

    def getPieceDisplayName(self):
        raise NotImplementedError()


    def __init__(self, square):
        self.currentPosition = square
        pass


    def isValidMove(self,square):
        actualX = self.currentPosition.getColumnNumber()
        actualY = self.currentPosition.getRowNumber()

        futureX = square.getColumnNumber()
        futureY = square.getRowNumber()
        for xMove in xValidMoves:
            for yMove in yValidMoves:
                validXMove = actualX + xMove
                validYMove = actualY + yMove
                if futureX == validXMove and futureY == validYMove:
                    return true
        return false
