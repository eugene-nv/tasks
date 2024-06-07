import unittest
from hooks_balance import is_balanced


class TestHooksBalance(unittest.TestCase):

    def test_hooks_balance(self):
        self.assertEqual(is_balanced('((()))'), 'Is balance')
        self.assertEqual(is_balanced('{[()]}'), 'Is balance')
        self.assertEqual(is_balanced('(()]}'), 'Not balance')
        self.assertEqual(is_balanced('(()]'), 'Not balance')
        self.assertEqual(is_balanced('(((('), 'Not balance')
        self.assertEqual(is_balanced(']]]]'), 'Not balance')


if __name__ == '__main__':
    unittest.main()
