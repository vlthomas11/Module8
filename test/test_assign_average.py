import unittest

from more_fun_with_collections.assign_average import switch_average as topic3


class MyTestCase(unittest.TestCase):
    def test_switch_A(self):
        self.assertEqual(topic3('A'), '90 - 100')

    def test_switch_B(self):
        self.assertEqual(topic3('B'),'80 - 89')

    def test_switch_C(self):
        self.assertEqual(topic3('C'),'70 - 79')

    def test_switch_D(self):
        self.assertEqual(topic3('D'),'60 - 69')

    def test_switch_F(self):
        self.assertEqual(topic3('F'),'0 - 59')

    def test_switch_z(self):
        self.assertEqual(topic3('Z'),'Invalid Input')

if __name__ == '__main__':
    unittest.main()

