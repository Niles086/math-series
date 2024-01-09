# test_series.py

import unittest
import series

class TestSeriesFunctions(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(series.fibonacci(0), None)
        self.assertEqual(series.fibonacci(1), 0)
        self.assertEqual(series.fibonacci(2), 1)
        self.assertEqual(series.fibonacci(6), 5)
        self.assertEqual(series.fibonacci(10), 34)

    def test_lucas(self):
        self.assertEqual(series.lucas(0), None)
        self.assertEqual(series.lucas(1), 2)
        self.assertEqual(series.lucas(2), 1)
        self.assertEqual(series.lucas(5), 7)
        self.assertEqual(series.lucas(8), 29)

    def test_sum_series_fibonacci(self):
        self.assertEqual(series.sum_series(0), None)
        self.assertEqual(series.sum_series(1), 0)
        self.assertEqual(series.sum_series(2), 1)
        self.assertEqual(series.sum_series(6), 5)
        self.assertEqual(series.sum_series(10), 34)

    def test_sum_series_lucas(self):
        self.assertEqual(series.sum_series(0, 2, 1), None)
        self.assertEqual(series.sum_series(1, 2, 1), 2)
        self.assertEqual(series.sum_series(2, 2, 1), 1)
        self.assertEqual(series.sum_series(5, 2, 1), 7)
        self.assertEqual(series.sum_series(8, 2, 1), 29)

    def test_sum_series_custom(self):
        self.assertEqual(series.sum_series(0, 3, 4), None)
        self.assertEqual(series.sum_series(1, 3, 4), 3)
        self.assertEqual(series.sum_series(2, 3, 4), 4)
        self.assertEqual(series.sum_series(5, 3, 4), 11)
        self.assertEqual(series.sum_series(8, 3, 4), 22)

if __name__ == '__main__':
    unittest.main()
