﻿class Board():
    def __init__(self, size):
        self.size = size
        self.setBoard()

    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = None
                row.append(piece)
            self.board.append(row)