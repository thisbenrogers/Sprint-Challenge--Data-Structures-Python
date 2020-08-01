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

    def append(self, item):
        pass

    def get(self):
        pass