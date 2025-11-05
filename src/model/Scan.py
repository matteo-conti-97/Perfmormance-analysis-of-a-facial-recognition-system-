class Scan:
    def __init__(self, scan_id, scan_type, service_time, arrival_time):
        self.scan_id = scan_id
        self.scan_type = scan_type
        self.arrival_time = arrival_time
        self.edge_start_time = None
        self.edge_end_time = None
        self.edge_resume_time = None
        self.cloud_arrival_time = None
        self.cloud_start_time = None
        self.cloud_end_time = None
        self.edge_return_time = None
        self.edge_return_service_start_time = None
        self.edge_return_service_end_time = None


    def get_scan_id(self):
        return self.scan_id

    def get_scan_type(self):
        return self.scan_type

    def set_scan_type(self, scan_type):
        self.scan_type = scan_type

    def get_service_time(self):
        return self.service_time

    def set_service_time(self, service_time):
        self.service_time = service_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_edge_start_time(self):
        return self.edge_start_time

    def set_edge_start_time(self, edge_start_time):
        self.edge_start_time = edge_start_time

    def get_edge_end_time(self):
        return self.edge_end_time

    def set_edge_end_time(self, edge_end_time):
        self.edge_end_time = edge_end_time

    def get_edge_resume_time(self):
        return self.edge_resume_time

    def set_edge_resume_time(self, edge_resume_time):
        self.edge_resume_time = edge_resume_time

    def get_cloud_arrival_time(self):
        return self.cloud_arrival_time

    def set_cloud_arrival_time(self, cloud_arrival_time):
        self.cloud_arrival_time = cloud_arrival_time

    def get_cloud_start_time(self):
        return self.cloud_start_time

    def set_cloud_start_time(self, cloud_start_time):
        self.cloud_start_time = cloud_start_time

    def get_cloud_end_time(self):
        return self.cloud_end_time

    def set_cloud_end_time(self, cloud_end_time):
        self.cloud_end_time = cloud_end_time

    def get_edge_return_time(self):
        return self.edge_return_time

    def set_edge_return_time(self, edge_return_time):
        self.edge_return_time = edge_return_time

    def get_edge_return_service_start_time(self):
        return self.edge_return_service_start_time

    def set_edge_return_service_start_time(self, edge_return_service_start_time):
        self.edge_return_service_start_time = edge_return_service_start_time

    def get_edge_return_service_end_time(self):
        return self.edge_return_service_end_time

    def set_edge_return_service_end_time(self, edge_return_service_end_time):
        self.edge_return_service_end_time = edge_return_service_end_time


