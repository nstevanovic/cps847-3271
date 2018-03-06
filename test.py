
import unittest
import cps3271

class TestMyFunc(unittest.TestCase):
 
    def setUp(self):
        pass 

    def test_multiply_by_four(self): 
        self.assertEqual(  cps3271.cps3271(4), 16)
        
if __name__ == '__main__':
    unittest.main()
