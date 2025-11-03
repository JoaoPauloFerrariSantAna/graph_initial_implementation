from typing import Final
from node import Node
from node_types import NodeList, NodeConnections, NodePath

TestPath = tuple[Node, Node]
NON_TRIVIAL_LENGTH: Final = 2

class Graph():
	"""Represents a undirected graph with Nodes.
	
	Keyword arguments:

	:param nodeList: the dictionary to represent the graph as a whole.
	"""
	def __init__(self, nodeList: NodeList) -> None:
		self.__nodeList = nodeList

	def getNodeList(self) -> NodeList:
		"""Will return the dict represeting the all conections.
		"""
		return self.__nodeList

	def __loopThroughConnections(self, nodeConnections: NodeConnections) -> None:
		for i in range(len(nodeConnections)):
			print(nodeConnections[i].getNodeName())
	
	def __isTrivial(self, pathLength) -> bool:
		return pathLength < NON_TRIVIAL_LENGTH

	def showConnections(self) -> None:
		"""Will print the connections from all nodes.
		"""
		for k in self.__nodeList.keys():
			print(f"--- {k.getNodeName()}")
			self.__loopThroughConnections(self.__nodeList[k])

	def isRouteValid(self, path: NodePath) -> bool:
		if(self.__isTrivial(len(path))):
			return True

		allConnections = self.__nodeList

		for node in range(len(path) - 2):
			testPath: TestPath = (path[node], path[node + 1])
			originConnections = testPath[0].getConnections()

			if(testPath[0] in allConnections):
				return True

			if(testPath[1] in originConnections):
				return True

	def addNodeToList(self, nodeToAdd: Node) -> None:
		"""Will add a node to the global node list.

		Keyword arguments:

		:param nodeToAdd: represents the node to add: it may be added without any previous connections made
		"""
		self.__nodeList[nodeToAdd] = nodeToAdd.getConnections()

	def removeNodeFromList(self, originNode: Node, nodeToRemove: Node) -> None:
		"""Will remove a node from the global list.

		Keyword arguments:

		:param originalNode: the node where that connection originates.
		:param nodeToRemove: the node to remove from originalNode.
		:return: the node that was deleted or None if the node was already removed.
		"""
		listOfConnections = self.__nodeList[originNode]

		if(nodeToRemove not in listOfConnections):
			raise Exception

		listOfConnections.remove(nodeToRemove)
