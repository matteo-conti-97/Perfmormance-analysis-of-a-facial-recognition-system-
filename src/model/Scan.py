class Scan:
    def __init__(self, scan_id, scan_type, service_demand):
        self.scan_id = scan_id
        self.scan_type = scan_type
        self.service_demand = service_demand
        self.service_time = 0.0

    def get_scan_id(self):
        return self.scan_id

    def get_scan_type(self):
        return self.scan_type

    def set_scan_type(self, scan_type):
        self.scan_type = scan_type

    def get_service_demand(self):
        return self.service_demand

    def get_service_time(self):
        return self.service_time

    def set_service_time(self, service_time):
        self.service_time = service_time
