from typing import Self

class Node():
    def __init__(self, name: str, connections: list[Self]) -> None:
        self.__name = name
        self.__connections = connections

    def getNodeName(self) -> str:
        return self.__name
    
    def getConnections(self):
        return self.__connections

    def addConnection(self, newConnection) -> None:
        self.__connections.append(newConnection)