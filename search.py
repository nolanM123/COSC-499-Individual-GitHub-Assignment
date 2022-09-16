"""

This file includes various searching algorithms

"""


from typing import Sequence


def linear_search(seq: Sequence, value: any, key: callable = None) -> int:
    """
    Apples linear search on given seqence to find target

    :param seq: seqence of any collection
    :param value: the value to search for
    :param key: function that serves as a key for the search comparison
    :return: returns the index of the target, returns -1 if target is not found
    """

    if key is None:
        key = lambda a: a
    
    for i, item in enumerate(seq):
        if key(item) == value:
            return i
    
    return -1