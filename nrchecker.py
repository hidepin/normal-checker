#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=os.path.relpath(os.getcwd()), help='search path')
    args = parser.parse_args()
    search_path = args.path

    for foldername, subfolders, filenames in os.walk(args.path):
        for filename in filenames:
            print(os.path.join(foldername, filename))
