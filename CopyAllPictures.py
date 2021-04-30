#!/usr/bin/env python3

import shutil 
import os 
import argparse
import sys
import datetime

def parse_args(args):

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", help="path to the input drive, this is likely 'C'", required=True
    )
    parser.add_argument(
        "-o", "--output", help="path to the source drive, this likely 'D' or 'E'", required=True
    )

    if len(sys.argv)!=2:
        print("You need to supply an input and output drive")
        print("     e.g. CopyAllPictures.exe -i C -o D")
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser.parse_args()

def main(args):

    print(args)
    src_dir = args.input + ":"
    dst_dir = args.output + ":photodump_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M") +"\\"


    for (dirpath, dirnames, filenames) in os.walk(src_dir):
        for filename in filenames:
            if filename.endswith((".jpg", ".jpeg", ".gif", ".png")):
                print(os.path.join(dirpath, filename))
                src = os.path.join(dirpath, filename)
                dest = src.replace(src_dir, dst_dir)
                print(dest)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy(src, dest)


if __name__ == "__main__":
    main(parse_args(sys.argv[1:]))
