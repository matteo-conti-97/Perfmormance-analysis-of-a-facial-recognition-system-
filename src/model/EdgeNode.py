from ProcessorSharingQueue import ProcessorSharingQueue
from Node import Node
from Server import Server

class EdgeNode(Node):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.queue = ProcessorSharingQueue()
        self.server = Server()

    def get_queue(self):
        return self.queue

    def is_full(self):
        return self.server.is_busy()