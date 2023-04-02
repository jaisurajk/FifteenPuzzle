from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
class A:
    # Define the initial state of the puzzle board and the goal state.
    # Create an open list and a closed list to keep track of visited nodes.
    # Add the initial state to the open list.
    # While the open list is not empty:
    # a. Select the node with the lowest cost f(n) = g(n) + h(n), where g(n) is the cost to reach the current node and h(n) is the estimated cost to reach the goal state from the current node.
    # b. If the selected node is the goal state, terminate and return the path from the initial state to the goal state.
    # c. Expand the selected node by generating its successor states.
    # d. For each successor state, calculate its f(n) value and add it to the open list if it has not been visited yet.
    # e. Mark the selected node as visited and add it to the closed list.

class IDS:
    # Define the initial state of the puzzle board and the goal state.
    # Define a maximum depth limit for the search.
    # For each depth limit, perform a Breadth-First Search (BFS) starting from the initial state up to the defined depth limit.
    # If the goal state is found during the BFS, terminate and return the path from the initial state to the goal state.
    # If the goal state is not found, increase the depth limit and repeat the search.
    # Iterative Deepening A* (IDA*):

class IDA:
    # Define the initial state of the puzzle board and the goal state.
    # Define a heuristic function h(n) that estimates the cost to reach the goal state from node n.
    # Set the initial depth limit to the estimated cost to reach the goal state from the initial state.
    # While the depth limit is not infinite:
    # a. Perform a Depth-First Search (DFS) starting from the initial state up to the defined depth limit, selecting nodes with the lowest f(n) value.
    # b. If the goal state is found during the DFS, terminate and return the path from the initial state to the goal state.
    # c. If the goal state is not found, update the depth limit to the lowest f(n) value of the unvisited nodes and repeat the search.