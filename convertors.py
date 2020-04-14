#!/usr/bin/python
""" Convertors Modules """
import abc
import re

class ConvertorInterface(metaclass=abc.ABCMeta):
    """
    Convertor interface for all convertors implementations.
    """
    @abc.abstractmethod
    def get_output_filename(self, filename) -> str:
        """
        Should return the output file name with extension

        Keyword arguments:
        filename -- the file name without extension
        """
        pass

    @abc.abstractmethod
    def convert_line(self, line) -> str:
        """
        Should return the input string line converted to the convertors format

        Keyword arguments:
        line -- the pmwiki file line to convert
        """
        pass

class DokuwikiConvertor(ConvertorInterface):
    """ Dokuwiki syntax convertor """
    def __init__(self):
        self.file_ext = '.txt'

    def get_output_filename(self, filename):
        """ Return the dokuwiki filename """
        return filename+self.file_ext

    def convert_line(self, line):
        """ convert the input line to dokuwiki syntax """
        converted = None
        if re.match("^text=", line):
            converted = line
            converted = re.sub("^text=", "", converted)
            # Replaces linebreaks with nothing
            converted = re.sub("%0a", "\n", converted)
            # Reencode %25 to %
            converted = re.sub("%25", "%", converted)

            # # Table Creations
            converted = re.sub("\\|{2}Border(.*)\n", "", converted, flags=re.IGNORECASE)
            converted = re.sub("\\|{2}\\!", "^", converted)
            converted = re.sub("\\!\\|{2}", "", converted)
            converted = re.sub("\\|{2}", "|", converted)

            # # Header Substitutions
            converted = re.sub("(\n)?!{5}(.*)", r"\1== \2 ==", converted)
            converted = re.sub("(\n)?!{4}(.*)", r"\1=== \2 ===", converted)
            converted = re.sub("(\n)?!{3}(.*)", r"\1==== \2 ====", converted)
            converted = re.sub("(\n)?!{2}(.*)", r"\1===== \2 =====", converted)
            converted = re.sub("(\n)?!(.*)", r"\1====== \2 ======", converted)
            converted = re.sub("\\(:title (.*)\\s?:\\)", r"\n====== \1 ======", converted)

            # # Order Lists (up to 5)
            converted = re.sub("(\n)?\\#{5}(.*)", r"\1          - \2", converted)
            converted = re.sub("(\n)?\\#{4}(.*)", r"\1        - \2", converted)
            converted = re.sub("(\n)?\\#{3}(.*)", r"\1      - \2", converted)
            converted = re.sub("(\n)?\\#{2}(.*)", r"\1    - \2", converted)
            converted = re.sub("(\n)?\\#{1}(.*)", r"\1  - \2", converted)

            # # Unordered Lists (up to 5)
            converted = re.sub("(\n)\\*{5}(.*)", r"\1          * \2", converted)
            converted = re.sub("(\n)\\*{4}(.*)", r"\1        * \2", converted)
            converted = re.sub("(\n)\\*{3}(.*)", r"\1      * \2", converted)
            converted = re.sub("(\n)\\*{2}(.*)", r"\1    * \2", converted)
            converted = re.sub("(\n)\\*{1}(.*)", r"\1  * \2", converted)

            # # Bold + Italic
            converted = re.sub("\\'{5}(.*)\\'{5}", r"**//\1//**", converted)

            # # Bold (done after unordered)
            converted = re.sub("\\'{3}", "**", converted)

            # # Italic
            # $theline =~ s/\`~/\/\//g;
            # converted = re.sub("\`~", "//", converted)
            # $theline =~ s/~\'/\/\//g;
            # converted = re.sub("~\'", "//", converted)
            # $theline =~ s/\'{2}/\/\//g;
            converted = re.sub("\\'{2}", "//", converted)

            # # Striked Through
            converted = re.sub("{-", "<del>", converted)
            converted = re.sub("-}", "</del>", converted)

            # # Underline
            converted = re.sub("{\\+", "__", converted)
            converted = re.sub("\\+}", "__", converted)

            # # Subscript
            converted = re.sub("\\'_", "<sub>", converted)
            converted = re.sub("_\\'", "</sub>", converted)

            # # Superscript
            converted = re.sub("\\'\\^", "<sub>", converted)
            converted = re.sub("\\^\\'", "</sub>", converted)

            # # MonoScript (done after italic)
            converted = re.sub("@@", "\'\'", converted)

            # # Questions/Answers
            converted = re.sub("Q:", "\\ :?:", converted)
            converted = re.sub("R:", "\\ :!:", converted)

            # # [@ to <code> and @] to </code> for non-rendering syntax
            converted = re.sub("\\[\\@", "<code>", converted)
            converted = re.sub("\\@\\]", "</code>", converted)

            # # Remove (:cell:)&(:cellnr:)&(:tableend:)&(:table:)
            converted = re.sub("\\(\\:cell.*\\:\\)", "", converted)
            converted = re.sub("\\(\\:cellnr.*\\:\\)", "", converted)
            converted = re.sub("\\(\\:tableend.*\\:\\)", "", converted)
            converted = re.sub("\\(\\:table.*\\:\\)", "", converted)

            # # Adding newlines
            converted = re.sub("\\{1}", "\\\\", converted)

            # # Remove %enclosedstuffs%
            converted = re.sub("%.*%", "", converted)

            # Remove trails <|[[\w]]|>
            converted = re.sub("%3c\\|\\[\\[([a-zA-Z0-9_.])*\\]\\]\\|>", "", converted)

            # links syntax pmwiki = dokuwiki
            # horizontal line syntax pmwiki = dokuwiki

        return converted


class MarkdownConvertor(ConvertorInterface):
    """ Markdown syntax convertor """
    def __init__(self):
        self.file_ext = '.md'

    def get_output_filename(self, filename):
        """ Return the markdown filename """
        return filename+self.file_ext

    def convert_line(self, line):
        """ convert the input line to markdown syntax """
        converted = None
        if re.match("^text=", line):
            converted = line
            converted = re.sub("^text=", "", converted)
            # Replaces linebreaks with nothing
            converted = re.sub("%0a", "\n", converted)
            # Reencode %25 to %
            converted = re.sub("%25", "%", converted)

            # # Table Creations
            converted = re.sub("\\|{2}Border(.*)\n", "", converted, flags=re.IGNORECASE)
            converted = re.sub("\\|{2}\\!", "|", converted)
            converted = re.sub("\\!\\|{2}", "|", converted)
            converted = re.sub("\\|{2}", "|", converted)

            # # Order Lists (up to 5)
            converted = re.sub("(\n)?\\#{5}(.*)", r"\1                1. \2", converted)
            converted = re.sub("(\n)?\\#{4}(.*)", r"\1            1. \2", converted)
            converted = re.sub("(\n)?\\#{3}(.*)", r"\1        1. \2", converted)
            converted = re.sub("(\n)?\\#{2}(.*)", r"\1    1. \2", converted)
            converted = re.sub("(\n)?\\#{1}(.*)", r"\g<1>1. \g<2>", converted)

            # # Header Substitutions
            converted = re.sub("(\n)?!{5}(.*)", r"\1##### \2", converted)
            converted = re.sub("(\n)?!{4}(.*)", r"\1#### \2", converted)
            converted = re.sub("(\n)?!{3}(.*)", r"\1### \2", converted)
            converted = re.sub("(\n)?!{2}(.*)", r"\1## \2", converted)
            converted = re.sub("(\n)?!(.*)", r"\1# \2", converted)
            converted = re.sub("\\(:title (.*)\\s?:\\)", r"\n# \1", converted)

            # # Unordered Lists (up to 5)
            converted = re.sub("(\n)\\*{5}(.*)", r"\1                * \2", converted)
            converted = re.sub("(\n)\\*{4}(.*)", r"\1            * \2", converted)
            converted = re.sub("(\n)\\*{3}(.*)", r"\1        * \2", converted)
            converted = re.sub("(\n)\\*{2}(.*)", r"\1    * \2", converted)
            converted = re.sub("(\n)\\*{1}(.*)", r"\1* \2", converted)

            # # Bold + Italic
            converted = re.sub("\\'{5}(.*)\\'{5}", r"***\1***", converted)

            # # Bold (done after unordered)
            converted = re.sub("\\'{3}", "**", converted)

            # # Italic
            # $theline =~ s/\`~/\/\//g;
            # converted = re.sub("\`~", "//", converted)
            # $theline =~ s/~\'/\/\//g;
            # converted = re.sub("~\'", "//", converted)
            # $theline =~ s/\'{2}/\/\//g;
            converted = re.sub("\\'{2}", "*", converted)

            # # Striked Through
            converted = re.sub("{-", "~~", converted)
            converted = re.sub("-}", "~~", converted)

            # # Underline
            converted = re.sub("{\\+", "", converted)
            converted = re.sub("\\+}", "", converted)

            # # Subscript
            converted = re.sub("\\'_", "", converted)
            converted = re.sub("_\\'", "", converted)

            # # Superscript
            converted = re.sub("\\'\\^", "", converted)
            converted = re.sub("\\^\\'", "", converted)

            # # MonoScript (done after italic)
            converted = re.sub("@@", "```", converted)

            # # Questions/Answers
            converted = re.sub("Q:", "Question: ", converted)
            converted = re.sub("R:", "Answer: ", converted)

            # # [@ to <code> and @] to </code> for non-rendering syntax
            converted = re.sub("\\[\\@", "```\n", converted)
            converted = re.sub("\\@\\]", "\n```", converted)

            # # Remove (:cell:)&(:cellnr:)&(:tableend:)&(:table:)
            converted = re.sub("\\(\\:cell.*\\:\\)", "", converted)
            converted = re.sub("\\(\\:cellnr.*\\:\\)", "", converted)
            converted = re.sub("\\(\\:tableend.*\\:\\)", "", converted)
            converted = re.sub("\\(\\:table.*\\:\\)", "", converted)

            # # Adding newlines
            converted = re.sub("\\{1}", "\n\n", converted)

            # # Remove %enclosedstuffs%
            converted = re.sub("%.*%", "", converted)

            # Remove trails <|[[\w]]|>
            converted = re.sub("%3c\\|\\[\\[([a-zA-Z0-9_.])*\\]\\]\\|>", "", converted)

            # links syntax [[link|text]] -> [text](link)
            converted = re.sub("\\[\\[http(.*)\\|(.*)\\]\\]", r"[\2](http\1)", converted)
            converted = re.sub("\\[\\[(.*)/(.*)\\|(.*)\\]\\]", self._to_internal_link, converted)
            converted = re.sub("\\[\\[(.*)/(.*)\\]\\]", self._to_internal_link, converted)
            # converted = re.sub("\[\[(.*)/(.*)\]\]", r"[\1 \2](\1/\2)", converted)

            # horizontal line syntax pmwiki = markdown

        return converted

    @staticmethod
    def _to_internal_link(match):
        """ convert pmwiki internal link to markdown link """
        if match.lastindex == 3:
            text = match.group(3)
        else:
            text = match.group(2)
        return "[{0}]({1}/{2})".format(text.lower(), match.group(1).lower(), match.group(2).lower())
