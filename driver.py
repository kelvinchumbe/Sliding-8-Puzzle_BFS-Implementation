import time
from Queue_Implementation import *


# function to check if the board state is the goal state
def is_goalstate(board):
    # check if numbers are in the correct order (goal state)
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    for i in range(len(goal_state)):
        if board[i] != goal_state[i]:
            return False

    return True


# Breadth First Search implementation
def bfs(initial_node):
    # initialize the frontier as a queue
    frontier = Queue()

    # add the initial node to the frontier
    frontier.enqueue(initial_node)

    # initialize the explored set so it only contains unique value/ nodes
    explored = set()

    # empty list that will contain the directions the blank space should move
    directions = []

    while not frontier.isEmpty():
        # get the first element in the queue, add it to the explored set then explore the node's children
        node = frontier.dequeue()
        explored.add(node)

        # check if selected node is the goal state
        if is_goalstate([x for sub in node.board_state for x in sub]):
            print("Goal State Found!!!")
            current_node = node

            # if this is the goal, traverse up the tree/ graph to identify the directions to move the blank space
            while current_node.parent is not None:
                if current_node.parent.find_blankpos()[0] > current_node.find_blankpos()[0]:
                    directions.append("up")

                if current_node.parent.find_blankpos()[0] < current_node.find_blankpos()[0]:
                    directions.append("down")

                if current_node.parent.find_blankpos()[1] > current_node.find_blankpos()[1]:
                    directions.append("left")

                if current_node.parent.find_blankpos()[1] < current_node.find_blankpos()[1]:
                    directions.append("right")

                current_node = current_node.parent

            print("These are the steps taken to get to the goal state")
            directions.reverse()
            print(directions)
            return directions

        # if the goal hasn't been found, identify the node's children i.e. the next posibble positions to move the blank space from its current position
        node.traverse_children()

        # link all the children to the parent node and is they havent been explored yet, add them to the frontier so they will be explored
        for child in node.children:
            child.parent = node
            if not frontier.contains(child) and child not in explored:
                frontier.enqueue(child)

    print("Did not find goal state")
    return False
