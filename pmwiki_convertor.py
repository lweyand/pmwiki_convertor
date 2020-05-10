#!/usr/bin/python
import os
import sys
import argparse
from shutil import copyfile

import convertors

SKIP_FILENAMES = ['recentchanges', 'allrecentchanges', 'sidebar', 'status',
                  'recentuploads', 'flock', 'htaccess', 'lastmod', 'linkindex',
                  'pageindex']
WIKI_FILES_DIR = 'wiki.d'
WIKI_ATTACHMENTS_DIR = 'uploads'


def normalize(string):
    """
    normalise string to lowercase
    """
    return string.lower()


def get_files(base):
    """
    list all the files in dir
    """
    files = os.listdir(base)
    return files


def get_media_files(base):
    fullpath_files = []
    for path, subdirs, files in os.walk(base):
        for name in files:
            fullpath_files.append(os.path.join(path, name).replace(base+os.path.sep, ''))
    return fullpath_files


def extract_dir_and_file(wiki_file):
    """
    convert pmwiki file name to a directory and a file
    """
    (wiki_dir, wiki_file) = wiki_file.split(".", 1)
    return  (normalize(wiki_dir), normalize(wiki_file))


def extract_dir_and_media(media_file):
    """
    convert pmwiki file name to a directory and a file
    """

    source_ns = normalize(os.path.dirname(media_file))
    source_file = os.path.basename(media_file)
    return  (source_ns, source_file)


def create_directory(dirname):
    """
    create directory
    """
    path = dirname
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)


def get_convertor(convertor_type):
    """
    return convertor class
    """
    convertor = None
    if convertor_type == 'markdown':
        convertor = convertors.MarkdownConvertor()
    else:
        convertor = convertors.DokuwikiConvertor()
    return convertor


def convert_file(output_base_dir, output_namespace_dir, output_file, wiki_file, convertor):
    """
    convert the content of a file to the desired format.

    Keyword arguments:
    output_base_dir -- where to write file
    output_namespace_dir -- wiki namespace dir
    output_file -- the file name (with no extension)
    wiki_file -- the filename of the pmwiki file to convert
    convertor -- the instance of a convertor
    """
    output_file = open(
        os.path.join(
            output_base_dir,
            convertor.get_pages_path(),
            output_namespace_dir,
            convertor.get_output_filename(output_file)),
        "w")
    for line in wiki_file:
        converted_line = convertor.convert_line(line, output_namespace_dir)
        if converted_line is not None:
            output_file.write(converted_line)


def convert_files(directory, files, output, convertor):
    """
    convert a files list to the desired format.

    Keyword arguments:
    directory -- the directory where are located pmwiki files
    files -- pmwiki filenames list
    output -- the directory where to write converted files
    convertor -- the instance of a convertor
    """
    for filename in files:
        (output_namespace_dir, output_file) = extract_dir_and_file(filename)

        if output_file not in SKIP_FILENAMES:
            create_directory(os.path.join(output, convertor.get_pages_path()))
            create_directory(os.path.join(output, convertor.get_pages_path(), output_namespace_dir))

            pmwiki_file = open(os.path.join(directory, filename), "r", encoding="ISO-8859-1")
            convert_file(
                output,
                output_namespace_dir,
                output_file,
                pmwiki_file,
                convertor)


def convert_attachments(directory, files, output, convertor):
    """
    Copy all attached files to the directory.

    Keyword arguments:
    directory -- the base directory where are located the attached files
    files -- attached filenames list (include namespace dir)
    output -- the directory where to write converted files
    convertor -- the instance of a convertor
    """
    for filename in files:
        (output_namespace_dir, output_file) = extract_dir_and_media(filename)
        create_directory(os.path.join(output, convertor.get_media_path()))
        create_directory(os.path.join(output, convertor.get_media_path(), output_namespace_dir))

        src_media_path = os.path.join(directory, filename)
        trg_media_path = os.path.join(output, convertor.get_media_path(), output_namespace_dir, output_file)
        copyfile(src_media_path, trg_media_path)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='pmwiki file converter')
    GROUP = PARSER.add_mutually_exclusive_group()
    GROUP.add_argument('--file', type=str,
                       help='a file to convert')
    GROUP.add_argument('--directory', type=str,
                       help='directory containing PmWiki backup files')
    PARSER.add_argument('--output', type=str,
                        help='directory output to write converted files')
    PARSER.add_argument('--convertor', type=str,
                        help='convertor type: dokuwiki (default), markdown',
                        default='dokuwiki')
    ARGS = PARSER.parse_args()

    if ARGS.file:
        convert_files(
            os.path.dirname(ARGS.file),
            [os.path.basename(ARGS.file)],
            ARGS.output,
            ARGS.convertor)
    elif ARGS.directory:
        WIKI_FILES = get_files(os.path.join(ARGS.directory, WIKI_FILES_DIR))
        ATTACHMENT_FILES = get_media_files(os.path.join(ARGS.directory, WIKI_ATTACHMENTS_DIR))
        CONVERTOR = get_convertor(ARGS.convertor)
        convert_files(
            ARGS.directory+WIKI_FILES_DIR,
            WIKI_FILES,
            ARGS.output,
            CONVERTOR)
        convert_attachments(
            ARGS.directory+WIKI_ATTACHMENTS_DIR,
            ATTACHMENT_FILES,
            ARGS.output,
            CONVERTOR)
    else:
        PARSER.print_help()
        sys.exit(1)
