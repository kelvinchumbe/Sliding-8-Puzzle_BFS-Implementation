# Create a class to implement and visualize the board
from BoardNode import *
import time

# Class that implements the actual sliding 8_puzzle game board
# Create an instance of the graph by initializing the game board with the the root node
class GameBoard:
    def __init__(self, board):
        self.board_node = BoardNode(board)
        self.blank_pos = self.board_node.find_blankpos()

    # method to move the blank position upward on the game board
    def move_Up(self, board_state, blank_pos):
        if blank_pos[0] > 0:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0] - 1][blank_pos[1]]
            board_state[blank_pos[0] - 1][blank_pos[1]] = temp

        return [x for sub in board_state for x in sub]

    # method to move the blank position downward on the game board
    def move_Down(self, board_state, blank_pos):
        if blank_pos[0] < 2:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0] + 1][blank_pos[1]]
            board_state[blank_pos[0] + 1][blank_pos[1]] = temp

            return [x for sub in board_state for x in sub]

    # method to move the blank position left on the game board
    def move_Left(self, board_state, blank_pos):
        if blank_pos[1] > 0:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0]][blank_pos[1] - 1]
            board_state[blank_pos[0]][blank_pos[1] - 1] = temp

            return [x for sub in board_state for x in sub]

    # method to move the blank position right on the game board
    def move_Right(self, board_state, blank_pos):
        if blank_pos[1] < 2:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0]][blank_pos[1] + 1]
            board_state[blank_pos[0]][blank_pos[1] + 1] = temp

            return [x for sub in board_state for x in sub]

    # method to draw the game boards current state
    def draw_board(self, board):
        print("+-+-+-+-+-+-+")
        print("| " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + " |")
        print("-------------")
        print("| " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + " |")
        print("-------------")
        print("| " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + " |")
        print("+-+-+-+-+-+-+")

        print("\n")

    # method to automatically play the game after the directions to move the blank space have been determined
    def auto_Play(self, directions):
        if directions[0] is not False:
            for direction in directions:
                print(direction)
                if direction is "up":
                    new_board_state = self.move_Up(self.board_node.board_state, self.blank_pos)
                    self.board_node = BoardNode(new_board_state)
                    self.blank_pos = self.board_node.find_blankpos()
                    self.draw_board(new_board_state)

                elif direction is "down":
                    new_board_state = self.move_Down(self.board_node.board_state, self.blank_pos)
                    self.board_node = BoardNode(new_board_state)
                    self.blank_pos = self.board_node.find_blankpos()
                    self.draw_board(new_board_state)

                elif direction is "left":
                    new_board_state = self.move_Left(self.board_node.board_state, self.blank_pos)
                    self.board_node = BoardNode(new_board_state)
                    self.blank_pos = self.board_node.find_blankpos()
                    self.draw_board(new_board_state)

                elif direction is "right":
                    new_board_state = self.move_Right(self.board_node.board_state, self.blank_pos)
                    self.board_node = BoardNode(new_board_state)
                    self.blank_pos = self.board_node.find_blankpos()
                    self.draw_board(new_board_state)

                time.sleep(2)
