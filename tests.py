import unittest
from hooks_balance import is_balanced
from add_function import add
from calculate_function import calculate_function
from cache_function import cache_function


class TestHooksBalance(unittest.TestCase):

    def test_hooks_balance(self):
        self.assertEqual(is_balanced('((()))'), 'Is balance')
        self.assertEqual(is_balanced('{[()]}'), 'Is balance')
        self.assertEqual(is_balanced('(()]}'), 'Not balance')
        self.assertEqual(is_balanced('(()]'), 'Not balance')
        self.assertEqual(is_balanced('(((('), 'Not balance')
        self.assertEqual(is_balanced(']]]]'), 'Not balance')


class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2)(3)(), 5)
        self.assertEqual(add(2)(3)(4)(), 9)
        self.assertEqual(add(2)(3)(4)(10)(), 19)


class TestCalculateFunction(unittest.TestCase):

    def test_calculate_function(self):
        self.assertEqual(calculate_function([('+', 1, 1), ('*', 2, 3)]), [2, 6])
        self.assertEqual(calculate_function([('+', 1, 1), ('*', 2, 3), ('-', 9, 3)]), [2, 6, 6])
        self.assertEqual(calculate_function([('+', 1, 1), ('*', 2, 3), ('**', 2, 2)]), [2, 6, 4])


class TestCacheFunction(unittest.TestCase):

    def test_cache_function(self):
        x = cache_function()

        lst = [x(), x(), x(), x()]

        self.assertEqual(lst[0], lst[1])
        self.assertEqual(lst[1], lst[2])
        self.assertNotEqual(lst[3], lst[2])
        self.assertNotEqual(lst[3], lst[1])
        self.assertNotEqual(lst[3], lst[0])

        print(lst)


if __name__ == '__main__':
    unittest.main()
