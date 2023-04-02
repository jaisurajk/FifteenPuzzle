import numpy as np
from random import choice

class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4): 
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.size = size

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        for i in range(self.size):
            print("+---" * self.size + "+")
            row = "|"
            for j in range(self.size):
                if self.tiles[i*self.size + j] == 0:
                    row += "   |"
                else:
                    row += " " + str(self.tiles[i*self.size + j]).rjust(2) + " |"
            print(row)
        print("+---" * self.size + "+")

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 
    def __str__(self): 
        res = ""
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if self.tiles[i*self.size + j] == 0:
                    row += "   "
                else:
                    row += str(self.tiles[i*self.size + j]).rjust(2) + " "
            res += row.rstrip() + "\n"
        return res.rstrip()

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j): 
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move):  
        i, j = move
        if self.tiles[i] == 0 and self.tiles[j] in self.neighbors(i):
            return True
        if self.tiles[j] == 0 and self.tiles[i] in self.neighbors(j):
            return True
        return False
    
    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move): 
        if self.is_valid_move(move):
            self.transpose(*move)

    # shuffle tiles
    def shuffle(self, moves=100):
        for a in range(moves):
            neighbors = [i for i, x in enumerate(self.tiles) if x == 0]
            move = (choice(neighbors), choice(self.neighbors(neighbors[0])))
            self.update(move)
    def is_solved(self):
        for i in range(len(self.tiles) - 1):
            if self.tiles[i] != i+1:
                return False
        return True
    
if __name__ == '__main__':

    game = Fifteen()
    print(str(game))
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    print("All tests passed")

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')