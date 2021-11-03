"""
stock span: determine the list of integer values for a list of stock prices p
to depict the span (s) at a given day (d), where

    s[d] := number of consecutive prior to d where p[i] <= p[d] for i < d

See the test cases for a more precise definition.

>>> print(span([10, 4, 5, 90, 120, 80, 121]))
[1, 1, 2, 4, 5, 1, 7]

>>> print(span([88]))
[1]

# >>> print(span(["error"]))    # or empty list, different assertion tripped
Exception raised:...

More test cases!!!

>>> print(span([1,1,1,1,1,1,1,1,12,1]))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

>>> print(span([0,-1,4,2,2,2,-18,7]))
[1, 1, 3, 1, 2, 3, 1, 8]

>>> print(span([99999]))
[1]

"""

def intListPredicate(lst:list)-> bool:      # linear complexity O(len(lst))
    if lst == []:
        return True
    else:
        head = lst[0]
        rest = lst[1:]
        return (type(head) == type(8)) and intListPredicate(rest)

def spanNaive(prices: list) -> list:             # quadratic complexity O(len(prices)^2)
    assert len(prices) > 0
    assert intListPredicate(prices)
    
    spans = [None] * len(prices)   # generate a list to hold spans
    assert len(spans) == len(prices)
    spans[0] = 1                   # by definition, initial span is always 1

    for d in range(1, len(prices)):     # each of the remaining spans
        spans[d] = 1
        i = d - 1               # start at the previous day's price
        while (i >= 0) and (prices[d] >= prices[i]):
            spans[d] += 1           # increment the span
            i -= 1                  # move to the previous day's price

    return spans

from stackADTimpl import *

def spanWstacks(prices: list) -> list:             # better complexity O(len(prices)^2)
    assert len(prices) > 0    # precondition: the length of prices has to be greater than 0
    assert intListPredicate(prices)   # make sure every element is a number
    output = [1]*len(prices)  # stupid output
    stk = stackADT()  # stupid stack
    stk.push(0)  # first index is always 0

    for i in range(1,len(prices)):
        while not stk.empty():
            if prices[stk.top()] > prices[i]:
                output[i] = i - stk.top()
                stk.push(i)
                break
            else:
                stk.pop()
        
        if stk.empty():
            stk.push(i)
            output[i]=i+1
    
    return output

span = spanWstacks        # set to spanWstacks to test your code


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
