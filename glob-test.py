#!/usr/bin/env python3

import argparse, glob, sys

parser = argparse.ArgumentParser()
parser.add_argument("src_path", metavar="path", type=str,
    help="Example - python3 glob-test.py '/home/foo/**/*.txt' => will search recursevly for all .txt files in all subdirs of /home/foo directory")

args = parser.parse_args()
files = glob.glob(args.src_path, recursive=True)

if not files:
    print('File does not exist: ' + args.src_path, file=sys.stderr)
for file in files:
    print(file)
