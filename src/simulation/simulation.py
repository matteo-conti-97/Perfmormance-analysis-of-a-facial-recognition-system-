from src.simulation.network import Network
from rngs import plantSeeds, selectStream, Exponential

__CLOUD_SERVICE__ = 1
__EDGE_SERVICE__ = 2
__EDGE_SAVE__ = 3

class Simulation:
    def __init__(self, config):
        self.seed=config['seed']
        self.duration=config['duration']
        self.arrival_rate=config['arrival_rate']
        self.cloud_mean_service_time=config['cloud_mean_service_time']
        self.edge_mean_service_time=config['edge_mean_service_time']
        self.edge_mean_save_time=config['edge_mean_save_time']
        self.c_scan_probability=config['c_scan_probability']
        self.response_time_qos=config['response_time_qos']
        self.nodes=config['nodes']
        self.min_cloud_nodes=config['min_cloud_nodes']
        self.max_cloud_nodes=config['max_cloud_nodes']

        plantSeeds(self.seed)

        self.network = Network(self.nodes, self.min_cloud_nodes, self.max_cloud_nodes)
        self.arrival_temp=0.0


    def get_arrival(self):
      selectStream(0)
      self.arrival_temp += Exponential(1/self.arrival_rate)
      return self.arrival_temp



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