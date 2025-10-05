from Queue import Queue

class FIFOQueue(Queue):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None