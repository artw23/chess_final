from model.colors.PieceColors import PieceColors
class ChessUi:

    def printBoard(self, board):
        self.width = board.width
        self.height = board.height
        self.uiBoard = [[0 for x in range(self.width)] for y in range(self.height)]

        for pieceSet in board.pieceSet:
            for piece in pieceSet.pieces:
                self.uiBoard[piece.currentPosition.getColumnNumber()][piece.currentPosition.getRowNumber()] = pieceSet.color+piece.getPieceDisplayName()+PieceColors.ENDC





        print('\n\t\t-- Chess Board--\n')
        self.printRows()
        self.printLetters()
        print('\n')

    def printDivision(self):
        line = ''
        for letter in range(0,self.width):
            line = line + '-----'
        print line

    def printRows(self):
        for number in range(0,self.height):
            print '| {}'.format(number + 1),
            for letter in range(0,self.width):
                print '| {}'.format(self.uiBoard[letter][number]),
            print '|'
            self.printDivision()

    def printLetters(self, board):
        print '| -',
        for letter in range(0,self.width):
            asciiLetter = self.intToChar(letter)
            print '| {}'.format(asciiLetter),
        print '|'

    def intToChar(self, intValue):
        asciiLetter = intValue + ord('A')
        return str(unichr(asciiLetter))
