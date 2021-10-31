"""
queueADT: an implementation of a queue represented as stackADT

>>> que = queueADT()
>>> assert que.empty()
>>> que.enqueue("chi")
>>> assert not que.empty()
>>> assert que.front() == "chi"
>>> que.dequeue()
>>> assert que.empty()
"""

from stackADTimpl import *

class queueADT:
    def __init__(self, front=None, rest=None):
        if front == None:            # empty constructor
            self.rep = stackADT()
        else:                       # extending constructor
            assert type(rest) == stackADT
            self.rep = stackADT(front, rest.rep)

    def empty(self) -> bool:    # returns True iff the queue is empty
        return self.rep.empty()
        
    def front(self):      # returns the value at the fromt of the queue
        if self.rep == stackADT():
            return None
        else:
            return self.rep.top()

    def enqueue(self, x):  # mutates the queue to add x at the back
        self.rep.rep.rep.append(x)

    def dequeue(self):      # mutates the queue to remove x from the front
        self.rep.rep = self.rep.rep.rest()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
