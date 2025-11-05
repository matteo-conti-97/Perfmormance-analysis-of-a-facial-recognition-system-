from src.model.CloudNode import CloudNode
from src.model.EdgeNode import EdgeNode


class Network:
    def __init__(self, nodes, min_cloud_servers, max_cloud_servers):
        self.nodes = nodes
        self.edge_nodes = [EdgeNode(i) for i in range(nodes)]
        self.cloud_nodes = [CloudNode(i, min_cloud_servers, max_cloud_servers) for i in range(nodes)]


    def get_nodes_number(self):
        return self.nodes

    def get_edge_nodes(self):
        return self.edge_nodes

    def get_cloud_nodes(self):
        return self.cloud_nodes


