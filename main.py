#!/usr/bin/env python3
"""Entry point for the news-image-20261119 v2 front page.

The page itself (entry.png, 1024 by 1024) is composed by
build_frontpage_v2.py from generated photo panels and PIL typesetting.
This script only places those exact bytes where the harness looks for
them. It never touches the network, never re-encodes the image and
never writes a timestamp, so repeated runs stay byte-identical.
"""

import shutil
import sys
from os import environ, makedirs
from os.path import abspath, dirname, join


def run() -> int:
    # v2 keeps the v1 contract (copy entry.png to the harness output dir)
    # but spells the path handling out instead of relying on module globals.
    here = dirname(abspath(__file__))
    target_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(target_dir, exist_ok=True)
    shutil.copyfile(join(here, "entry.png"), join(target_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
