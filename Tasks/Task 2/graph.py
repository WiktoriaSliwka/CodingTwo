import math

class Graph:
	def __init__(self, vertices, edges):
		self.vertices = set(vertices)
		self.edges = edges

		# Adjacency list
		self.adjacency_list = {}
		for vertex in vertices:
			self.adjacency_list[vertex] = []

			for edge in edges.keys():
				if vertex in edge:
					for v in edge:
						if v != vertex:
							self.adjacency_list[vertex].append(v)
							break

		# Incidence matrix
		self.incidence_matrix = {}
		for vertex in vertices:
			self.incidence_matrix[vertex] = {}

			for edge in edges.keys():
				if vertex in edge:
					self.incidence_matrix[vertex][edge] = 1
				else:
					self.incidence_matrix[vertex][edge] = 0

		# Adjacency matrix
		self.adjacency_matrix = {}
		for vertex in vertices:
			self.adjacency_matrix[vertex] = {}

			for vertex2 in vertices:
				self.adjacency_matrix[vertex][vertex2] = 0

				for edge in edges.keys():
					if (vertex != vertex2) and (vertex in edge) and (vertex2 in edge):
						self.adjacency_matrix[vertex][vertex2] = 1

	def walk(self, source, target):
			# Initialize distances with infinity for all nodes except source
			distances = {vertex: math.inf for vertex in self.vertices}
			distances[source] = 0
			
			# Priority queue to select the next node to visit
			# We'll use a simple list and sort it (for simplicity)
			unvisited = list(self.vertices)
			
			# To reconstruct paths
			previous = {vertex: None for vertex in self.vertices}
			
			while unvisited:
				# Find the unvisited node with the smallest distance
				current = min(unvisited, key=lambda vertex: distances[vertex])
				
				# Remove it from unvisited set
				unvisited.remove(current)
				
				# If we've reached the target, we can stop
				if current == target:
					break
					
				# Update distances for all neighbors
				for neighbor in self.adjacency_list[current]:
					# Find the edge between current and neighbor
					edge = None
					if (current, neighbor) in self.edges:
						edge = (current, neighbor)
					elif (neighbor, current) in self.edges:
						edge = (neighbor, current)
					
					if edge:
						distance = distances[current] + self.edges[edge]
						if distance < distances[neighbor]:
							distances[neighbor] = distance
							previous[neighbor] = current
			
			# Reconstruct the path from source to target
			path = []
			current = target
			
			# Handle case where target is unreachable
			if previous[current] is None and current != source:
				return path
				
			while current is not None:
				path.insert(0, current)
				current = previous[current]
			
			return path