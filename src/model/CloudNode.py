from FIFOQueue import FIFOQueue
from Node import Node
from Server import Server

class CloudNode(Node):
    def __init__(self, node_id, min_servers=1, max_servers=None):
        super().__init__(node_id)
        self.queue = FIFOQueue()
        self.min_servers = min_servers
        self.max_servers = max_servers if max_servers else min_servers
        self.server_list = [Server() for _ in range(min_servers)]


    def get_queue(self):
        return self.queue

    def is_full(self):
        for server in self.server_list:
            if not server.is_busy():
                return False
        return True