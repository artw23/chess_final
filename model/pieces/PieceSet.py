from model.pieces.Piece import Piece
from model.board.Square import Square
from model.pieces.types.King import King
from model.pieces.types.Pawn import Pawn
class PieceSet:
    def __init__(self, color):
        self.color = color
        self.pieces = [King(Square('A', 0)), Pawn(Square('B', 0))]
