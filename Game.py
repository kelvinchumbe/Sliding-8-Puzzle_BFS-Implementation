# This is the main game file
from driver import *
from Board_Visualizer import *

# Input 1: [1, 2, 5, 3, 4, 0, 6, 7, 8])

if __name__ == '__main__':
    board = input("Enter the board state as a list e.g. '1,2,3,4,5,6,7,8,0': \n")
    board = board.split(",")
    for i in range(len(board)):
        board[i] = int(board[i])

    gameboard = GameBoard(board)
    gameboard.draw_board(board)

    print(" BFS Game")
    bfs_solver = Solver(board, [0, 1, 2, 3, 4, 5, 6, 7, 8])
    directions = bfs_solver.A_Star()
    gameboard.auto_Play(directions)


    print(" A_Star Game")
    a_star_solver = Solver(board, [0,1,2,3,4,5,6,7,8])
    directions2 = a_star_solver.A_Star()
    gameboard.auto_Play(directions2)