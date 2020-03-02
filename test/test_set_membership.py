import unittest

from more_fun_with_collections.set_membership import in_set as topic1

class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(topic1(2), True)

    def test_in_set_false(self):
        self.assertEqual(topic1(11), False)


if __name__ == '__main__':
    unittest.main()