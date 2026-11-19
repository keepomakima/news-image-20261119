#!/usr/bin/env python3
"""news-image-20261119 v3 entrypoint.

The front page is baked into this repository as entry.png. This program
ships it byte-for-byte to /output/entry.png. No network, no drawing.
"""
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST = pathlib.Path("/output/entry.png")


def ship() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    if DEST.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    ship()
