This python script is based on the [perl one](https://forum.dokuwiki.org/thread/3895) from Jason Cameron.

# Requirement:

Python3

# Usage

```
usage: pmwiki_convertor.py [-h] [--file FILE | --directory DIRECTORY]
                           [--output OUTPUT] [--convertor CONVERTOR]

pmwiki file converter

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           a file to convert
  --directory DIRECTORY
                        directory containing PmWiki backup files
  --output OUTPUT       directory output to write converted files
  --convertor CONVERTOR
                        convertor type: dokuwiki (default), markdown
```


## Examples

This is a typical PmWiki directory layout that need to be converted:
```bash
Pmwiki
├── uploads
|   └── namespace
|       └── media files
└── wiki.d
    └── namespace
        └── wiki files
```
* *uploads* directory contains all media files uploaded in pages, like pictures, pdf, ...
* *wiki.d* directory contains all the wiki files

### Convert a file to md:

```bash
python pmwiki_convertor.py --file wiki.d/Linux.Debian --output markdown --convertor markdown
```

Output Markdown directory layout:
```bash
output directory
├── media
|   └── namespace
|       └── media files
└── namespace
    └── mardown files
```
The pmwiki uploaded files will be copy to *output directory/media* directory.
The pmwiki wiki files will be converted to markdown in *output directory*. And all the link
to media files will be converted to point to right media files.

### Convert files in a directory to dokuwiki files:

```bash
python pmwiki_convertor.py --directory wiki.d --output dokuwiki
```

Output DokuWiki directory layout:
```bash
output directory
└── data
    ├── media
    |   └── namespace
    |       └── media files
    └── pages
        └── namespace
            └── wiki files
```
The pmwiki uploaded files will be copy to *output directory/data/media* directory.
The pmwiki wiki files will be converted to dokuwiki syntax in *output directory/data/pages*. And all the link
to media files will be converted to point to right media files.

# What it does:

This script only convert pmwiki files to dokuwiki files or markdown files.

This script will do:
* create output directory
* convert pmwiki namespaces to directory. For example page with name like **Linux.Debian**
    will be converted to a directory named **linux** (lowercase) that will contain
    a file named **debian.txt** (lowercase)
* convert the content, only the *text=* line, to the target convertor.

# What it does not:

It will not convert a pmwiki database content.
