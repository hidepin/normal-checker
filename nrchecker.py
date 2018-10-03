#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

ignore_list = [
    '.git',
    ]

def is_target(path):
    result=True
    for ignore in ignore_list:
        if ignore in path:
            return False
    return True

def chk_only_utf8(path):
    print(filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=os.path.relpath(os.getcwd()), help='search path')
    args = parser.parse_args()
    search_path = args.path

    for foldername, subfolders, filenames in os.walk(args.path):
        for filename in filenames:
            path = os.path.join(foldername, filename)
            if is_target(path):
                print(os.path.join(foldername, filename))
