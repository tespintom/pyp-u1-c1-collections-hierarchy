from .base_classes import Sequenceable, Appendable, Pushable, Popable


class List(Sequenceable, Appendable, Pushable, Popable):
    pass


class Stack(Sequenceable, Pushable, Popable):
    pass
