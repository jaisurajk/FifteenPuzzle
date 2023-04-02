# author: Jaisuraj Kaleeswaran
# date: March 17, 2023
# file: fifteen.py creates a puzzle board game called Fifteen
# input: A number that moves on the puzzle board
# output: The game Fifteen that operates by the user inputs

import numpy as np
from random import choice

class Fifteen:
    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1, size**2)] + [0])  # create the tiles
        self.size = size
        self.adjtiles = self.getAdjTiles(size)
        
    #Helper method that gets the adjacent tiles
    def getAdjTiles(self, size):
        adjtiles = {}  
        for i in range(size**2):
            adjtiles[i] = []
            if i % size != 0:
                adjtiles[i].append(i - 1)
            if (i + 1) % size != 0:
                adjtiles[i].append(i + 1)
            if i - size >= 0:
                adjtiles[i].append(i - size)
            if size**2 > i + size:
                adjtiles[i].append(i + size)
        return adjtiles
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
    def draw(self):  # draw the game
        print(f"\n {self.size * '+---'}+")
        for i in range(self.size):
            print(' |', end = '')
            for j in range(self.size):
                tile_spot = self.tiles[j + self.size * i]
                if 9 < tile_spot:
                    print(f'{tile_spot} |', end = '')
                elif tile_spot == 0:
                    print('   |', end = '')
                else:
                    print(f'{tile_spot:2} |', end = '')
            print(f"\n {self.size * '+---'}+")
        print()

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 
    def __str__(self):
        s = str()
        for i in range(self.size):
            for j in range(self.size):
                tile_spot = self.tiles[j + self.size * i]
                if 1 <= tile_spot:  # if the tile is not 0
                    s += f'{tile_spot:2} ' # add the tile to the string
                else:
                    s += "   "  #Add an empty string
            s += "\n"
        return s

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j): 
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move):
        ind = np.where(self.tiles == 0)[0][0]  # get index of 0
        for i in self.adjtiles[ind]:
            if move == self.tiles[i]:  # if move is adjacent to 0
                return True
        return False

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move):
        ind = np.where(self.tiles == 0)[0][0]  # get index of 0
        if self.is_valid_move(move):  # if the move is valid
            # for each adjacent tile
            for i in self.adjtiles[ind]:  
                if self.tiles[i] == move:  # if the tile is the move, swap them and then break
                    self.tiles[ind], self.tiles[i] = self.tiles[i], self.tiles[ind]
                    break
    
    # shuffle tiles
    def shuffle(self, moves = 100):
        ind = np.where(self.tiles == 0)[0][0]  # get index of 0
        for i in range(moves):
            tile_shf = choice(self.adjtiles[ind])  # choose a random move
            self.tiles[tile_shf], self.tiles[ind] = self.tiles[ind], self.tiles[tile_shf]
            ind = tile_shf  # update index
    
    # verify if the puzzle is solved
    def is_solved(self):  # check if the game is solved
        tot_solve = len(self.tiles) - 1
        for i in range(tot_solve):
            if i != self.tiles[i] - 1: # if the tile is not in the correct position
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