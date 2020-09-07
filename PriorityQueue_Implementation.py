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

#
# from BoardNode import *
#
# pq = PriorityQueue()
# pq.push(1, BoardNode([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# pq.push(2, BoardNode([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# pq.push(0, BoardNode([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# print(pq.heap)
# pq.pop()
# print(pq.heap)
# pq.pop()
# print(pq.heap)
# pq.push(4, BoardNode([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(pq.heap)
