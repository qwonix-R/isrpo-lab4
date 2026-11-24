import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(10), math.pi * 100)

    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(circle_area(2.5), math.pi * 6.25)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(10), 2 * math.pi * 110)

    def test_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle_perimeter(1.5), 2 * math.pi * 1.5)


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rect_area(10, 5), 50)

    def test_area_zero(self):
        self.assertEqual(rect_area(10, 0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(rect_area(2.5, 4), 10.0)

    def test_perimeter(self):
        self.assertEqual(rect_perimeter(10, 5), 30)

    def test_perimeter_zero(self):
        self.assertEqual(rect_perimeter(0, 0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(rect_perimeter(1.5, 2.5), 8.0)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(10), 100)

    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(square_area(2.5), 6.25)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(10), 40)

    def test_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square_perimeter(1.5), 6.0)


if __name__ == '__main__':
    unittest.main()