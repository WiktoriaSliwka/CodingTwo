from PriorityQueue import PriorityQueue

queue_data = [
	("Bakerloo", 2),
	("Central", 1),
	("Circle", 1),
	("District", 3),
	("Hammersmith & City", 3),
	("Jubilee", 1),
	("Waterloo & City", 5),
	("Metropolitan", 3),
	("Northern", 2),
	("Piccadilly", 1),
	("Victoria", 4)
]
queue = PriorityQueue(queue_data)

print("Getting the first item in the queue ... " + str(queue.get()))
print("Getting the second item in the queue ... " + str(queue.get()))
queue.add(("Windrush", 1))
print("Getting the third item in the queue ... " + str(queue.get() ))
print("Getting the fourth item in the queue ... " + str(queue.get()))
print("Getting the fifth item in the queue ... " + str(queue.get()))
queue.add(("Lioness", 3))
print("Getting the sixth item in the queue ... " + str(queue.get() ))
print("Getting the seventh item in the queue ... " + str(queue.get() ))
print("Getting the eigth item in the queue ... " + str(queue.get() ))
print("Getting the ninth item in the queue ... " + str(queue.get() ))
print("Getting the tenth item in the queue ... " + str(queue.get() ))
print("Getting the eleventh item in the queue ... " + str(queue.get() ))
print("Getting the twelfth item in the queue ... " + str(queue.get()))
print("Getting the thirteenth item in the queue ... " + str(queue.get()))

queue = PriorityQueue(queue_data)
print(queue.get())