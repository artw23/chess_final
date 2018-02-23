from model.pieces.Piece import Piece
class Pawn(Piece):

    name = 'Pawn'
    displayName = 'P'

    xValidMoves = { 0}
    yValidMoves = {1, 0}

    xValidAttackMove = {1, -1}
    yValidAttackMove = {1}


    def __init__(self, square):
        Piece.__init__()
