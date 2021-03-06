#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.head is None

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – adding new tail, no list iteration"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.list.is_empty() == False:
            return self.list.head.data
        return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – assigning new head pointer"""
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError()
        else:
            temp = self.list.head.data
            self.list.delete(temp)
            return temp


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if self.list == []:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        # count = 0
        # for item in self.list:
        #     count += 1
        # return count
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(n) – Need to shift everything to make room at index 0"""
        # TODO: Insert given item
        self.list.insert(0, item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        return self.list[len(self.list)-1]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – no shifting needed since removing item at end of list"""
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError()
        else:
            temp = self.list[len(self.list)-1]
            self.list.remove(temp)
            return temp


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
