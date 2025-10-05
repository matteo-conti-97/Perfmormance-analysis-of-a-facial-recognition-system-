from Queue import Queue

class ProcessorSharingQueue(Queue):
    def __init__(self):
        super().__init__()
        self.service_quantum = 1.0  # Default service quantum

    def push(self, item):
        self.items.append(item)
        self._update_service_quantum()

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            self._update_service_quantum()

    def _update_service_quantum(self):
        num_items = self.size()
        if num_items == 0:
            self.service_quantum = 1.0
        else:
            self.service_quantum = 1.0 / num_items

    def get_service_quantum(self):
        return self.service_quantum