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