#!/usr/bin/env python3

import argparse
import logging

parser = argparse.ArgumentParser(description="Put your TeX and Bib files here to visualize the relationship tying them")
parser.add_argument('-t', '--tex', nargs='*', default=[], type=str, help="TeX files to load and link")
parser.add_argument('-b', '--bib', nargs='*', default=[], type=str, help="BiB files to load and link")
parser.add_argument('-v', '--verbose', action="store_true", help="Set output to verbose (debug)")

args = parser.parse_args()

print(args.tex, args.bib, args.verbose)
if(args.verbose):
    logging.basicConfig(level=logging.DEBUG)

from latexparser import LaTexFiles
from bibtexparser import BibTexFiles

bibtexfiles = LaTexFiles(args.tex)
bibtexfiles = BibTexFiles(args.bib)
