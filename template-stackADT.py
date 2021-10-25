"""
stackADT: an implementation of a stack represented as listADT

>>> stk = stackADT()
>>> assert stk.empty()
>>> stk = push("omega")
>>> assert not stk.empty()
>>> assert stk.top() == "omega"
"""

# import the listADT

class stackADT:
    def __init__(self):
        pass

    def empty(self):    # returns True iff the stack is empty
        pass

    def top(self):      # returns the value at the top of the stack
        pass

    def push(self, x):  # mutates the stack to add x at the top
        pass

    def pop(self):      # mutates the stack to remove x from the top
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
