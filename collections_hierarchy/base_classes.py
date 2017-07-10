from .node import Node


class Sequenceable(object):
    def __init__(self):
        self.start = None
        self.end = None

    def get_elements(self):
        elements = []
        current_node = self.start
        while current_node:
            elements.append(current_node.value)
            current_node = current_node.next

        return elements



class Appendable(object):
    def append(self, element):
        node = Node(element)
        if self.start is not None:
            self.end.next = node
        else:
            self.start = node
        self.end = node




class Popable(object):

    def pop(self):
        if self.start is None:
            raise IndexError('pop from empty list')

        node = self.start
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.next

        return node.value


class Pushable:
    def push(self, element):
        node = Node(element)

        if self.start is None:
            self.start = node
            self.end = self.start
        else:
            node.next = self.start
            self.start = node
