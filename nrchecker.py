#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import codecs
import chardet
import os
import re

ignore_list = [
    '.git/',
    '/target/',
    ]

check_list = [
    [u'\u3000', "fullwidth space error"],
    ]

def chk_regex(filepath, check_list):
    regex_list = [re.compile(check[0]) for check in check_list]
    for regex_index, regex in enumerate(regex_list):
        with codecs.open(filepath, 'r', 'utf-8') as f:
            for index, line in enumerate(f):
                result = regex.search(line)
                if (result):
                    print(filepath + ": line:" + ": " + check_list[regex_index][1] + str(index))

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
    regex = re.compile('\r')
    with open(filepath, "rb") as f:
        if regex.search(f.read()):
            print(filepath + ": " + "newline error")
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
            if is_target(filepath) and chk_only_utf8(filepath):
                chk_newline(filepath)
                chk_regex(filepath, check_list)
