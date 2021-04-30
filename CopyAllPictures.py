#!/usr/bin/env python3

import shutil 
import os 
import argparse
import sys
import datetime
import tkinter as tk
from tkinter import filedialog


def parse_args(args):

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", help="path to the input drive, this is likely 'C'"
    )
    parser.add_argument(
        "-o", "--output", help="path to the source drive, this likely 'D' or 'E'"
    )

    return parser.parse_args()

def main(args):
    print(args)

    root = tk.Tk()

    if not args.input:
        src_dir = filedialog.askdirectory()
    else:
        src_dir = args.input + ":"

    if not args.output:
        dst_dir = filedialog.askdirectory()
        dst_dir = os.path.join(dst_dir, "photodump_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M"))
    else:
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
