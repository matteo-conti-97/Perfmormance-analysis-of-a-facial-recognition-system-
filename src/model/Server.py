class Server:
    def __init__(self, capacity, busy=False):
        self.capacity = capacity
        self.busy = busy

    def is_busy(self):
        return self.busy

    def set_busy(self, busy):
        self.busy = busy

    def get_capacity(self):
        return self.capacity