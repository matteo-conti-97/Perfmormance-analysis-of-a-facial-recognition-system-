import sys

from src.simulation.network import Network
from rngs import plantSeeds, selectStream, Exponential

__CLOUD_SERVICE__ = 1
__EDGE_SERVICE__ = 2
__EDGE_SAVE__ = 3


class Simulation:
    def __init__(self, config):
        #Read configuration parameters
        self.seed = config['seed']
        self.duration = config['duration']
        self.arrival_rate = config['arrival_rate']
        self.cloud_mean_service_time = config['cloud_mean_service_time']
        self.edge_mean_service_time = config['edge_mean_service_time']
        self.edge_mean_save_time = config['edge_mean_save_time']
        self.c_scan_probability = config['c_scan_probability']
        self.response_time_qos = config['response_time_qos']
        self.nodes = config['nodes']
        self.min_cloud_servers = config['min_cloud_servers']
        self.max_cloud_servers = config['max_cloud_servers']

        #Build network
        self.network = Network(self.nodes, self.min_cloud_servers, self.max_cloud_servers)

        #Initialize simulation variables
        plantSeeds(self.seed)
        self.clock = 0.0
        self.departed_jobs = 0
        self.number_of_jobs = 0
        self.infinity = 100  * self.duration
        self.arrival_time = [self.get_arrival() for _ in range(self.nodes)] #DEVO CAPIRE COME INIZIALIZZARE QUESTI
        self.edge_completion_time = [0.0 for _ in range(self.nodes)]
        self.cloud_completion_time = [[0.0 for _ in range(0, self.max_cloud_servers)] for _ in range(self.nodes)]



    def get_arrival(self):
      selectStream(0)
      self.arrival_time += Exponential(1/self.arrival_rate)
      return self.arrival_time


    def get_service(self, service_type):
      if service_type == __CLOUD_SERVICE__:
        selectStream(1)
        return Exponential(self.cloud_mean_service_time)
      elif service_type == __EDGE_SERVICE__:
        selectStream(2)
        return Exponential(self.edge_mean_service_time)
      elif service_type == __EDGE_SAVE__:
        selectStream(3)
        return Exponential(self.edge_mean_save_time)
      return None

    def run(self):
        # take max of arrival times across all nodes
        self.clock = max(self.get_arrival())

