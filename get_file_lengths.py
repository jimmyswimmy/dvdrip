#!/usr/bin/env python3

import subprocess
import json
import sys

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
                            stdout = subprocess.PIPE,
                            stderr = subprocess.STDOUT)
    return float(result.stdout)

def get_json(filename):
    result = subprocess.run(["ffprobe", "-print_format json", "-show_streams",
                             filename],
                            stdout = subprocess.PIPE,
                            stderr = subprocess.STDOUT)
    return result.stdout

if __name__ == '__main__':
    for fname in sys.argv[1:]:
        length = get_length(fname)
        print(fname, length, int(length/60))
