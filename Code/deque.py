
class Deque(list):

    def __init__(self, iterable=None):
        """Initialize this node with the given data."""
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue_to_end(item)

    def length(self):
        return len(self.list)

    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False

    def enqueue_to_start(self, item):
        self.list.insert(0, item)

    def enqueue_to_end(self, item):
        self.list.append(item)

    def dequeue_from_start(self):
        if len(self.list) is not 0:
            return self.list.pop(0)
        else:
            raise ValueError()

    def dequeue_from_end(self):
        if len(self.list) is not 0:
            return self.list.pop(len(self)-1)
        else:
            raise ValueError()

    def peek_front(self):
        if not self.is_empty():
            return self.list[0]
        return None

    def peek_back(self):
        if not self.is_empty():
            return self.list[len(self.list)-1]
        return None

    def iterate(self):
        all_items = []
        for item in self.list:
            all_items.append(item)
        return all_items

# def test_queue():
#     q = Duque()
#     q.enqueue_to_start((1, 1))
#     q.enqueue_to_end((2, 2))
#     q.enqueue_to_start((3, 3))
#     print(q.iterate())
#     print(q.dequeue_from_start())
#     print(q.dequeue_from_end())
#     print(q.dequeue_from_start())
#     print(q.dequeue_from_start())

if __name__ == '__main__':
    test_queue()
