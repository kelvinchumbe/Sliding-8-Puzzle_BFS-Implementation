import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, priority_val, item):
        heapq.heappush(self.heap, (priority_val, item))

    def pop(self):
        return heapq.heappop(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0

    def clear(self):
        while not (self.isEmpty()):
            self.heap.pop()

    def getHeap(self):
        return self.heap

    def exists(self, item):
        return item in (x[1] for x in self.heap)

    def remove(self, item):
        return self.heap.remove(item)
