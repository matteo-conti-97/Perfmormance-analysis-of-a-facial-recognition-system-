from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, node_id):
        self.node_id = node_id

    def get_node_id(self):
        return self.node_id

    @abstractmethod
    def is_full(self):
        pass

    @abstractmethod
    def get_server(self):
        pass

    @abstractmethod
    def get_queue(self):
        pass
