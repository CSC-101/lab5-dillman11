import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        input1 = data.Time(5, 10, 32)
        input2 = data.Time(6,45, 53)
        result = lab5.time_add(input1, input2)
        expected = data.Time(11, 56, 25)
        self.assertEqual(expected, result)

    def test_time_add_2(self):
        input1 = data.Time(4, 52, 4)
        input2 = data.Time(2,35, 8)
        result = lab5.time_add(input1, input2)
        expected = data.Time(7, 27, 12)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending_1(self):
        input = [8,6,3,2,1]
        result = lab5.is_descending(input)
        expected = True
        self.assertEqual(expected, result)

    def test_is_descending_2(self):
        input = [10, 6, 6, 5, 3, 2, 1]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected, result)

    def test_is_descending_3(self):
        input = [13, 5, 6, 2, 1]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected, result)


    # Part 5
    def test_largest_between_1(self):
        input = [15, 6, 1, 23, 8]
        input2 = 0
        input3 = 3
        result = lab5.largest_between(input, input2, input3)
        expected = 3
        self.assertEqual(expected, result)

    def test_largest_between_2(self):
        input = [6, 3, 15, 7, 18, 3, 7, 24]
        input2 = 1
        input3 = 6
        result = lab5.largest_between(input, input2, input3)
        expected = 4
        self.assertEqual(expected, result)

    def test_largest_between_3(self):
        input = [6, 3, 15, 7, 24]
        input2 = 1
        input3 = 6
        result = lab5.largest_between(input, input2, input3)
        expected = None
        self.assertEqual(expected, result)

    def test_largest_between_4(self):
        input = [15, 7, 18, 3, 7]
        input2 = -1
        input3 = 3
        result = lab5.largest_between(input, input2, input3)
        expected = None
        self.assertEqual(expected, result)

    def test_largest_between_5(self):
        input = [6, 3, 15, 7]
        input2 = 2
        input3 = 0
        result = lab5.largest_between(input, input2, input3)
        expected = None
        self.assertEqual(expected, result)


    # Part 6
    def test_furthest_from_origin_1(self):
        input = [data.Point(5,10), data.Point(9, 11), data.Point(4,15)]
        result = lab5.furthest_from_origin(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_furthest_from_origin_2(self):
        input = [data.Point(11, 23), data.Point(-34,8), data.Point(27,-13), data.Point(-38,-2)]
        result = lab5.furthest_from_origin(input)
        expected = 3
        self.assertEqual(expected, result)

    def test_furthest_from_origin_3(self):
        input = []
        result = lab5.furthest_from_origin(input)
        expected = None
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()
