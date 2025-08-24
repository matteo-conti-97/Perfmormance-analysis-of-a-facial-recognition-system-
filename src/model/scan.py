class Scan:
    def __init__(self, scan_type):
        self.scan_type = scan_type

    def get_type(self):
        return self.scan_type

    def set_type(self, scan_type):
        self.scan_type = scan_type