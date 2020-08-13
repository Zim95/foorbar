from unittest import TestCase
from solution1 import solution


class TestSalutations(TestCase):

    def test_string(self):
        self.assertEqual(
            solution(">----<"),
            2
        )
    
    def test_blank_string(self):
        self.assertEqual(
            solution("----"),
            0
        )
    
    def test_empty_string(self):
        self.assertEqual(
            solution(""),
            0
        )
    
    def test_extreme_right(self):
        self.assertEqual(
            solution(">>>>>"),
            0
        )
    
    def test_extreme_left(self):
        self.assertEqual(
            solution("<<<<<"),
            0
        )
