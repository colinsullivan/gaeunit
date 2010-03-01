'''
Created on May 5, 2009

@author: george
'''
import unittest
import gaeunit

class Test(unittest.TestCase):
    tc = gaeunit.GAETestCase("run")
    
    def test_html_compare_ignorable_blank(self):
        html1 = """ <div>  test text
                </div> """
        html2 = """<div>test text</div>"""
        self.tc.assertHtmlEqual(html1, html2)

    def test_html_compare_unignorable_blank(self):
        html1 = """<div>test text</div>"""
        html2 = """<div>testtext</div>"""
        self.assertRaises(AssertionError, self.tc.assertHtmlEqual, html1, html2)

    def test_kill_extra_blank(self):
        html1 = """ < div  class="aaa">  test  test\t </div > """
        html2 = """<div class="aaa">test test</div>"""
        self.assertEqual(self.tc._formalize(html1), html2)
        
    def test_replace_return_sign(self):
        html1 = """test
test\r\n"""
        html2 = """test test """
        self.assertEqual(self.tc._formalize(html1), html2)
        
    def test_unescape(self):
        html1 = "&lt; &amp; &gt;"
        html2 = "< & >"
        self.assertEqual(self.tc._formalize(html1), html2)
        
    def test_findHtmlDifference(self):
        html1 = "abcdef"
        html2 = "abccef"
        result_expected = "\nabcdef\nabccef\n___^"
        result = self.tc._findHtmlDifference(html1, html2)
        self.assertEqual(result, result_expected)

    def test_findHtmlDifference_long(self):
        html1 = "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkk"
        html2 = "aaaaabbbbbcccccdddddeeeeeeffffggggghhhhhiiiiijjjjjkkkkk"
        result_expected = "\n...bbbbbcccccdddddeeeeefffffggggghhhhhiiiiij...\n...bbbbbcccccdddddeeeeeeffffggggghhhhhiiiiij...\n_______________________^"
        result = self.tc._findHtmlDifference(html1, html2)
        self.assertEqual(result, result_expected)

    def test_findHtmlDifference_long_leftmost(self):
        html1 = "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkk"
        html2 = "aaaabbbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkk"
        result_expected = "\naaaaabbbbbcccccdddddeeeeefffffggggghhhhhi...\naaaabbbbbbcccccdddddeeeeefffffggggghhhhhi...\n____^"
        result = self.tc._findHtmlDifference(html1, html2)
        self.assertEqual(result, result_expected)

    def test_findHtmlDifference_long_rightmost(self):
        html1 = "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkk"
        html2 = "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjkkkkkk"
        result_expected = "\n...cdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkk\n...cdddddeeeeefffffggggghhhhhiiiiijjjjkkkkkk\n______________________________________^"
        result = self.tc._findHtmlDifference(html1, html2)
        self.assertEqual(result, result_expected)


class SystemTest(gaeunit.GAETestCase):
    def test_html_compare_ignorable_blank(self):
        html1 = """ <div>  test text
                </div> """
        html2 = """<div>test text</div>"""
        self.assertHtmlEqual(html1, html2)

    def test_html_compare_unignorable_blank(self):
        html1 = """<div>test text</div>"""
        html2 = """<div>testtext</div>"""
        self.assertRaises(AssertionError, self.assertHtmlEqual, html1, html2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()