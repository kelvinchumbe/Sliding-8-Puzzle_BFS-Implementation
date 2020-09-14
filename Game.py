# This is the main game file
from driver import *
from Board_Visualizer import *
import sys

if __name__ == '__main__':
    # Run program from command line with Game.py initial_board_state final_board_state i.e. > Game.py 0,1,2,3,4,5,6,7,8,9 0,9,8,7,6,5,4,3,2,1

    board = sys.argv[1]
    goal_state = sys.argv[2]
    solver_function = sys.argv[3]

    board = board.split(",")
    goal_state = goal_state.split(",")

    for i in range(len(board)):
        board[i] = int(board[i])
        goal_state[i] = int(goal_state[i])



    gameboard = GameBoard(board)
    gameboard.draw_board(board)

    if solver_function == "bfs":
        print("Solving Puzzle by BFS Algorithm... \n")
        bfs_solver = Solver(board, goal_state)
        directions = bfs_solver.bfs()
        gameboard.auto_Play(directions)

    elif solver_function == "a_star":
        print("Solving Puzzle by A_Star Algorithm... \n")
        a_star_solver = Solver(board, goal_state)
        directions2 = a_star_solver.A_Star()
        gameboard.auto_Play(directions2)
