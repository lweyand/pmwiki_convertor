#!/usr/bin/python
""" this is a test suite on DokuwikiConvertor class"""

import unittest
from convertors import DokuwikiConvertor

class DokuwikiConvertorTest(unittest.TestCase):
    """ this is a test class suite on DokuwikiConvertor class """

    dokuwiki_convertor = DokuwikiConvertor()

    def test_should_extract_text(self):
        """ this is a test """
        line = 'text=this the text to extract'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('this the text to extract', result)

    def test_should_convert_to_linebreak(self):
        """ this is a test """
        line = 'text=foo%0abar'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('foo\nbar', result)

    def test_should_convert_to_percent(self):
        """ this is a test """
        line = 'text=foo%25bar'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('foo%bar', result)

    def test_should_convert_to_h1(self):
        """ this is a test """
        line = 'text=\n!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n====== Header ======', result)
        line = 'text=!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('====== Header ======', result)

    def test_should_convert_to_h2(self):
        """ this is a test """
        line = 'text=\n!!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n===== Header =====', result)
        line = 'text=!!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('===== Header =====', result)

    def test_should_convert_to_h3(self):
        """ this is a test """
        line = 'text=\n!!!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n==== Header ====', result)
        line = 'text=!!!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('==== Header ====', result)

    def test_should_convert_to_h4(self):
        """ this is a test """
        line = 'text=\n!!!!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n=== Header ===', result)
        line = 'text=!!!!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('=== Header ===', result)

    def test_should_convert_to_h5(self):
        """ this is a test """
        line = 'text=\n!!!!!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n== Header ==', result)
        line = 'text=!!!!!Header'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('== Header ==', result)

    def test_should_convert_to_order_list1(self):
        """ this is a test """
        line = 'text=\n#list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n  - list', result)
        line = 'text=#list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('  - list', result)

    def test_should_convert_to_order_list2(self):
        """ this is a test """
        line = 'text=\n##list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n    - list', result)
        line = 'text=##list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('    - list', result)

    def test_should_convert_to_order_list3(self):
        """ this is a test """
        line = 'text=\n###list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n      - list', result)
        line = 'text=###list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('      - list', result)

    def test_should_convert_to_order_list4(self):
        """ this is a test """
        line = 'text=\n####list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n        - list', result)
        line = 'text=####list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('        - list', result)

    def test_should_convert_to_order_list5(self):
        """ this is a test """
        line = 'text=\n#####list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n          - list', result)
        line = 'text=#####list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('          - list', result)


    def test_should_convert_to_unorder_list1(self):
        """ this is a test """
        line = 'text=\n*list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n  * list', result)

    def test_should_convert_to_unorder_list2(self):
        """ this is a test """
        line = 'text=\n**list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n    * list', result)

    def test_should_convert_to_unorder_list3(self):
        """ this is a test """
        line = 'text=\n***list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n      * list', result)

    def test_should_convert_to_unorder_list4(self):
        """ this is a test """
        line = 'text=\n****list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n        * list', result)

    def test_should_convert_to_unorder_list5(self):
        """ this is a test """
        line = 'text=\n*****list'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n          * list', result)

    def test_should_convert_to_bold_italic(self):
        """ this is a test """
        line = "text='''''text'''''"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('**//text//**', result)

    def test_should_convert_to_bold(self):
        """ this is a test """
        line = "text='''text'''"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('**text**', result)

    def test_should_convert_to_italic(self):
        """ this is a test """
        line = "text=''text''"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('//text//', result)

    def test_should_convert_to_strike(self):
        """ this is a test """
        line = 'text={-text-}'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('<del>text</del>', result)

    def test_should_convert_to_underline(self):
        """ this is a test """
        line = 'text={+text+}'
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('__text__', result)

    def test_should_convert_to_subscript(self):
        """ this is a test """
        line = "text='_text_'"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('<sub>text</sub>', result)

    def test_should_convert_to_superscript(self):
        """ this is a test """
        line = "text='^text^'"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('<sub>text</sub>', result)

    def test_should_convert_to_monoscript(self):
        """ this is a test """
        line = "text=@@text@@"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("''text''", result)

    def test_should_convert_to_question_answer(self):
        """ this is a test """
        line = "text=Q:text"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\\ :?:text', result)
        line = "text=R:text"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\\ :!:text', result)

    def test_should_convert_to_code(self):
        """ this is a test """
        line = "text=[@text@]"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("<code>text</code>", result)

    def test_should_convert_table(self):
        """ this is a test """
        line = "text=\n||Border=1\n"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("\n", result)
        line = "text=||! Table Title !||"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("^ Table Title ", result)
        line = "text=||!Cell heading"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("^Cell heading", result)
        line = "text=||!Cell heading||!Cell heading||!Cell heading"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("^Cell heading^Cell heading^Cell heading", result)
        line = "text=|| Cell ||"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("| Cell |", result)

    def test_should_convert_to_link(self):
        """ this is a test """
        line = "text=[[link|text]]"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("[[link|text]]", result)

    def test_should_remove_trails(self):
        """ this is a test """
        line = "text=%3c|[[TrailPage]]|>"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('', result)
        line = "text=%3c|[[Trail.Page]]|>"
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('', result)


    def test_should_remove_border_table(self):
        """ this is a test """
        line = "text=%0a%0a||Border=1%0a||! Heading "
        result = self.dokuwiki_convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n\n^ Heading ', result)

if __name__ == '__main__':
    unittest.main()
