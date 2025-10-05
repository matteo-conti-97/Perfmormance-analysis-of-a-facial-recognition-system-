class Server:
    def __init__(self, busy=False):
        self.busy = busy

    def is_busy(self):
        return self.busy

    def set_busy(self, busy):
        self.busy = busy