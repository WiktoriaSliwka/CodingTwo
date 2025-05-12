class PriorityQueue:
    def __init__(self, data):
        self.queue = []
        self.counter = 0
        for item in data:
            self.add(item)

    def add(self, data):
        name, priority = data
        self.queue.append((priority, self.counter, name))
        self.counter += 1

    def get(self):
        if not self.queue:
            return None
        # Sort by priority, then insertion order (stable)
        self.queue.sort()
        return self.queue.pop(0)[2]

    def peek(self):
        if not self.queue:
            return None
        self.queue.sort()
        return self.queue[0][2]


# queue_data = [
# 	("Robert", 1),
# 	("Jane", 4),
# 	("Alex", 2),
# 	("Robert", 1)
# ]
# queue = PriorityQueue(queue_data)

# print(queue.get())
# queue.add(("", 2))
# print(queue.get())