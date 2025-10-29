from node import Node
from node_types import NodeList, NodeConnections

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

    def showConnections(self) -> None:
        """Will print the connections from all nodes.
        """
        for k in self.__nodeList.keys():
            print(f"--- {k.getNodeName()}")
            self.__loopThroughConnections(self.__nodeList[k])

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