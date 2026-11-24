#!/usr/bin/env python3
"""Place the committed front-page image at the harness output path.

The entry itself is entry.png: a 1024x1024 newspaper front page summing
up the world news of Monday 23 November 2026, drawn from verified
headlines and committed to this repository. This script draws nothing
and fetches nothing. It copies that file, byte for byte, into the
output directory and refuses to finish unless the copy matches the
original exactly.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable and defaults to /output.
"""

import hashlib
import os
import shutil
import sys


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        print("entry.png is missing next to main.py", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)

    if sha256_of(source) != sha256_of(target):
        print("output does not match the committed entry.png", file=sys.stderr)
        return 1

    print("wrote " + target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
