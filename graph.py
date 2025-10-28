from node import Node
from node_types import NodeList, NodeConnections

class Graph():
    def __init__(self, nodeList: NodeList) -> None:
        self.__nodeList = nodeList

    def getNodeList(self) -> NodeList:
        return self.__nodeList

    def __loopThroughConnections(self, nodeConnections: NodeConnections) -> None:
        for i in range(len(nodeConnections)):
            print(nodeConnections[i].getNodeName())

    def showConnections(self) -> None:
        for k in self.__nodeList.keys():
            self.__loopThroughConnections(self.__nodeList[k])

    def addNodeToList(self, nodeToAdd: Node) -> None:
        self.__nodeList[nodeToAdd] = nodeToAdd.getConnections()

    def removeNodeFromList(self, originNode: Node, nodeToRemove: Node) -> Node:
        listOfConnections = self.__nodeList[originNode]

        for i in range(len(listOfConnections) - 1):
            if(listOfConnections[i] != nodeToRemove):
                continue

        return nodeToRemove