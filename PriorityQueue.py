class PriorityQueue:
	def __init__(self, data): #takes data as ain put and assigns it to self.storage 
		self.storage = data

	def get(self):
		if not self.storage:
			raise IndexError("Priority Queue is empty")
		# Find the element with the highest priority (lowest numerical value)
		highest_priority_index =0
		for i in range(1, len(self.storage)):
			if self.storage[i][1]< self.storage[highest_priority_index][1]:
				highest_priority_index= i 
			return self.storage.pop(highest_priority_index)
		#remove and return the element with the highest priority from the queue.
		

	def add(self, data):
		self.storage.append(data)

	def peek(self):
		if not self.storage:
			raise IndexError("Priority Queue is empty")
		highest_priority_index =0
		for i in range(1, len(self.storage)):
			if self.storage[i][1]< self.storage[highest_priority_index][1]:
				highest_priority_index= i 
			return self.storage.pop(highest_priority_index)
		#method is intended to return the element with the highest priority without removing it.
		
	def __str__(self):
        # Return a string representation of the entire queue
         return "\n".join(str(item) for item in self.storage)


queue_data = [
	("Robert", 1),
	("Jane", 2),
	("Alex", 3),
]
queue = PriorityQueue(queue_data)
# queue.add(("Jimmy Neutron", 2))
# print(queue.get())
# print(queue.get())
# # queue.print_queue
# print(queue.get())
# print(queue.get())
print(queue)