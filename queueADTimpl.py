"""
queueADT: an implementation of a queue represented as stackADT

>>> que = queueADT()
>>> assert que.empty()
>>> que.enqueue("chi")
>>> assert not que.empty()
>>> assert que.front() == "chi"
>>> que.dequeue()
>>> assert que.empty()


more test cases!!

>>> que.enqueue('alpha')
>>> que.enqueue('beta')
>>> que.enqueue('charlie')
>>> assert que.front() == 'alpha'
>>> que.dequeue()
>>> assert que.front() == 'beta'
>>> assert not que.empty()
"""

from stackADTimpl import *

class queueADT:
    def __init__(self, front=None, rest=None):
        if front == None:            # empty constructor
            self.rep = stackADT()
        else:                       # extending constructor
            assert type(rest) == stackADT  # precondition: the rest has to be stackADT
            self.rep = stackADT(front, rest.rep)   # complexity: O(1)

    def empty(self) -> bool:    # returns True iff the queue is empty
        return self.rep.empty()  # postcondition: returns a boolean value
                                # complexity: O(1)
        
    def front(self):      # returns the value at the front of the queue
        if self.rep == stackADT():
            return None
        else:
            return self.rep.top()  # postcondition: returns a value
                                    # complexity: O(1)

    def enqueue(self, x):  # mutates the queue to add x at the back
        self.rep.rep.rep.append(x)  
                            # complexity: o(1)

    def dequeue(self):      # mutates the queue to remove x from the front
        self.rep.rep = self.rep.rep.rest()
                            # complexity: o(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
