import sort
import random
import unittest


class TestSort(unittest.TestCase):
    """

    unit test class for the sort module

    """

    def test_quick_sort(self) -> None:
        """
        unit test for thr the quick sort function

        :return: None
        """

        for s in range(1, 5):
            seqence = [i for i in range(10 ** s)]
            answer = [*seqence]

            random.shuffle(seqence)
            sort.quick_sort(seqence)

            self.assertEqual(seqence, answer)


if __name__ == "__main__":
    unittest.main()
