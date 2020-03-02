import unittest

from more_fun_with_collections.dict_membership import in_dict as topic2

class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(topic2({1:'orange',2:'lemon',3:'lime'},3), True)

    def test_in_set_false(self):
        self.assertEqual(topic2({1:'orange',2:'lemon',3:'lime'},7), False)


if __name__ == '__main__':
    unittest.main()