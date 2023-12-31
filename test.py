import unittest
from main import *

class TestStringMethods(unittest.TestCase):

    def test(self):
        self.assertEqual(product(6, 8), 48)
    
    def test2(self):
        self.assertEqual(product(6, -1), -6)
        
    def test3(self):
    	self.assertEqual(product(0, 8), 0)

if __name__ == '__main__':
    unittest.main()
