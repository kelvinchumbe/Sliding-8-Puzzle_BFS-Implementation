import time


# Create a graph node which represents a state of the board
# Algorithms BFS

class Queue:
    # define the constructor which initializes an empty list, the size of the list to 0 and sets the max size of the list
    def __init__(self):
        self.items = []
        self.size = 0

    # method to add items to the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # method to remove items from the queue. Items that entered first in the queue are accessed first and removed. Method returns the item that has been removed
    def dequeue(self):
        return self.items.pop()

    # method to check the queue returns access the first item that would be accessed in the queue
    def peek(self):
        return self.items[-1]

    # method that return a boolean is the queue/ list is empty or not
    def isEmpty(self):
        return self.items == []

    # method to check if an item is present in the queue
    def contains(self, elem):
        for item in self.items:
            if elem == item:
                return True

        return False


class Node:
    def __init__(self, board):
        self.board_state = [[], [], []]
        self.depth = 0
        self.children = []
        self.cost = 0
        self.parent = None

        self.board = board

        self.board_state[0] = self.board[:3]
        self.board_state[1] = self.board[3:6]
        self.board_state[2] = self.board[6:]

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

        state1 = self.make_board_copy()
        state2 = self.make_board_copy()
        state3 = self.make_board_copy()
        state4 = self.make_board_copy()

        up_child = self.move_blankSpace_Up(state1, blank_pos)
        if up_child is not None:
            up_node = Node(up_child)
            self.children.append(up_node)

        down_child = self.move_blankSpace_Down(state2, blank_pos)
        if down_child is not None:
            down_node = Node(down_child)
            self.children.append(down_node)

        left_child = self.move_blankSpace_Left(state3, blank_pos)
        if left_child is not None:
            left_node = Node(left_child)
            self.children.append(left_node)

        right_child = self.move_blankSpace_Right(state4, blank_pos)
        if right_child is not None:
            right_node = Node(right_child)
            self.children.append(right_node)

    # method to make a copy of the board
    def make_board_copy(self):
        new_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.board_state)):
            for j in range(len(self.board_state[i])):
                new_list[i][j] = self.board_state[i][j]

        return new_list

    # method to move the blank space once upwards
    def move_blankSpace_Up(self, board_state, blank_pos):
        if blank_pos[0] > 0:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0] - 1][blank_pos[1]]
            board_state[blank_pos[0] - 1][blank_pos[1]] = temp

            self.cost += 1

            return [x for sub in board_state for x in sub]

        else:
            return None

    # method to move the blank space once downwards
    def move_blankSpace_Down(self, board_state, blank_pos):
        if blank_pos[0] < 2:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0] + 1][blank_pos[1]]
            board_state[blank_pos[0] + 1][blank_pos[1]] = temp

            self.cost += 1

            return [x for sub in board_state for x in sub]

        else:
            return None

    # method to move the blank space once left
    def move_blankSpace_Left(self, board_state, blank_pos):
        if blank_pos[1] > 0:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0]][blank_pos[1] - 1]
            board_state[blank_pos[0]][blank_pos[1] - 1] = temp

            self.cost += 1

            return [x for sub in board_state for x in sub]

        else:
            return None

    # method to move the blank space once right
    def move_blankSpace_Right(self, board_state, blank_pos):
        if blank_pos[1] < 2:
            temp = board_state[blank_pos[0]][blank_pos[1]]
            board_state[blank_pos[0]][blank_pos[1]] = board_state[blank_pos[0]][blank_pos[1] + 1]
            board_state[blank_pos[0]][blank_pos[1] + 1] = temp

            self.cost += 1

            return [x for sub in board_state for x in sub]

        else:
            return None

    def __str__(self):
        return ''.join([str(x) + "," for sub in self.board_state for x in sub])

# Breadth First Search implementation
def bfs(initial_state):
    initial_node = Node(initial_state)
    frontier = Queue()
    frontier.enqueue(initial_node)
    explored = set()

    directions = []

    while not frontier.isEmpty():
        node = frontier.dequeue()
        explored.add(node)

        if is_goalstate([x for sub in node.board_state for x in sub]):
            print("Goal State Found!!!")
            current_node = node

            while current_node.parent is not None:
                if current_node.parent.find_blankpos()[0] > current_node.find_blankpos()[0]:
                    directions.append("up")

                if current_node.parent.find_blankpos()[0] < current_node.find_blankpos()[0]:
                    directions.append(" down")

                if current_node.parent.find_blankpos()[1] > current_node.find_blankpos()[1]:
                    directions.append(" left")

                if current_node.parent.find_blankpos()[1] < current_node.find_blankpos()[1]:
                    directions.append(" right")

                current_node = current_node.parent

            print("Read directions from the last to first. These are the steps taken to get to the goal state")
            print(directions)
            return True

        node.traverse_children()

        for child in node.children:
            child.parent = node
            if not frontier.contains(child) and child not in explored:
                frontier.enqueue(child)

    print("Did not find goal state")
    return False

# function to check if the board state is the goal state
def is_goalstate(board):
    # check if numbers are in the correct order
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for i in range(len(goal_state)):
        if board[i] != goal_state[i]:
            return False

    return True


# Time how fast the algorithm runs with a test case
start_time = time.time()
bfs([1, 2, 5, 3, 4, 0, 6, 7, 8])
print(time.time() - start_time)
