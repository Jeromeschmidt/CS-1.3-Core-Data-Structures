#!python

from deque import Deque
import unittest


class DequeTest(unittest.TestCase):

    def test_init(self):
        d = Deque()
        assert d.peek_front() is None
        assert d.peek_back() is None
        assert d.length() == 0
        assert d.is_empty() is True

    def test_init_with_list(self):
        d = Deque(['A', 'B', 'C'])
        assert d.peek_front() == 'A'
        assert d.peek_back() == 'C'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_length(self):
        d = Deque()
        assert d.length() == 0
        d.enqueue_to_start('A')
        assert d.length() == 1
        d.enqueue_to_start('B')
        assert d.length() == 2
        d.dequeue_from_end()
        assert d.length() == 1
        d.dequeue_from_end()
        assert d.length() == 0

    def test_enqueue_to_start(self):
        d = Deque()
        d.enqueue_to_start('A')
        assert d.peek_front() == 'A'
        assert d.length() == 1
        d.enqueue_to_start('B')
        assert d.peek_front() == 'B'
        assert d.length() == 2
        d.enqueue_to_start('C')
        assert d.peek_front() == 'C'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_enqueue_to_end(self):
        d = Deque()
        d.enqueue_to_end('A')
        assert d.peek_front() == 'A'
        assert d.length() == 1
        d.enqueue_to_end('B')
        assert d.peek_front() == 'A'
        assert d.length() == 2
        d.enqueue_to_end('C')
        assert d.peek_front() == 'A'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_peek_front(self):
        d = Deque()
        assert d.peek_front() is None
        d.enqueue_to_start('A')
        assert d.peek_front() == 'A'
        d.enqueue_to_start('B')
        assert d.peek_front() == 'B'
        d.dequeue_from_end()
        assert d.peek_front() == 'B'
        d.dequeue_from_end()
        assert d.peek_front() is None

    def test_peek_back(self):
        d = Deque()
        assert d.peek_back() is None
        d.enqueue_to_start('A')
        assert d.peek_back() == 'A'
        d.enqueue_to_start('B')
        assert d.peek_back() == 'A'
        d.dequeue_from_end()
        assert d.peek_back() == 'B'
        d.dequeue_from_end()
        assert d.peek_back() is None

    def test_dequeue_from_start(self):
        d = Deque(['A', 'B', 'C'])
        assert d.dequeue_from_start() == 'A'
        assert d.length() == 2
        assert d.dequeue_from_start() == 'B'
        assert d.length() == 1
        assert d.dequeue_from_start() == 'C'
        assert d.length() == 0
        assert d.is_empty() is True
        with self.assertRaises(ValueError):
            d.dequeue_from_start()


if __name__ == '__main__':
    unittest.main()
