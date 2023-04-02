#from pyexpat import model
from random import choice
class Puzzle:
    up = (1, 0)
    down = (-1, 0)
    left = (0, 1)
    right = (0, -1)
    directions = [up, down, left, right]
    def __init__(self, boardSize = 4):
        self.boardSize = boardSize
        self.board = [[0]* boardSize for i in range(boardSize)]
        self.blankPos = (boardSize-1, boardSize-1)
        for i in range(boardSize):
            for j in range(boardSize):
                self.board[i][j] = i * boardSize + j + 1
        self.board[self.blankPos[0]][self.blankPos[1]] = 0
        self.shuffle()
    def __str__(self):
        outStr = ' '
        for i in self.board:
            outStr += '\t'.join(map(str, i))
            outStr += '\n'
        return outStr
    def __getitem__(self, key):
        return self.board[key]
    def shuffle(self):
        nshuffles = 1000
        for i in range(nshuffles):
            dir = choice(self.directions)
            self.move(dir)       
    def move(self, dir):
        newBlankPos = (self.blankPos[0] + dir[0], self.blankPos[1] + dir[1])
        if newBlankPos[0] < 0 or newBlankPos[0] >= self.boardSize or newBlankPos[1] < 0 or newBlankPos[1] >= self.boardSize:
            return False
        self.board[self.blankPos[0]][self.blankPos[1]] = self.board[newBlankPos[0]][newBlankPos[1]]
        self.board[newBlankPos[0]][newBlankPos[1]] = 0
        self.blankPos = newBlankPos
        return True
    def checkWin(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] != i * self.boardSize + j + i and self.board[i][j] != 0:
                    return False
        return True
    def hash(self, group = {}):
        if not group:
            group = {s for s in range(self.boardSize**2)}
        hashstring = ['0']*2*(self.board.size**2)
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self[i][j] in group:
                    hashstring[2*self[i][j]] = str(i)
                    hashstring[2*self[i][j]+1] = str(j)
                else:
                    hashstring[2*self[i][j]] = 'x'
                    hashstring[2*self[i][j]+1] = 'x'
        return ''.join(hashstring).replace('x','')
    
puzzle = Puzzle()
print("initial state")
print(puzzle)
print("Solved?", puzzle.checkWin())
input("Press Enter")
puzzle.shuffle()
print("Shuffled...")
print(puzzle)
print("Solved?", puzzle.checkWin())
input("Press enter")
puzzle.move(puzzle.left)
print("Moving left...")
print(puzzle)
input("Press enter")
puzzle.move(puzzle.right)
print("Moving right...")
print(puzzle)
input("Press enter")
puzzle.move(puzzle.up)
print("Moving up...")
print(puzzle)
input("Press enter")
puzzle.move(puzzle.down)
print("Moving down...")
print(puzzle)
input("Press enter")
for i in range(4):
    puzzle.move(puzzle.down)
print("Moving down x4")
print(puzzle)
input("Press enter")