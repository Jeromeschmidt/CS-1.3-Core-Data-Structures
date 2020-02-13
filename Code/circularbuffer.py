
class CircularBuffer(list):

    def __init__(self, max_size, iterable=None):
        """Initialize this node with the given data."""
        # self = list()
        self.max_size = max_size
        self.size = 0
        self.ph = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False

    def length(self):
        return self.size

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty() == False:
            return self[0]
        return None

    def enqueue(self, item):
        if len(self) < self.max_size:
            self.append(item)
            self.size += 1
        else:
            self[self.ph] = item
            self.ph += 1
        if self.ph == self.max_size:
            self.ph = 0

    def dequeue(self):
        if len(self) is not 0:
            self.size -= 1
            return self.pop(0)
        else:
            raise ValueError()

    def iterate(self):
        all_items = []
        for item in self:
            all_items.append(item)
        return all_items

def test_queue():
    q = CircularBuffer(5)
    q.enqueue((1, 1))
    q.enqueue((2, 2))
    q.enqueue((3, 3))
    q.enqueue((4, 4))
    q.enqueue((5, 5))
    q.enqueue((6, 6))
    print(q.iterate())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

if __name__ == '__main__':
    test_queue()
