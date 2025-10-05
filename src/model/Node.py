from abc import ABC

class Node(ABC):
    def __init__(self, node_id):
        self.node_id = node_id

    def get_node_id(self):
        return self.node_id

    def get_server(self):
        pass
    def get_queue(self):
        pass
