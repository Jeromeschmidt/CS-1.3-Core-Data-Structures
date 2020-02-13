#!python

from circularbuffer import CircularBuffer
import unittest


class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        cb = CircularBuffer(5)
        assert cb.front() is None
        assert cb.length() == 0
        assert cb.is_empty() is True

    def test_init_with_list(self):
        cb = CircularBuffer(5, ['A', 'B', 'C'])
        assert cb.front() == 'A'
        assert cb.length() == 3
        assert cb.is_empty() is False

    def test_length(self):
        cb = CircularBuffer(5)
        assert cb.length() == 0
        cb.enqueue('A')
        assert cb.length() == 1
        cb.enqueue('B')
        assert cb.length() == 2
        cb.dequeue()
        assert cb.length() == 1
        cb.dequeue()
        assert cb.length() == 0

    def test_enqueue(self):
        cb = CircularBuffer(5)
        cb.enqueue('A')
        assert cb.front() == 'A'
        assert cb.length() == 1
        cb.enqueue('B')
        assert cb.front() == 'A'
        assert cb.length() == 2
        cb.enqueue('C')
        assert cb.front() == 'A'
        assert cb.length() == 3
        assert cb.is_empty() is False

    def test_front(self):
        cb = CircularBuffer(5)
        assert cb.front() is None
        cb.enqueue('A')
        assert cb.front() == 'A'
        cb.enqueue('B')
        assert cb.front() == 'A'
        cb.dequeue()
        assert cb.front() == 'B'
        cb.dequeue()
        assert cb.front() is None

    def test_dequeue(self):
        cb = CircularBuffer(5, ['A', 'B', 'C'])
        assert cb.dequeue() == 'A'
        assert cb.length() == 2
        assert cb.dequeue() == 'B'
        assert cb.length() == 1
        assert cb.dequeue() == 'C'
        assert cb.length() == 0
        assert cb.is_empty() is True
        with self.assertRaises(ValueError):
            cb.dequeue()

    def test_rollover(self):
        cb = CircularBuffer(5, ['A', 'B', 'C', 'D', 'E'])
        assert cb.front() == 'A'
        assert cb.length() == 5
        cb.enqueue('X')
        assert cb.front() == 'X'
        assert cb.length() == 5


if __name__ == '__main__':
    unittest.main()
