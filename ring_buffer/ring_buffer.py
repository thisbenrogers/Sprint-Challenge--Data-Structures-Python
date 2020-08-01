class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.data = [None]*capacity


    def append(self, item):
        self.data[self.current] = item
        if self.current == self.capacity -1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        ring = []
        for i in self.data:
            if i is not None:
                ring.append(i)
        return ring