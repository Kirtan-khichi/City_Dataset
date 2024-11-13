import random
import copy 

class Graph(object):

	def __init__(self):
		self._nodes = []
		# self._dropout = 0
		self._edges = []
		self._adjLst = {}


	def add_node(self, node):
		self._nodes.append(node)

	def add_nodes(self, df):
		# df should be a dataframe , list or array

		for name in df:
			self._nodes.append(name)


	def add_edge(self, node1, node2, cost = None, heuristic = None, direction = True):
		assert direction in [True, False], 'Direction must be boolean value.'
		if direction:
			element = (node1, node2, cost, heuristic)

			self._edges.append(element)

		else:

			element1 = (node1, node2, cost, heuristic)
			element2 = (node2, node1, cost, heuristic)

			self._edges.append(element1)
			self._edges.append(element2)



	def edges(self, data = True):
		# Return Edge
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
		maximum_dropout = 1 - ((len(set(self._nodes)) - 1) / len(self._edges))
		assert dropout <= maximum_dropout, f'{dropout} dropout can"t be more than maximum_dropout {maximum_dropout}'

		num_edges_to_drop = int(dropout * len(self._edges))

		# copy_edges = copy.deepcopy(self._edges)

		for i in range(num_edges_to_drop):
			# print(self._edges)
			randomEdge = random.choice(self._edges)
			# print(randomEdge)
			element1 = (randomEdge[0], randomEdge[1], randomEdge[2], randomEdge[3])
			element2 = (randomEdge[1], randomEdge[0], randomEdge[2], randomEdge[3])
			if self.nodeDegree(randomEdge[0]) > 2 and self.nodeDegree(randomEdge[1]) > 2:
				if element1 in self._edges and element2 in self._edges:
					self._edges.remove(element1)
					self._edges.remove(element2)
		return self._edges

if __name__ == '__main__':
	obj = Graph()