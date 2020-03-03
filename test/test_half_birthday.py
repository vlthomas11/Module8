import unittest

from datetime import datetime
from more_fun_with_collections.half_birthday import half_birthday as topic4


class MyTestCase(unittest.TestCase):
    def test_half_brithday(self):
        self.assertEqual(topic4('12/01/2019'), datetime.strptime('06/01/2020', '%m/%d/%Y'))


if __name__ == '__main__':
    unittest.main()
