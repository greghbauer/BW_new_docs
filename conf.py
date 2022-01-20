#!/usr/bin/env python3

import sys
import os
import sys

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode', 
    'sphinx_markdown_tables',
    
   
]

# for markdown files
from recommonmark.parser import CommonMarkParser
# The suffix of source filenames.
source_suffix=['.rst', '.md']

source_parsers = {
       '.md': CommonMarkParser,
}
