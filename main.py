#!/usr/bin/env python3
"""news-image-20261123 entry: copy the committed front-page image to the output directory.

The image (entry.png) is a newspaper front page summing up the world news of
Monday 23 November 2026. This program does no drawing and no network: it
copies the committed file byte for byte, so both grading runs write identical
bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly instead of silently shipping a partial copy.
    with open(src, "rb") as f_src, open(dst, "rb") as f_dst:
        assert f_src.read() == f_dst.read(), "entry.png copy mismatch"


if __name__ == "__main__":
    main()
