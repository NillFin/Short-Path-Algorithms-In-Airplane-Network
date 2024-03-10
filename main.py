import networkx as nx 
import matplotlib.pyplot as plt 
from queue import PriorityQueue

class Node:
	def __init__(self, name: str, cityNumber: int, isCataclysm: bool):
		self.name = name
		self.isCataclysm = isCataclysm
		self.cityNumber = cityNumber

class Graph:
	def __init__(self):
		self.graph = dict()
		self.visual = []

	def addNode(self, name: str, cityNumber: int, isCataclysm=False):
		for node in self.graph.keys():
			if node.name == name:
				print(f">>> Error: {name} is already in the graph\n")
				return 
		else:
			newNode = Node(name, cityNumber, isCataclysm)
			self.graph[newNode] = dict()

	def addEdge(self, name1: str, name2: str, dist: int):
		if dist <= 0:
			print(">>> Error: Distance is a positive, not negative, number")
			return
		isName1, isName2 = False, False
		for node in self.graph.keys():
			if node.name == name1:
				isName1 = True
				nodeName1 = node
			elif node.name == name2:
				isName2 = True
				nodeName2 = node
		if (isName1 and isName2 and (nodeName2 not in self.graph[nodeName1].keys())
	  	and (nodeName1 not in self.graph[nodeName2].keys())):
			self.graph[nodeName1][nodeName2] = dist
			self.graph[nodeName2][nodeName1] = dist
			self.visual.append([name1, name2])
		else:
			print(">>> Error: I didn't find {name1} and {name2} in the graph")
	
	def removeNode(self, name: str):
		Node = None
		for node in self.graph.keys():
			if node.name == name:
				Node = node
		if Node is None:
			print(">>> Error: I can't delete a non-existent city")
			return
		
		del self.graph[Node]
		for ver in self.graph.keys():
			if Node in self.graph[ver].keys():
				del self.graph[ver][Node]
		temp = []
		for lst in self.visual:
			if name not in lst:
				temp.append(lst)
		self.visual.clear()
		self.visual = temp
		del temp

	def getEdgeDist(self, name1: str, name2: str):
		NodeName1, NodeName2 = None, None
		for node in self.graph.keys():
			if node.name == name1:
				NodeName1 = node
			if node.name == name2:
				NodeName2 = node
		if NodeName1 == None or NodeName2 == None:
			print(">>> Error: I can't find distance between non-existent cities")
			return
		if name1 == name2:
			return 0
		if NodeName2 in self.graph[NodeName1]:
			return self.graph[NodeName1][NodeName2]
		print(">>> Error: There is no edge between these two cities")
		return float('inf')
	
	def changeInfoAboutWeather(self, name: str):
		for node in self.graph.keys():
			if node.name == name:
				node.isCataclysm = not node.isCataclysm
				break

	def displayGraph(self):
		for key in self.graph.keys():
			print(f"-> {key.name}: {{", end="")
			for subkey in self.graph[key].keys():
				print(f"'{subkey.name}' : {self.graph[key][subkey]}, ", end="")
			print("}")
	
	def displayBadWeatherCities(self):
		print("Cities with Bad Weather:")
		for key in self.graph.keys():
			if key.isCataclysm:
				print(key.name)
		print()

	def graphVisualization(self):
		G = nx.Graph() 
		G.add_edges_from(self.visual) 
		nx.draw_networkx(G) 
		plt.show()

def greedy(graph: Graph, start: str, target: str):
	startNode, targetNode = None, None
	for node in graph.keys():
		if node.name == start:
			startNode = node
		if node.name == target:
			targetNode = node
	h = None
	openedList = [startNode]
	while True:
		if not openedList:
			break # No solution found
		#selectNode = 
		
if __name__ == "__main__":
	graph = Graph()

	graph.addNode("Paris", 1) 			# 1
	graph.addNode("London", 2)			# 2
	graph.addNode("Milano", 3, True)		# 3
	graph.addNode("Berlin", 4)			# 4
	graph.addNode("Hamburg", 5)			# 5
	graph.addNode("Warsaw", 6)			# 6
	graph.addNode("Saint Petersburg", 7)		# 7
	graph.addNode("Moscow", 8)			# 8
	graph.addNode("Dubai", 9, True)			# 9
	graph.addNode("Istanbul", 10)			# 10
	graph.addNode("Toronto", 11)			# 11
	graph.addNode("Hanoi", True, 12)		# 12
	graph.addNode("New York", 13)			# 13

	graph.addEdge("Paris", "London", 5)
	graph.addEdge("Paris", "Hamburg", 16)
	graph.addEdge("Paris", "Warsaw", 45)
	graph.addEdge("London", "Milano", 12)
	graph.addEdge("London", "Berlin", 44)
	graph.addEdge("London", "Warsaw", 43)
	graph.addEdge("Milano", "Hamburg", 22)
	graph.addEdge("Milano", "Warsaw", 38)
	graph.addEdge("Milano", "Hanoi", 8)
	graph.addEdge("Berlin", "Hamburg", 66)
	graph.addEdge("Berlin", "Warsaw", 69)
	graph.addEdge("Hamburg", "Istanbul", 8)
	graph.addEdge("Warsaw", "Hanoi", 18)
	graph.addEdge("Saint Petersburg", "Moscow", 16)
	graph.addEdge("Saint Petersburg", "Istanbul", 41)
	graph.addEdge("Saint Petersburg", "Hanoi", 58)
	graph.addEdge("Saint Petersburg", "New York", 64)
	graph.addEdge("Moscow", "Dubai", 23)
	graph.addEdge("Moscow", "New York", 37)
	graph.addEdge("Dubai", "Hanoi", 35)
	graph.addEdge("Dubai", "New York", 48)
	graph.addEdge("Istanbul", "Toronto", 9)
	graph.addEdge("Istanbul", "New York", 45)
	graph.addEdge("Hanoi", "New York", 68)

	graph.displayGraph()
	graph.displayBadWeatherCities()
	print(graph.getEdgeDist("Dubai", "Dubai"))
	print(graph.getEdgeDist("Dubai", "Moscow"))
	print(graph.getEdgeDist("Dubai", "fdfd"))
	print(graph.getEdgeDist("Paris", "Moscow"))
	graph.graphVisualization()
