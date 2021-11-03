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
>>> assert not lst1.empty()
>>> lst1 = listADT("alpha", lst1)
>>> assert not lst1.rest().empty()
>>> assert lst1.head() == "alpha"
>>> assert lst1.__str__() == "['alpha', 'beta', 'alpha']"
>>> a = listADT()
>>> assert a.head() == None
>>> assert not lst1.__eq__(lst)

"""

class listADT:
    def __init__(self, head = None, rest = None):
        if head == None:            # empty constructor
            self.rep = []
        else:                       # extending constructor
            assert type(rest) == listADT  # precondition: the rest has to be a listADT
            self.rep = [head] + rest.rep

    def empty(self) -> bool:  # postcondition: gives a boolean value
        return self.rep == []  # return a bool depending on if the list is empty.

    def head(self):
        if len(self.rep) == 0:
            return None
        else:
            return self.rep[0]    # the first element of the list
                                  # postcondition: returns the first value of the listADT

    def rest(self):
        if len(self.rep) > 1:
            temp = listADT()
            temp.rep = self.rep[1:]
            return temp  # return the rest of the list
        else:
            return listADT()  # if the rest is empty, return an empty listADT

    def __eq__(self, other) -> bool:     # compare two things
        assert type(other) == listADT    # precondition: the other has to be listADT as well
        return self.rep == other.rep     # postcondition: return a bool 


    def __str__(self) -> str:              # "abstraction function" (to text)
        return str(self.rep)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")

    
