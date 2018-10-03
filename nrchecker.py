#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import chardet


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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=os.path.relpath(os.getcwd()), help='search path')
    args = parser.parse_args()
    search_path = args.path

    for foldername, subfolders, filenames in os.walk(args.path):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            if is_target(filepath) and not chk_only_utf8(filepath):
                break
