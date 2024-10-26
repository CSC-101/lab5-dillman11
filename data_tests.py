import data
import unittest


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)


    #### Add tests for Time._q_e__
    def test_time_eq(self):
        input = data.Time(12, 5, 6)
        input2 = data.Time(6, 5, 2)
        result = (input == input2)
        expected = False
        self.assertEqual(expected, result)

    def test_time_eq_2(self):
        input = data.Time(3, 8, 4)
        input2 = data.Time(3, 8, 4)
        result = (input == input2)
        expected = True
        self.assertEqual(expected, result)

    #### Add tests for Time.__repr__
    def test_time_repr(self):
        input = data.Time(5,1,3)
        result = input.__repr__()
        expected = "Time({}, {}, {})".format(5, 1, 3)
        self.assertEqual(expected, result)

    def test_time_repr_1(self):
        input = data.Time(10,3,5)
        result = input.__repr__()
        expected = "Time({}, {}, {})".format(10, 3, 5)
        self.assertEqual(expected, result)






    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(7, point.x)
        self.assertAlmostEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(4, point.x)
        self.assertAlmostEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))


if __name__ == '__main__':
    unittest.main()
