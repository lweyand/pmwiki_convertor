#!/usr/bin/python
""" this is a test suite on MakdownConvertor class"""

import unittest
from convertors import MarkdownConvertor


class MarkdownConvertorTest(unittest.TestCase):
    """ this is a test class suite on MakdownConvertor class"""

    convertor = MarkdownConvertor()

    def test_should_extract_text(self):
        """ this is a test """
        line = 'text=this the text to extract'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('this the text to extract', result)

    def test_should_convert_to_linebreak(self):
        """ this is a test """
        line = 'text=foo%0abar'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('foo\nbar', result)

    def test_should_convert_to_percent(self):
        """ this is a test """
        line = 'text=foo%25bar'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('foo%bar', result)

    def test_should_convert_to_h1(self):
        """ this is a test """
        line = 'text=\n!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n# Header', result)
        line = 'text=!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('# Header', result)

    def test_should_convert_to_h2(self):
        """ this is a test """
        line = 'text=\n!!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n## Header', result)
        line = 'text=!!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('## Header', result)

    def test_should_convert_to_h3(self):
        """ this is a test """
        line = 'text=\n!!!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n### Header', result)
        line = 'text=!!!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('### Header', result)

    def test_should_convert_to_h4(self):
        """ this is a test """
        line = 'text=\n!!!!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n#### Header', result)
        line = 'text=!!!!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('#### Header', result)

    def test_should_convert_to_h5(self):
        """ this is a test """
        line = 'text=\n!!!!!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n##### Header', result)
        line = 'text=!!!!!Header'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('##### Header', result)

    def test_should_convert_to_order_list1(self):
        """ this is a test """
        line = 'text=\n#list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n1. list', result)
        line = 'text=#list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('1. list', result)

    def test_should_convert_to_order_list2(self):
        """ this is a test """
        line = 'text=\n##list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n    1. list', result)
        line = 'text=##list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('    1. list', result)

    def test_should_convert_to_order_list3(self):
        """ this is a test """
        line = 'text=\n###list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n        1. list', result)
        line = 'text=###list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('        1. list', result)

    def test_should_convert_to_order_list4(self):
        """ this is a test """
        line = 'text=\n####list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n            1. list', result)
        line = 'text=####list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('            1. list', result)

    def test_should_convert_to_order_list5(self):
        """ this is a test """
        line = 'text=\n#####list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n                1. list', result)
        line = 'text=#####list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('                1. list', result)


    def test_should_convert_to_unorder_list1(self):
        """ this is a test """
        line = 'text=\n*list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n* list', result)

    def test_should_convert_to_unorder_list2(self):
        """ this is a test """
        line = 'text=\n**list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n    * list', result)

    def test_should_convert_to_unorder_list3(self):
        """ this is a test """
        line = 'text=\n***list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n        * list', result)

    def test_should_convert_to_unorder_list4(self):
        """ this is a test """
        line = 'text=\n****list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n            * list', result)

    def test_should_convert_to_unorder_list5(self):
        """ this is a test """
        line = 'text=\n*****list'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n                * list', result)

    def test_should_convert_to_bold_italic(self):
        """ this is a test """
        line = "text='''''text'''''"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('***text***', result)

    def test_should_convert_to_bold(self):
        """ this is a test """
        line = "text='''text'''"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('**text**', result)

    def test_should_convert_to_italic(self):
        """ this is a test """
        line = "text=''text''"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('*text*', result)

    def test_should_convert_to_strike(self):
        """ this is a test """
        line = 'text={-text-}'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('~~text~~', result)

    def test_should_remove_underline(self):
        """ this is a test """
        line = 'text={+text+}'
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('text', result)

    def test_should_remove_subscript(self):
        """ this is a test """
        line = "text='_text_'"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('text', result)

    def test_should_remove_superscript(self):
        """ this is a test """
        line = "text='^text^'"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('text', result)

    def test_should_convert_to_monoscript(self):
        """ this is a test """
        line = "text=@@text@@"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("```text```", result)

    def test_should_convert_to_question_answer(self):
        """ this is a test """
        line = "text=Q:text"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('Question: text', result)
        line = "text=R:text"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('Answer: text', result)

    def test_should_convert_to_code(self):
        """ this is a test """
        line = "text=[@text@]"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("```\ntext\n```", result)

    def test_should_convert_table(self):
        """ this is a test """
        line = "text=\n||Border=1\n"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("\n", result)
        line = "text=||! Table Title !||"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("| Table Title |", result)
        line = "text=||!Cell heading"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("|Cell heading", result)
        line = "text=||!Cell heading||!Cell heading||!Cell heading"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("|Cell heading|Cell heading|Cell heading", result)
        line = "text=|| Cell ||"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("| Cell |", result)

    def test_should_convert_to_link(self):
        """ this is a test """
        line = "text=[[http://link|text]]"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("[text](http://link)", result)

    def test_should_convert_to_iternal_link(self):
        """ this is a test """
        line = "text=[[Namespace/Page]]"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("[page](namespace/page)", result)

        line = "text=[[Namespace/Page|text]]"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("[text](namespace/page)", result)

    def test_should_remove_trails(self):
        """ this is a test """
        line = "text=%3c|[[TrailPage]]|>"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('', result)
        line = "text=%3c|[[Trail.Page]]|>"
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('', result)


    def test_should_remove_border_table(self):
        """ this is a test """
        line = "text=%0a%0a||Border=1%0a||! Heading "
        result = self.convertor.convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n\n| Heading ', result)

if __name__ == '__main__':
    unittest.main()
