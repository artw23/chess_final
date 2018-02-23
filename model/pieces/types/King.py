from model.pieces.Piece import Piece
class King(Piece):

    name = 'King'
    displayName = 'K'

    xValidMoves = {1, 0, -1}
    yValidMoves = {1, 0, -1}

    xValidAttackMove = {1, 0, -1}
    yValidAttackMove = {1, 0, -1}

    def __init__(self, square):
        Piece.__init__(square)
