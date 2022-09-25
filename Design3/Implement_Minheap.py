
class Minheap:
    def __init__(self):
        self.heap=[] # craeting heap array
        
    def getMin(self):
        return self.heap[0] # returning first element from the heap array
        
    def bubbleUp(self,index):
        parentIndex = (index-1)//2 # finding parent Index
        if parentIndex<0: # if parent index is not present
            return
                
        if self.heap[parentIndex]<self.heap[index]: # if parent index is lesser than present index
            return
                
        self.heap[parentIndex],self.heap[index] = self.heap[index],self.heap[parentIndex] # swapping parent and present index
        self.bubbleUp(parentIndex) # calling recursively
                
    def bubbleDown(self,index):
        lchild = 2*index+1 # finding leftchild
        rchild = 2*index+2 # finding rightchild
        temp = index
        if lchild<len(self.heap) and self.heap[index]>self.heap[lchild]: # if left child is lesser than lenght of heap and heap index is greater than leftchild of heap
            
            temp=lchild                                                    
        if rchild<len(self.heap) and self.heap[index]>self.heap[rchild]: # if left child is lesser than lenght of heap and heap index is greater than leftchild of heap
            temp=rchild
        if temp == index:
            return
                    
        self.heap[temp],self.heap[index] = self.heap[index],self.heap[temp] # swapping heap temp and heap index
        self.bubbleDown(temp) # calling recursively 
                
    def insert(self,key):
        self.heap.append(key)
        self.bubbleUp(len(self.heap)-1) # calling bubbleUp

    def extractMin(self):
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0] #swapping 0th index and first index
        temp = self.heap.pop()  # storing the popped value in temp
        self.bubbleDown(0) # calling bubbledown
        return temp
            
    def size(self):
        return len(self.heap) # return size of heap
            
h=Minheap()
h.insert(5);
h.insert(13);
h.insert(6);
h.insert(9);
h.insert(0);
h.insert(1);
print(h.heap)
print(h.getMin())
for i in range(len(h.heap)):
    print(h.extractMin())
