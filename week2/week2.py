#use deque to implement to add and get methods
#Implement a queue with a maximum length 
from collections import deque

# class Queue:
#     def __init__(self):
#         self.storage = deque()
#         self.maxlen = 5  # max length

#     def add(self, data):
#         if len(self.storage) == self.maxlen:  # Fix condition
#             self.storage.append(data)

#     def get(self):
#         if self.storage:  
#             return self.storage.popleft()
    
#     def reverse(self):
#         self.storage.reverse()
#         #self.queue = deque(reversed(self.queue), maxlen=self.queue.maxlen)
#     def rotate(self, n=1):
#         self.storage.rotate(n)

    #implement circular queue
class CircularQueue:
    def __init__(self, data):
        self.storage = deque(data) 
    def get(self):
        val = self.storage[0]
        self.storage.rotate(-1)
        return val
    def add(self, data):
        self.storage.append(data)
    

my_circular = CircularQueue(["a","b", "c", "d"])
print(my_circular.storage)    
print (my_circular.get())
print (my_circular.get())
print (my_circular.get())
print (my_circular.get())
    
# my_queue = Queue()
# my_queue.add(1)
# my_queue.add(2)
# my_queue.add(3)
# my_queue.add(4)
# my_queue.add(5)
# print(my_queue.get()) #maxlength 5
# my_queue.add(6)
# #my_queue.rotate(2)
# print(my_queue.get())
# print(my_queue.get())
# print(my_queue.get())
# print(my_queue.get())
# print(my_queue.get())
