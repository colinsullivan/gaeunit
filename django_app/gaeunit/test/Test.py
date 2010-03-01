'''
Created on May 11, 2009

@author: george
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        self.assertTrue(False)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()