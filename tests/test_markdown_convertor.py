#!/usr/bin/python
""" this is a test suite on MakdownConvertor class"""

import unittest
from convertors import MarkdownConvertor


class MarkdownConvertorTest(unittest.TestCase):
    """ this is a test class suite on MakdownConvertor class"""

    convertor = MarkdownConvertor()


    def _convert_line(self, line, current_namespace=None):
        return self.convertor.convert_line(line, current_namespace)

    def test_should_extract_text(self):
        """ this is a test """
        line = 'text=this the text to extract'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('this the text to extract', result)

    def test_should_convert_to_linebreak(self):
        """ this is a test """
        line = 'text=foo%0abar'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('foo\nbar', result)

    def test_should_convert_to_percent(self):
        """ this is a test """
        line = 'text=foo%25bar'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('foo%bar', result)

    def test_should_convert_to_h1(self):
        """ this is a test """
        line = 'text=\n!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n# Header', result)
        line = 'text=!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('# Header', result)

    def test_should_convert_to_h2(self):
        """ this is a test """
        line = 'text=\n!!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n## Header', result)
        line = 'text=!!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('## Header', result)

    def test_should_convert_to_h3(self):
        """ this is a test """
        line = 'text=\n!!!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n### Header', result)
        line = 'text=!!!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('### Header', result)

    def test_should_convert_to_h4(self):
        """ this is a test """
        line = 'text=\n!!!!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n#### Header', result)
        line = 'text=!!!!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('#### Header', result)

    def test_should_convert_to_h5(self):
        """ this is a test """
        line = 'text=\n!!!!!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n##### Header', result)
        line = 'text=!!!!!Header'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('##### Header', result)

    def test_should_not_convert_exclamation_mark(self):
        """ this is a test """
        line = 'text=\nNot Header!! Sir'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\nNot Header!! Sir', result)

    def test_should_convert_to_order_list1(self):
        """ this is a test """
        line = 'text=\n#list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n1. list', result)
        line = 'text=#list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('1. list', result)

    def test_should_convert_to_order_list2(self):
        """ this is a test """
        line = 'text=\n##list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n    1. list', result)
        line = 'text=##list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('    1. list', result)

    def test_should_convert_to_order_list3(self):
        """ this is a test """
        line = 'text=\n###list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n        1. list', result)
        line = 'text=###list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('        1. list', result)

    def test_should_convert_to_order_list4(self):
        """ this is a test """
        line = 'text=\n####list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n            1. list', result)
        line = 'text=####list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('            1. list', result)

    def test_should_convert_to_order_list5(self):
        """ this is a test """
        line = 'text=\n#####list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n                1. list', result)
        line = 'text=#####list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('                1. list', result)


    def test_should_convert_to_unorder_list1(self):
        """ this is a test """
        line = 'text=\n*list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n* list', result)

    def test_should_convert_to_unorder_list2(self):
        """ this is a test """
        line = 'text=\n**list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n    * list', result)

    def test_should_convert_to_unorder_list3(self):
        """ this is a test """
        line = 'text=\n***list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n        * list', result)

    def test_should_convert_to_unorder_list4(self):
        """ this is a test """
        line = 'text=\n****list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n            * list', result)

    def test_should_convert_to_unorder_list5(self):
        """ this is a test """
        line = 'text=\n*****list'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n                * list', result)

    def test_should_convert_to_bold_italic(self):
        """ this is a test """
        line = "text='''''text'''''"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('***text***', result)

    def test_should_convert_to_bold(self):
        """ this is a test """
        line = "text='''text'''"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('**text**', result)

    def test_should_convert_to_italic(self):
        """ this is a test """
        line = "text=''text''"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('*text*', result)

    def test_should_convert_to_strike(self):
        """ this is a test """
        line = 'text={-text-}'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('~~text~~', result)

    def test_should_remove_underline(self):
        """ this is a test """
        line = 'text={+text+}'
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('text', result)

    def test_should_remove_subscript(self):
        """ this is a test """
        line = "text='_text_'"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('text', result)

    def test_should_remove_superscript(self):
        """ this is a test """
        line = "text='^text^'"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('text', result)

    def test_should_convert_to_monoscript(self):
        """ this is a test """
        line = "text=@@text@@"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("```text```", result)

    def test_should_convert_to_question_answer(self):
        """ this is a test """
        line = "text=Q:text"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('Question: text', result)
        line = "text=R:text"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('Answer: text', result)

    def test_should_convert_to_code(self):
        """ this is a test """
        line = "text=[@text@]"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("```\ntext\n```", result)

    def test_should_convert_table(self):
        """ this is a test """
        line = "text=\n||Border=1\n"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("\n", result)
        line = "text=||! Table Title !||"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("| Table Title |", result)
        line = "text=||!Cell heading"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("|Cell heading", result)
        line = "text=||!Cell heading||!Cell heading||!Cell heading"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("|Cell heading|Cell heading|Cell heading", result)
        line = "text=|| Cell ||"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("| Cell |", result)

    def test_should_convert_to_link(self):
        """ this is a test """
        line = "text=[[http://link|text]]"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("[text](http://link)", result)

    def test_should_convert_to_iternal_link(self):
        """ this is a test """
        line = "text=[[Namespace/Page]]"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("[page](namespace/page)", result)

        line = "text=[[Namespace/Page|text]]"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual("[text](namespace/page)", result)

    def test_should_remove_trails(self):
        """ this is a test """
        line = "text=%3c|[[TrailPage]]|>"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('', result)

    def test_should_remove_trails_with_namespace1(self):
        line = "text=%3c|[[Trail.Page]]|>"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('', result)

    def test_should_remove_trails_with_namespace2(self):
        line = "text=%3c|[[Trail/Page]]|>"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('', result)

    def test_should_remove_trails_with_namespace3(self):
        line = "text=%25trail%25 %3c|[[Main.Page]]|>%0a%0a"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual(' \n\n', result)


    def test_should_remove_border_table(self):
        """ this is a test """
        line = "text=%0a%0a||Border=1%0a||! Heading "
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('\n\n| Heading ', result)


    def test_should_convert_syntax1_attachments_with_caption(self):
        """ this is a test """
        line = "text=[[(Attach:)file.ext|txt]] "
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![txt](../media/file.ext) ', result)


    def test_should_convert_syntax1_attachments(self):
        line = "text=[[(Attach:)file.ext]] "
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![file](../media/file.ext) ', result)

    def test_should_convert_syntax1_attachments_with_single_namespace(self):
        line = "text=[[(Attach:)Namespace/File.ext]] "
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![File](../media/namespace/File.ext) ', result)

    def test_should_convert_syntax1_attachments_with_namespace_and_current_file_namespace(self):
        line = "text=[[(Attach:)Namespace/File.ext]] "
        result = self._convert_line(line, 'other_NameSpace')
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![File](../media/namespace/File.ext) ', result)

    def test_should_convert_syntax1_attachments_with_current_file_namespace(self):
        line = "text=[[(Attach:)file.ext]] "
        result = self._convert_line(line, 'other_NameSpace')
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![file](../media/other_namespace/file.ext) ', result)

    def test_should_convert_syntax1_attachments_with_multi_namespace(self):
        line = "text=[[(Attach:)Ns1/Ns2/file.ext]] "
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![file](../media/ns1/ns2/file.ext) ', result)

    def test_should_convert_syntax2_attachments(self):
        line = "text=[[Attach:file.ext]] "
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![file](../media/file.ext) ', result)

    def test_should_convert_syntax2_attachments_with_caption(self):
        line = "text=[[Attach:file.ext|txt]] "
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![txt](../media/file.ext) ', result)

    def test_should_convert_syntax13_attachments(self):
        line = "text=Attach:file.ext "
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('![file](../media/file.ext) ', result)

    def test_should_add_new_line(self):
        line = "text=text1\\text2"
        result = self._convert_line(line)
        self.assertIsNotNone(result, "result is None")
        self.assertEqual('text1\ntext2', result)

if __name__ == '__main__':
    unittest.main()
