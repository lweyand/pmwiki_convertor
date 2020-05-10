#!/usr/bin/python
import unittest
import pmwiki_convertor
import convertors


class PmWikiConvertorTest(unittest.TestCase):
    """ this is a test class suite on pmwiki_convertor main"""

    def test_should_return_files_list(self):
        files = pmwiki_convertor.get_files('tests/filesdir')
        self.assertIsNotNone(files, 'files is None')
        self.assertListEqual(['file.txt'], files)

    def test_should_return_files_list(self):
        files = pmwiki_convertor.get_media_files('tests/mediasdir')
        self.assertIsNotNone(files, 'files is None')
        self.assertListEqual(['namespacedir/media.txt'], files)

    def test_should_return_markdown_convertor(self):
        convertor = pmwiki_convertor.get_convertor('markdown')
        self.assertIsNotNone(convertor, 'convertor is None')
        isinstance(convertor, convertors.MarkdownConvertor)


    def test_should_return_dokuwiki_convertor(self):
        convertor = pmwiki_convertor.get_convertor('dokuwiki')
        self.assertIsNotNone(convertor, 'convertor is None')
        isinstance(convertor, convertors.DokuwikiConvertor)


    def test_should_return_default_convertor(self):
        convertor = pmwiki_convertor.get_convertor(None)
        self.assertIsNotNone(convertor, 'convertor is None')
        isinstance(convertor, convertors.DokuwikiConvertor)
