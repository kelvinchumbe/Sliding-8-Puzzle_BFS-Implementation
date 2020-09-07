import time
from Queue_Implementation import *
from PriorityQueue_Implementation import PriorityQueue
from BoardNode import *


class Solver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    # method to check if the board state is the goal state
    def is_goalstate(self, board):
        for i in range(len(self.goal_state)):
            if board[i] != self.goal_state[i]:
                return False

        return True

    def hamming_distance(self, node, goal_state):
        misplaced = 0
        board_state = [x for sub in node.board_state for x in sub]

        for i in range(len(board_state)):
            if (board_state[i] != 0) and (board_state[i] != goal_state[i]):
                misplaced += 1

        return misplaced

    def bfs(self):
        # Create root of the tree
        initial_node = BoardNode(self.initial_state)

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
            if self.is_goalstate([x for sub in node.board_state for x in sub]):
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

    def A_Star(self):
        # initialize the root/ start node
        initial_node = BoardNode(self.initial_state)

        # Create an open list which implements a priority queue. Contains unvisited nodes
        openlist = PriorityQueue()

        # Create a closed list. Contains visited nodes
        closedlist = set()

        # List to hold the directions/ moves to make
        directions = []

        # No of nodes explored
        node_explored = 0

        # Initialize the start node's g_score to 0 i.e. number of nodes that have been traversed to this node
        initial_node.g_score = 0

        # Initialize the start node's h_score to the initial number of misplaced tiles
        h_score = self.hamming_distance(initial_node, [0, 1, 2, 3, 4, 5, 6, 7, 8])

        # f_score = g_score + h_score
        initial_node.f_score = initial_node.g_score + h_score

        # Add the initial node to the openlist with its f_score as its priority
        openlist.push(initial_node.f_score, initial_node)

        while not openlist.isEmpty():
            node_explored += 1
            print(node_explored)
            node = openlist.pop()[1]

            if self.is_goalstate([x for sub in node.board_state for x in sub]):
                print("Goal State Found!!!")
                current_node = node

                # if this is the goal, traverse up the tree / graph to identify the directions to move the blank space
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

            closedlist.add(node)

            # link all the children to the parent node and is they haven't been explored yet, add them to the frontier so they will be explored
            for child in node.children:
                if child in closedlist:
                    continue

                tent_g_score = node.g_score + 1

                if openlist.exists(child) and tent_g_score < child.g_score:
                    openlist.remove(child)

                if child in closedlist and tent_g_score < child.g_score:
                    closedlist.remove(child)

                if not openlist.exists(child):
                    child.parent = node
                    child.g_score = tent_g_score
                    child.f_score = child.g_score + self.hamming_distance(child, [0, 1, 2, 3, 4, 5, 6, 7, 8])

                    openlist.push(child.f_score, child)

                elif tent_g_score <= child.g_score:
                    continue

        print("Did not find goal state")
        return False

