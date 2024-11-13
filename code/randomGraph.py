import random
import copy 

class Graph(object):

	def __init__(self):
		self._nodes = []
		self._dropout = 0
		self._edges = []
		self._adjLst = {}


	def add_node(self, node):
		self._nodes.append(node)

	def add_nodes(self, df):
		# df should be a dataframe , list or array

		for name in df:
			self._nodes.append(name)


	def add_edge(self, node1, node2, cost = None, direction = True):
		assert direction in [True, False], 'Direction must be boolean value.'
		if direction:
			element = (node1, node2, cost)

			self._edges.append(element)

		else:

			element1 = (node1, node2, cost)
			element2 = (node2, node1, cost)

			self._edges.append(element1)
			self._edges.append(element2)



	def edges(self, data = True):

		if data == True:
			return self._edges

		else:
			lst = []
			for element in self._edges:
				for node1, node2 in element:
					temp = (node1, node2)

				lst.append(temp)

			return lst


	def adjList(self):
		# adj_lst = {}
		
		for key in set(self._nodes):
			lst = []

			for element in self.edges(data = True):
				if key == element[0]:
					temp = (element[1], element[2])
					lst.append(temp)

			self._adjLst[key] = lst

		return self._adjLst


	def nodeDegree(self, node):

		assert node in self._nodes, f'{node} node does not exists.'

		self.adjList()
		return len(self._adjLst[node])

	def randomGraphCreater(self, dropout):

		print(len(set(self._nodes)), len(self._edges))

		maximum_dropout = 1 - ((len(set(self._nodes)) - 1) / len(self._edges))
		# minimum_dropout = 1 - maximum_dropout
		# print(maximum_dropout, minimum_dropout)

		assert dropout <= maximum_dropout, f'{dropout} dropout can"t be more than maximum_dropout {maximum_dropout}'
		# assert dropout >= minimum_dropout, f"{dropout} dropout can't be less than minimum_dropout {minimum_dropout}"

		num_edges_to_drop = int(dropout * len(self._edges))
		print(num_edges_to_drop, maximum_dropout)
		copy_edges = copy.deepcopy(self._edges)
		print('before', len(copy_edges))

		for i in range(num_edges_to_drop):
			randomEdge = random.choice(self._edges)
			print(randomEdge, i)


			if self.nodeDegree(randomEdge[0]) != 0:
				if randomEdge in self._edges :

					# element1 = (randomEdge[0], randomEdge[1], randomEdge[2])
					# element2 = (randomEdge[1], randomEdge[0], randomEdge[2])
					print(randomEdge)
					self._edges.remove(randomEdge)
					# copy_edges.remove(element2)

		print('After', len(self._edges))

		return self._edges


		# print(randomEdge)

	# def is_connected(self, graph):
	#     visited = set()
	#     stack = [list(graph.keys())[0]]  # Start DFS from the first node
	    
	#     while stack:
	#         node = stack.pop()
	#         if node not in visited:
	#             visited.add(node)
	#             stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

	#     return len(visited) == len(graph)

	# def random_connected_graph(self, dropout_prob, complete_graph):
	#     # complete_graph = {i: set(range(i)) | set(range(i + 1, n)) for i in range(n)}
	#     n = len(set(self._nodes))

	#     random_graph = {node: set(neighbors) for node, neighbors in complete_graph.items()}

	#     for node, neighbors in complete_graph.items():
	#         for neighbor in neighbors:
	#         	# print(random.random())
	#             if random.random() <= dropout_prob:
	#                 print(node, neighbors)
	#                 random_graph[node].remove(neighbor)
	#                 random_graph[neighbor[0]].remove(node)

	#     # Ensure the graph remains connected
	#     while not self.is_connected(random_graph):
	#         node1, node2 = random.sample(range(n), 2)
	#         print(node1, node2)
	#         if node2 not in random_graph[node1]:
	#             random_graph[node1].add(node2)
	#             random_graph[node2].add(node1)

	#     return random_graph

if __name__ == '__main__':
	obj = Graph()

	obj.add_node('a')
	obj.add_node('b')
	obj.add_node('c')
	obj.add_node('d')
	obj.add_node('e')
	# obj.add_edge(7, 8, 'a')
	# obj.add_edge(8, 7, 'b')
	# obj.add_edge(5, 6, 'k')
	# obj.add_edge(6, 5, 'l')
	# obj.add_edge(5, 7, 'q')
	# obj.add_edge(5, 8, 'w')
	# obj.add_edge(6, 7, 'w')
	# obj.add_edge(6, 8, 'e')
	# obj.add_edge(7, 5, 'p')
	# obj.add_edge(7, 6, 'p')
	# obj.add_edge(8, 5, 'f')
	# obj.add_edge(8, 6, 'q')
	obj.add_edge('a', 'b', 1)
	obj.add_edge('a', 'c', 1)
	obj.add_edge('a', 'd', 1)
	obj.add_edge('b', 'd', 1)
	obj.add_edge('c', 'b', 1)
	obj.add_edge('d', 'c', 1)
	obj.add_edge('a', 'e', 1)
	obj.add_edge('c', 'e', 1)
	obj.add_edge('e', 'b', 1)
	obj.add_edge('d', 'c', 1)



	# print(obj.adjList())
	# obj.random_connected_graph(0.5, obj.adjList())



	# print(obj.nodeDegree(8))
	print(obj.randomGraphCreater(0.2))


