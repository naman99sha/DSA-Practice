#parentIdx = (idx-1)/2 // For array representation
#leftChildIdx = 2*idx + 1 // For array representation
#rightChildIdx = 2*idx + 2 // For array representation

# For Max Heap just turn the '<' to '>='

class MinHeap:
    def __init__(self,capacity):
        self.storage = [0] * capacity #Array for MinHeap
        self.capacity = capacity
        self.size = 0
        
    #helper methods
    def getParentIdx(self,idx):
        return (idx-1)//2
    def getLeftChildIdx(self,idx):
        return (2*idx) + 1
    def getRightChildIdx(self,idx):
        return (2*idx) + 2
    def hasParent(self,idx):
        return self.getParentIdx(idx) >= 0
    def hasLeftChild(self,idx):
        return self.getLeftChildIdx(idx) < self.size
    def hasRightChild(self,idx):
        return self.getRightChildIdx(idx) < self.size
    def isFull(self):
        return self.size >= self.capacity
    def swap(self,idx1,idx2):
        self.storage[idx1],self.storage[idx2] = self.storage[idx2],self.storage[idx1]
    
    #insertion and deletion
    def insert(self,data):
        if self.isFull:
            raise "Heap is Full"
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()
        
    def heapifyUp(self):
        idx = self.size - 1
        while(self.hasParent(idx) and self.getParentIdx(idx) > self.storage[idx]):
            self.swap(self.getParentIdx(idx),idx)
            idx = self.getParentIdx(idx)
    
    def removeMin(self):
        if self.size == 0:
            raise "Heap is empty"
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.heapifyDown()
        return data
    
    def heapifyDown(self):
        idx = 0
        while(self.hasLeftChild(idx)):
            smallerChild = self.getLeftChildIdx(idx)
            if self.hasRightChild(idx) and self.storage[self.getLeftChildIdx(idx)] > self.storage[self.getRightChildIdx[idx]]:
                smallerChild = self.getRightChildIdx(idx)
            if self.storage[idx] < self.storage[smallerChild]:
                break
            self.swap(idx,smallerChild)
            idx = smallerChild