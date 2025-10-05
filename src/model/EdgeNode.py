from ProcessorSharingQueue import ProcessorSharingQueue
from Node import Node
from Server import Server

class EdgeNode(Node):
    def __init__(self, node_id, capacity):
        super().__init__(node_id, capacity)
        self.queue = ProcessorSharingQueue()
        self.Server = Server(capacity)

    def get_queue(self):
        return self.queue