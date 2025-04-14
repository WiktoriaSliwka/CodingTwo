#FILO
class Stack:
    def __init__(self):
        self.stack = [] #empty list self.storage
    def add (self,data):
        self.stack.append(data)
    def get(self):
        if not self.is_empty(): #is_empty is unnecessary but checks list 
            return self.stack.pop()
        else:
            return None
        
    def is_empty(self):
        return len(self.stack)==0

s = Stack()
s.add(1)
s.add(2)
s.add(3)

#FIFO
class Queue:
    def __init__(self):
        self.storage=[]
    def add (self,data):
        self.storage.append(data)
    def get(self):
        return self.storage.pop(0)
#using pop(0) may be slower for larger lists die to index shifting
#simulation of how its used 

q = Queue()
q.add(4)
q.add(5)
q.add(6)