class Square:

    def __init__(self, letter, number):
        self.columnLetter = letter
        self.rowNumber = number

    def getColumnNumber(self):
        return self.charToInt(self.columnLetter)

    def getRowNumber(self):
        return self.rowNumber

    def intToChar(self, intValue):
        asciiLetter = intValue + ord('A')
        return str(unichr(asciiLetter))

    def charToInt(self, charValue):
        return ord(charValue) - ord('A')
