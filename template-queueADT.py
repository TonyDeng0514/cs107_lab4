"""
queueADT: an implementation of a queue represented as stackADT

>>> que = queueADT()
>>> assert que.empty()
>>> que.enqueue("chi")
>>> assert not que.empty()
>>> assert que.front() == "chi"
"""

# import anything???

class queueADT:
    def __init__(self):
        pass

    def empty(self):    # returns True iff the queue is empty
        pass

    def front(self):      # returns the value at the fromt of the queue
        pass

    def enqueue(self, x):  # mutates the queue to add x at the back
        pass

    def dequeue(self):      # mutates the queue to remove x from the front
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
