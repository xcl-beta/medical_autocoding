import unittest
from evaluation import intersect_size

import numpy as np

class TestIntersectSize(unittest.TestCase):
    def test_empty_lists(self):
        list1 = []
        list2 = []
        result = intersect_size(list1, list2,axis=0)
        self.assertEqual(result, 0)

    def test_no_common_elements(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        result = intersect_size(list1, list2,axis=0)
        self.assertEqual(result, 0)

    def test_some_common_elements(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        result = intersect_size(list1, list2,axis=0)
        self.assertEqual(result, 2)

    def test_all_common_elements(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        result = intersect_size(list1, list2,axis=0)
        self.assertEqual(result, 5)

    def test_intersect_size_axis_0(self):
        yhat = np.array([[1, 0, 1], [0, 1, 0]])
        y = np.array([[1, 1, 0], [1, 0, 1]])
        result = intersect_size(yhat, y, axis=0)
        expected = np.array([1., 0., 1.])
        np.testing.assert_array_equal(result, expected)

    def test_intersect_size_axis_1(self):
        yhat = np.array([[1, 0, 1], [0, 1, 0]])
        y = np.array([[1, 1, 0], [1, 0, 1]])
        result = intersect_size(yhat, y, axis=1)
        expected = np.array([1., 0.])
        np.testing.assert_array_equal(result, expected)


    def testExample1(self):
        x = np.arange(5)
        result = np.logical_and(x>1, x<4)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
