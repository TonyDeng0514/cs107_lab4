"""
stackADT: an implementation of a stack represented as listADT

>>> stk = stackADT()
>>> assert stk.empty()
>>> stk = push("omega")
>>> assert not stk.empty()
>>> assert stk.top() == "omega"
"""

from template_listADT import listADT

class stackADT:
    def __init__(self, head = None, rest = None):
        if head == None:            # empty constructor
            self.rep = listADT()
        else:                       # extending constructor
            self.rep = listADT(head) + rest.rep

    def empty(self):    # returns True iff the stack is empty
        return self.rep == listADT()

    def top(self):      # returns the value at the top of the stack
        return self.rep.head

    def push(self, x):  # mutates the stack to add x at the top
        pass

    def pop(self):      # mutates the stack to remove x from the top
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
