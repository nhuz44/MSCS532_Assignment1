import unittest
from insertion_sort import insertion_sort_descending


class TestInsertionSort(unittest.TestCase):

    def test_unsorted_array(self):
        numbers = [12, 5, 9, 2, 18, 7]
        self.assertEqual(
            insertion_sort_descending(numbers),
            [18, 12, 9, 7, 5, 2]
        )

    def test_already_descending(self):
        numbers = [10, 8, 6, 4, 2]
        self.assertEqual(
            insertion_sort_descending(numbers),
            [10, 8, 6, 4, 2]
        )

    def test_duplicates(self):
        numbers = [5, 2, 5, 9, 2]
        self.assertEqual(
            insertion_sort_descending(numbers),
            [9, 5, 5, 2, 2]
        )

    def test_negative_numbers(self):
        numbers = [-3, 4, -1, 0]
        self.assertEqual(
            insertion_sort_descending(numbers),
            [4, 0, -1, -3]
        )

    def test_empty_array(self):
        self.assertEqual(insertion_sort_descending([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort_descending([7]), [7])


if __name__ == "__main__":
    unittest.main()