from .node import Node


class Sequenceable(object):
    def __init__(self):
        pass

    def get_elements(self):
        pass


class Appendable(object):
    def append(self, element):
        pass


class Popable(object):
    def pop(self):
        pass


class Pushable:
    def push(self, element):
        pass
