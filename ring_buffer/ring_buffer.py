class RingBuffer:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = []

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return (f"ListNode("
                f"\n\capacity={self.cap}"
                f"\n\data={self.data}\n)")

    class __Full:
        def append(self, item):
            self.data[self.current] = item
            self.current = (self.current + 1) % self.max
        
        def get(self):
            return self.data[self.current:] + self.data[:self.current]

    def append(self, item):
        pass

    def get(self):
        pass