"""
stackADT: an implementation of a stack represented as listADT

>>> stk = stackADT()
>>> assert stk.empty()
>>> stk.push("omega")
>>> assert not stk.empty()
>>> assert stk.top() == "omega"
"""

from template_listADT import listADT

class stackADT:
    def __init__(self, top = None, rest = None):
        if top == None:            # empty constructor
            self.rep = listADT()
        else:                       # extending constructor
            self.rep = listADT(top, rest.rep)

    def empty(self):    # returns True iff the stack is empty
        return self.rep == listADT()

    def top(self):      # returns the value at the top of the stack
        if self.rep == self.rep.empty():
            return stackADT()
        else:        
            return self.rep.head

    def push(self, x):  # mutates the stack to add x at the top
        self.rep = listADT(x, self.rep)

    def pop(self):      # mutates the stack to remove x from the top
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
