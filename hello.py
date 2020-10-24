import unittest
from module import get_sum, print_some

class Test(unittest.TestCase):
    
    def test_get_sum(self):
        result = get_sum(10, 11)
        self.assertEqual(result, 21)
    
    def test_print_some(self):
        result = print_some(12)
        self.assertEqual(isinstance(result, str), True)



if __name__ == '__main__':
    unittest.main()