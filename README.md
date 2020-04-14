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
                        directory containing files to convert
  --output OUTPUT       directory output to write converted files
  --convertor CONVERTOR
                        convertor type: dokuwiki (default), markdown
```


## Examples

### Convert a file to md:

```bash
python pmwiki_convertor.py --file wiki.d/Linux.Debian --output markdown --convertor markdown
```

### Convert files in a directory to dokuwiki files:

```bash
python pmwiki_convertor.py --directory wiki.d --output dokuwiki
```

# What it does:

This script only convert pmwiki files to dokuwiki files or markdown files.

This script will do:
* create output directory
* convert pmwiki namespaces to directory. For example page with name like **Linux.Debian**
    will be converted to a directory named **linux** (lowercase) that will contain 
    a file named **debian.txt** (lowercase)
* convert the content, only the *text=* line, to the target convertor.

# What it does not:

It will not convert a  pmwiki database content.