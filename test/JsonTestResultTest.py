'''
Created on May 6, 2009

@author: george
'''
import unittest
import gaeunit

class Test(unittest.TestCase):
    tr = gaeunit.JsonTestResult()

    def test_list(self):
        testcase = MockTestCase()
        list = [(testcase, "error")]
        result_expected = [{"desc":"test","detail":"error"}]
        result = self.tr._list(list)
        self.assertEqual(result, result_expected) 
        
    def test_list_special_character(self):
        testcase = MockTestCase()
        list = [(testcase, "<error>")]
        result_expected = [{"desc":"test","detail":"&lt;error&gt;"}]
        result = self.tr._list(list)
        self.assertEqual(result, result_expected) 
        

class MockTestCase:
    def shortDescription(self):
        return "test"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()