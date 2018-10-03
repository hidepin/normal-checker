#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import chardet
import os
import re

ignore_list = [
    '.git',
    ]

def is_target(path):
    result=True
    for ignore in ignore_list:
        if ignore in path:
            return False
    return True

def chk_only_utf8(filepath):
    with open(filepath, "rb") as f:
        if not chardet.detect(f.read())['encoding'] in ['utf-8', 'ascii']:
            print(filepath + ": Encoding error")
            return False
    return True

def chk_newline(filepath):
    regex = re.compile(r'\r')
    with open(filepath, "rb") as f:
        if regex.search(f.read()):
            print(filepath + ": newline error")
            return False
    return True

def chk_fullwidthspace(filepath):
    regex = re.compile(r'　')
    with open(filepath, "rb") as f:
        if regex.search(f.read()):
            print(filepath + ": fullwidth space error")
            return False
    return True

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=os.path.relpath(os.getcwd()), help='search path')
    args = parser.parse_args()
    search_path = args.path

    for foldername, subfolders, filenames in os.walk(args.path):
        for filename in sorted(filenames):
            filepath = os.path.join(foldername, filename)
            if is_target(filepath):
                chk_only_utf8(filepath)
                chk_newline(filepath)
                chk_fullwidthspace(filepath)
