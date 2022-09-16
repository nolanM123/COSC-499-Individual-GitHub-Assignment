"""

This file includes various sorting algorithms

"""


from typing import Sequence


def quick_sort(seq: Sequence[any], key: callable = None, lmp: int = 0, rmp: int = None) -> None:
    """
    Apples quick sort algorithm on given sequence to sort the given seqence

    :param seq: seqence of any collection
    :param key: function that serves as a key for the sort comparison
    :param lmp: left most index of partition
    :param rmp: right most index of partition
    :return: None
    """

    if key is None:
        key = lambda a :a

    if rmp is None:
        rmp = len(seq) - 1
    
    if lmp < rmp:
        p: int = lmp

        for i in range(lmp, rmp):
            if key(seq[i]) < key(seq[rmp]):
                seq[i], seq[p] = seq[p], seq[i]
                p += 1
        
        seq[rmp], seq[p] = seq[p], seq[rmp]
        quick_sort(seq, key, lmp, p - 1)
        quick_sort(seq, key, p + 1, rmp)
