import search
import random
import unittest


class TestSort(unittest.TestCase):
    """

    unit test class for the search module

    """

    def test_linear_sort(self) -> None:
        """
        unit test for thr the linear search function

        :return: None
        """
        for s in range(1, 5):
            seqence = [i for i in range(10 ** s)]
            random.shuffle(seqence)

            target = random.randint(0, 10 ** s)
            result = search.linear_search(seqence, seqence[target])

            self.assertEqual(result, target)


if __name__ == "__main__":
    unittest.main()
