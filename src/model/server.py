class Server:
    def __init__(self, service_time, utilization=0.0):
        self.service_time = service_time
        self.utilization = utilization

    def get_service_time(self):
        return self.service_time

    def set_service_time(self, service_time):
        self.service_time = service_time

    def get_utilization(self):
        return self.utilization

    def set_utilization(self, utilization):
        self.utilization = utilization