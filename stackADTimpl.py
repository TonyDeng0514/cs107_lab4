"""
stackADT: an implementation of a stack represented as listADT

>>> stk = stackADT()
>>> assert stk.empty()
>>> stk.push("omega")
>>> assert not stk.empty()
>>> assert stk.top() == "omega"
>>> stk.pop()
>>> assert stk.empty()

more test cases!!!

>>> stk.push('alpha')
>>> stk.push('beta')
>>> assert stk.top() == 'beta'
>>> stk.push('charlie')
>>> stk.push('delta')
>>> assert not stk.top() == 'charlie'
>>> stk.pop()
>>> stk.pop()
>>> assert stk.top() == 'beta'
"""

from listADTimpl import listADT

class stackADT:
    def __init__(self, top = None, rest = None):  # complexity: O(1)
        if top == None:            # empty constructor
            self.rep = listADT()
        else:                       # extending constructor
            assert type(rest) == listADT  # precondtion: the rest has to be a listADT
            self.rep = listADT(top, rest.rep)

    def empty(self) -> bool:    # returns True iff the stack is empty
        return self.rep.empty()  # postcondition: returns a boolean value.
                                # complexity: O(1)

    def top(self):      # returns the value at the top of the stack
        if self.rep.empty() == True:
            return None
        else:        
            return self.rep.head()  # postcondition: returns the first value.
                                    # complexity: O(1)

    def push(self, x):  # mutates the stack to add x at the top
        self.rep = listADT(x, self.rep)
                        # complexity: O(1)

    def pop(self):      # mutates the stack to remove x from the top
        self.rep = listADT(self.rep.rest().head(), self.rep.rest().rest())
                        # complexity: O(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
