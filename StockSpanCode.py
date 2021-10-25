"""
stock span: determine the list of integer values for a list of stock prices p
to depict the span (s) at a given day (d), where

    s[d] := number of consecutive prior to d where p[i] <= p[d] for i < d

See the test cases for a more precise definition.

>>> print(span([10, 4, 5, 90, 120, 80, 121]))
[1, 1, 2, 4, 5, 1, 7]

>>> print(span([88]))
[1]

>>> print(span(["error"]))    # or empty list, different assertion tripped
Exception raised: ...
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

def spanWstacks(prices: list) -> list:             # better complexity O(???)
    pass

span = spanNaive            # set to spanWstacks to test your code


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
