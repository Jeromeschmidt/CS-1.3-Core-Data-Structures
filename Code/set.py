from binarytree import BinarySearchTree

class Set:
    def __init__(self, elements=None):
        self.tree = BinarySearchTree()
        self.size = 0
        if elements is not None:
            for elm in elements:
                self.add(elm)

    def size(self):
        return self.tree.size

    def contains(self, element):
        if self.tree.contains(element):
            return True
        return False

    def add(self, element):
        if self.contains(element):
            raise ValueError("Cannot add element to Set again")
        else:
            self.tree.insert(element)
            self.size += 1

    def remove(self, element):
        self.tree.delete(element)
        self.size -= 1

    def union(self, other_set):
        """TODO: Running time: O(n*squared(k)), have to visit every node
        TODO: Memory usage: O(n+k) nodes are stored on stack"""
        result = self.tree.items_in_order()
        for elm in other_set.tree.items_in_order():
            if elm not in result:
                result.append(elm)
        return Set(result)

    def intersection(self, other_set):
        """TODO: Running time: O(n*squared(k)), have to visit every node
        TODO: Memory usage: O(n+k) nodes are stored on stack"""
        result = Set()
        for elm in self.tree.items_in_order():
            if other_set.contains(elm):
                result.add(elm)
        return result

    def difference(self, other_set):
        """TODO: Running time: O(n*squared(k)), have to visit every node
        TODO: Memory usage: O(n+k) nodes are stored on stack"""
        result = Set()
        for elm in self.tree.items_in_order():
            if not other_set.contains(elm):
                result.add(elm)
        for elm in other_set.tree.items_in_order():
            if elm not in self.tree.items_in_order():
                result.add(elm)
        return result

    def is_subset(self, other_set):
        """TODO: Running time: O(n*squared(k)), have to visit every node
        TODO: Memory usage: O(n+k) nodes are stored on stack"""
        if self.size > other_set.size:
            return False

        for elm in self.tree.items_in_order():
            if not other_set.tree.contains(elm):
                return False
        return True
