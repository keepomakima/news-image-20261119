#!/usr/bin/env python3
"""news-image-20261119 v4 entrypoint.

The front page is baked into this repository as entry.png. Running this
program places an exact copy at /output/entry.png. It draws nothing and
talks to no network — it only moves bytes from here to there.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(TARGET_DIR, "entry.png")


def deliver():
    if not os.path.isfile(SOURCE):
        sys.exit("entry.png is missing from the repository")
    os.makedirs(TARGET_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    src_bytes = os.path.getsize(SOURCE)
    dst_bytes = os.path.getsize(TARGET)
    if src_bytes != dst_bytes:
        sys.exit("entry.png copy is incomplete: %d != %d" % (src_bytes, dst_bytes))
    print("delivered %s (%d bytes) -> %s" % (SOURCE, src_bytes, TARGET))


if __name__ == "__main__":
    deliver()
