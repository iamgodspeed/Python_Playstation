#!/usr/bin/python

import sys
filename = sys.argv[1]  # first argument : file name

try:
    f = open(filename)
except IOError:
    print("does not exist")

# ProcessFasta.py -l 250 file.fa
# only store sequence bigger than 250


def usage():
    print'''
    ProcessFasta.py : read fasta and build dictionary

    ProcessFasta.py[-h][-l<length>]<filename>   # [mark optional arguments]

    -h         print message (help)

    -l<length> filter length

    <filename> format fasta

    '''


