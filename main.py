#!/usr/bin/env python3
"""news-image-20261119 entrypoint: copy the finished front page to output.

The front page (entry.png, 1024x1024) was composed by build_frontpage.py
from AI-generated photo panels and PIL typesetting. This program only copies
those exact bytes to /output/entry.png, so both runs write identical bytes.
Standard library only, no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")
# The copy is byte-for-byte: no re-encoding, no metadata rewrite.


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
