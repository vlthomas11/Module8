import unittest

from more_fun_with_collections.half_birthday import half_birthday as topic4

class MyTestCase(unittest.TestCase):
    def test_half_brithday(self):
        self.assertEqual(topic4('2019/12/01'), '2020/06/01')

if __name__ == '__main__':
    unittest.main()
