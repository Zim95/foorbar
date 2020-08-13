from unittest import TestCase
from solution import answer


class TestSolution(TestCase):

    def test_threshold_zero(self):
        self.assertEqual(
            answer([1, 2, 3], 0),
            []
        )
    
    def test_all_same_item_list(self):
        self.assertEqual(
            answer([1, 1, 1, 1], 1),
            []
        )
    
    def test_all_unique_item_list(self):
        self.assertEqual(
            answer([1, 2, 3, 4], 1),
            [1, 2, 3, 4]
        )
    
    def test_normal(self):
        self.assertEqual(
            answer([1, 1, 2, 2, 3, 3, 4, 5], 1),
            [4, 5]
        )
    
    def test_empty_list(self):
        self.assertEqual(
            answer([], 1),
            []
        )