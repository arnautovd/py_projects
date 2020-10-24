import unittest
from module import get_sum

class Test(unittest.TestCase):
    
    def test_get_sum(self):
        result = get_sum(10, 11)
        self.assertEqual(result, 21)
    



if __name__ == '__main__':
    unittest.main()