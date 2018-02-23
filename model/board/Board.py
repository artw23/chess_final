from model.pieces.Piece import Piece
from model.pieces.PieceSet import PieceSet
from Square import Square
from model.colors.PieceColors import PieceColors


class Board:
    width = 8
    height = 8

    board = [[0 for x in range(width)] for y in range(height)]

    def __init__(self):
        for number in range(0,self.height):
            for letter in range(0,self.width):
                self.board[number][letter] = Square(letter,number)
        self.pieceSet = [PieceSet(PieceColors.BLUE), PieceSet(PieceColors.RED)]



    def intToChar(self, intValue):
        asciiLetter = intValue + ord('A')
        return str(unichr(asciiLetter))

    def charToInt(self, charValue):
        return ord(charValue) - ord('A')
