#!/usr/bin/python
import os
import sys
import argparse

import convertors

SKIP_FILENAMES = ['recentchanges', 'allrecentchanges', 'sidebar', 'status', 'recentuploads']

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

def extract_dir_and_file(wiki_file):
    """
    convert pmwiki file name to a directory and a file
    """
    (wiki_dir, wiki_file) = wiki_file.split(".", 1)
    return  (normalize(wiki_dir), normalize(wiki_file))

def create_directory(dirname):
    """
    create directory
    """
    path = dirname
    if not os.path.exists(path):
        try:
            os.mkdir(path)
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

def convert_file(output_path, output_file, wiki_file, convertor_type):
    """
    convert the content of a file to the desired format.

    Keyword arguments:
    output_path -- where to write file
    output_file -- the file name (with no extension)
    wiki_file -- the filename of the pmwiki file to convert
    convertor_type -- the type of convertor
    """
    convertor = get_convertor(convertor_type)
    output_file = open(os.path.join(output_path, convertor.get_output_filename(output_file)), "w")
    for line in wiki_file:
        converted_line = convertor.convert_line(line)
        if converted_line is not None:
            output_file.write(converted_line)


def convert_files(directory, files, output, convertor_type):
    """
    convert a files list to the desired format.

    Keyword arguments:
    directory -- the directory where are located pmwiki files
    files -- pmwiki filenames list
    output -- the directory where to write converted files
    convertor_type  -- the type of convertor
    """
    for filename in files:
        (output_file_dir, output_file) = extract_dir_and_file(filename)

        if output_file not in SKIP_FILENAMES:
            create_directory(output)
            create_directory(os.path.join(output, output_file_dir))

            pmwiki_file = open(os.path.join(directory, filename), "r", encoding="ISO-8859-1")
            convert_file(
                os.path.join(output, output_file_dir),
                output_file,
                pmwiki_file,
                convertor_type)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='pmwiki file converter')
    GROUP = PARSER.add_mutually_exclusive_group()
    GROUP.add_argument('--file', type=str,
                       help='a file to convert')
    GROUP.add_argument('--directory', type=str,
                       help='directory containing files to convert')
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
        WIKI_FILES = get_files(ARGS.directory)
        convert_files(
            ARGS.directory,
            WIKI_FILES,
            ARGS.output,
            ARGS.convertor)
    else:
        PARSER.print_help()
        sys.exit(1)
