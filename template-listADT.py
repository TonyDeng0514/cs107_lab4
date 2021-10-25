"""
listADT: an implementation of a list represented as a Python list

>>> lst = listADT()
>>> assert lst.empty()
>>> lst = listADT("alpha", lst)
>>> assert not lst.empty()
>>> assert lst.rest().empty()
>>> assert lst.head() == "alpha"
"""

class listADT:
    def __init__(self, head = None, rest = None):
        if head == None:            # empty constructor
            self.rep = []
        else:                       # extending constructor
            self.rep = [head] + rest.rep

    def empty(self):
        pass

    def head(self):
        pass

    def rest(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):              # "abstraction function" (to text)
        return str(self.rep)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")

    
