from solver2 import Puzzle
from collections import deque
import pickle
def buildPatternDb(boardSize, group):
    puzzle = Puzzle(boardSize, shuffle = False)
    puzzle.count = 0
    groupWithblank = group.copy()
    groupWithblank.add(0)
    visited = set()
    closedlist = {}
    openlist = deque()
    openlist.append((puzzle,(0, 0)))
    while openlist:
        cur, prevmove = openlist.popleft()
        if not visitNode(cur, visited, closedlist, groupWithblank, group):
            continue
        for dir in puzzle.directions:
            if dir == prevmove:
                continue
            validMove, simPuzzle = cur.simulateMove(dir)
            if not validMove:
                continue
            if simPuzzle[cur.blankPos[0]][cur.blankPos[1]] in group:
                simPuzzle.count += 1
            openlist.append((simPuzzle, (-dir)))
    return closedlist
def visitNode(puzzle, visited, closedlist, groupWithblank, group):
    puzzleHashWithBlank = puzzle.hash(groupWithblank)
    if puzzleHashWithBlank in visited:
        return False
    visited.add(puzzleHashWithBlank)
    groupHash = puzzle.hash(group)
    if groupHash not in closedlist:
        closedlist[groupHash] = puzzle.count
    elif closedlist[groupHash] > puzzle.count:
        closedlist[groupHash] = puzzle.count
    return True

def main():
    boardSize = 4
    groups = [{1, 5, 6, 9, 10, 13}, {7, 8, 11, 12, 14, 15}, {2, 3, 4}]
    closedlist = []
    for group in groups:
        closedlist.append(buildPatternDb(boardSize, group))
    with open('patternDb_'+str(boardSize)+'.dat', 'wb') as patternDbFile:
        pickle.dump(groups, patternDbFile)
        pickle.dump(closedlist, patternDbFile)
    for i in range(len(closedlist)):
        group = closedlist[i]
        print("Group:", groups[i], len(group), "permutations")

if __name__ == 'main':
    main()
    
        