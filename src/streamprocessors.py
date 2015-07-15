import heapq

class MinHeap(object):
    def __init__(self):
        self.heap = []
    def push(self, value):
        heapq.heappush(self.heap, value)
        return self.heap[0]
    def pop(self):
        return heapq.heappop(self.heap)
    def peek(self):
        return self.heap[0]
    def __len__(self):
        return len(self.heap)
    def __str__(self):
        return str(self.heap)

#Can extend MinHeap to make the code better.
class MaxHeap(object):
    def __init__(self):
        self.heap = []
    def push(self, value):
        heapq.heappush(self.heap, (-value))
        return -self.heap[0]
    def pop(self):
        return -heapq.heappop(self.heap)
    def peek(self):
        return -self.heap[0]
    def __len__(self):
        return len(self.heap)
    def __str__(self):
        return str(self.heap)


class Streaming_median_calculator:
    def __init__(self):
        self.minheap = MinHeap()
        self.maxheap = MaxHeap()
        self.median = 0

#Adds a value, and returns the resulting median
    def push(self, value):
        diff = len(self.maxheap)-len(self.minheap)
        if diff>0:
            if value < self.median:
                self.minheap.push(self.maxheap.pop())
                self.maxheap.push(value)
            else:
                self.minheap.push(value)
            self.median = ((self.minheap.peek()+self.maxheap.peek())/2)
        elif diff==0:
            if value < self.median:
                self.maxheap.push(value)
                self.median = self.maxheap.peek()
            else:
                self.minheap.push(value)
                self.median = self.minheap.peek()
        else:
            if value > self.median:
                self.maxheap.push(self.minheap.pop())
                self.minheap.push(value)
            else:
                self.maxheap.push(value)
            self.median = ((self.minheap.peek()+self.maxheap.peek())/2)
        return self.median
