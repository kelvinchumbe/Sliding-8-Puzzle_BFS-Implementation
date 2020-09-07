# Create the actual game board but as a node to help facilitate graph traversal

class BoardNode:
    def __init__(self, board):
        self.board_state = [[], [], []]
        self.depth = 0
        self.children = []
        self.cost = 0
        self.g_score = float("inf")
        self.f_score = 0
        self.parent = None

        self.board_state[0] = board[:3]
        self.board_state[1] = board[3:6]
        self.board_state[2] = board[6:]

    # method to display the board
    def display_board(self):
        for i in range(len(self.board_state)):
            for j in range(len(self.board_state[i])):
                print(self.board_state[i][j])
            print('\n')

    # method to find the blank position (denoted by a 0) on the board
    def find_blankpos(self):
        for i in range(len(self.board_state)):
            for j in range(len(self.board_state)):
                if self.board_state[i][j] == 0:
                    return [i, j]

    # method to identify the next possible position/ move on the board, convert the board state to a node and add it as a child to the current node
    def traverse_children(self):
        blank_pos = self.find_blankpos()

        # make copies of the board so you dont overwrite its current state
        state1 = self.make_board_copy()
        state2 = self.make_board_copy()
        state3 = self.make_board_copy()
        state4 = self.make_board_copy()

        # For each of the identified children, create a Node from its board's state

        up_child = self.check_Up_Child(state1, blank_pos)
        if up_child is not None:
            up_node = BoardNode(up_child)
            self.children.append(up_node)

        down_child = self.check_Down_Child(state2, blank_pos)
        if down_child is not None:
            down_node = BoardNode(down_child)
            self.children.append(down_node)

        left_child = self.check_Left_Child(state3, blank_pos)
        if left_child is not None:
            left_node = BoardNode(left_child)
            self.children.append(left_node)

        right_child = self.check_Right_Child(state4, blank_pos)
        if right_child is not None:
            right_node = BoardNode(right_child)
            self.children.append(right_node)

    # method to make a copy of the board
    def make_board_copy(self):
        new_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.board_state)):
            for j in range(len(self.board_state[i])):
                new_list[i][j] = self.board_state[i][j]

        return new_list

    # check if the blank space can be moved up, if so create a board state of the move's (upward move) board state
    def check_Up_Child(self, board_state, blank_pos):
        if blank_pos[0] > 0:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0] - 1][blank_pos[1]]
            board_state[blank_pos[0] - 1][blank_pos[1]] = temp

            self.cost += 1

            return [x for sub in board_state for x in sub]

        else:
            return None

    # check if the blank space can be moved down, if so create a board state of the move's (downward move) board state
    def check_Down_Child(self, board_state, blank_pos):
        if blank_pos[0] < 2:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0] + 1][blank_pos[1]]
            board_state[blank_pos[0] + 1][blank_pos[1]] = temp

            self.cost += 1

            return [x for sub in board_state for x in sub]

        else:
            return None

    # check if the blank space can be moved to the left, if so create a board state of the move's (left move) board state
    def check_Left_Child(self, board_state, blank_pos):
        if blank_pos[1] > 0:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0]][blank_pos[1] - 1]
            board_state[blank_pos[0]][blank_pos[1] - 1] = temp

            self.cost += 1

            return [x for sub in board_state for x in sub]

        else:
            return None

    # check if the blank space can be moved to the right, if so create a board state of the move's (right move) board state
    def check_Right_Child(self, board_state, blank_pos):
        if blank_pos[1] < 2:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0]][blank_pos[1] + 1]
            board_state[blank_pos[0]][blank_pos[1] + 1] = temp

            self.cost += 1

            return [x for sub in board_state for x in sub]


        else:
            return None

    def __lt__(self, other):
        return self.f_score < other.f_score

    def __str__(self):
        return ''.join([str(x) + "," for sub in self.board_state for x in sub])
