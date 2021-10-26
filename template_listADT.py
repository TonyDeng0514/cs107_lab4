"""
listADT: an implementation of a list represented as a Python list

>>> lst = listADT()
>>> assert lst.empty()
>>> lst = listADT("alpha", lst)
>>> assert not lst.empty()
>>> assert lst.rest().empty()
>>> assert lst.head() == "alpha"

more test cases!!!!

>>> lst1 = listADT("beta", lst)
>>> assert not lst.empty()
>>> lst1 = listADT("alpha", lst1)
>>> assert not lst1.empty()
>>> assert not lst1.rest().empty()
>>> assert lst1.head() == "alpha"

"""

class listADT:
    def __init__(self, head = None, rest = None):
        if head == None:            # empty constructor
            self.rep = []
        else:                       # extending constructor
            self.rep = [head] + rest.rep

    def empty(self) -> bool:
        return self.rep == []  # empty list

    def head(self):
        return self.rep[0]    # the first element of the list

    def rest(self):
        if len(self.rep) > 1:
            temp = listADT()
            temp.rep = self.rep[1:]
            return temp  # return the rest of the list
        else:
            return listADT()

    def __eq__(self, other) -> bool:     # compare two things
        return self.rep == other.rep


    def __str__(self) -> str:              # "abstraction function" (to text)
        return str(self.rep)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")

    
