import random
import copy 

class Graph(object):
	"""
	This class is uesed for creating objects of Graph. We created this class as per our modification.
	We wanted to give few facilitates like adding nodes or node, adding edges also. The main work of 
	this class is to convert a complete graph into a connected graph by asking user what percentage of 
	edges needs to be removed in the graph.  
	"""

	def __init__(self):
		self._nodes = []      # Initialize a list to store nodes
		self._edges = []	  # Initialize a list to store edges
		self._adjLst = {}	  # Initialize a dictionary to store adjacency list


	def add_node(self, node):
		"""
        Add a node to the graph.

		Parameter node: node that need to be added
		Precondition: node is not empty
        """
		self._nodes.append(node)

	def add_nodes(self, df):
		"""
        Add multiple nodes to the graph.

		Parameter df: nodes that need to be added
		Precondition: df should be a dataframe, list or array
        """
		
		for name in df:
			self._nodes.append(name)


	def add_edge(self, node1, node2, cost = None, direction = True):
		"""
        Add an edge to the graph between 'node1' and 'node2' with an optional 'cost'.
        'direction' specifies if the edge is directed or not.

		Parameter node1: first node for adding edge
		Precondition: node1 is not empty

		Parameter node2: second node for adding edge
		Precondition: node2 is not empty

		Parameter cost: weight of edge between node1 and node2
		Precondtion: cost is numerical value or None

		Parameter direction: direction of the edge between node1 and node2
		Precondition: direction is boolen
        """
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
		"""
        Get the list of edges in the graph. 'data' specifies if edge data should be included.

		Parameter data: true for inculding weight of edge otherwise false
		Precodition: data is boolen
        """

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
		"""
        Generating and returning the adjacency list of the graph.
        """
		for key in set(self._nodes):
			lst = []

			for element in self.edges(data = True):
				if key == element[0]:
					temp = (element[1], element[2])
					lst.append(temp)

			self._adjLst[key] = lst

		return self._adjLst


	def nodeDegree(self, node):
		"""
        Get the degree of a given node in the graph.

		Parameter node: node for which we want degree
		Precondition: node should be present in graph
        """
		assert node in self._nodes, f'{node} node does not exists.'

		self.adjList()
		return len(self._adjLst[node])

	def randomGraphCreater(self, dropout):
		"""
        Create a random graph by dropping edges with a given 'dropout' rate.

		Parameter droupout: rate at which edges needs to be removed
		Precondition: droupout should be numerical value
        """
		maximum_dropout = 1 - ((len(set(self._nodes)) - 1) / len(self._edges))
		assert dropout <= maximum_dropout, f'{dropout} dropout can"t be more than maximum_dropout {maximum_dropout}'

		num_edges_to_drop = int(dropout * len(self._edges))

		for i in range(num_edges_to_drop):

			randomEdge = random.choice(self._edges)
			element1 = (randomEdge[0], randomEdge[1], randomEdge[2])
			element2 = (randomEdge[1], randomEdge[0], randomEdge[2])
			
			if self.nodeDegree(randomEdge[0]) > 2 and self.nodeDegree(randomEdge[1]) > 2:
				if element1 in self._edges and element2 in self._edges:
					self._edges.remove(element1)
					self._edges.remove(element2)
		return self._edges

if __name__ == '__main__':
	obj = Graph()