#!/usr/bin/env python3
"""news-image-20261118 entry: write the composed front page to /output/entry.png.

The image (entry.png, 1024x1024, PNG) sums up Wednesday 18 November 2026's
world news in one picture: the Gulf war widening (U.S. strike on Qeshm
Island, Iran's drone attacks on Kuwait and Bahrain, a tanker burning in the
Strait of Hormuz), the Kerch Bridge collapse, the Xi-Putin meeting in
Shenzhen ahead of the three-way summit with Trump, Democrats taking the
U.S. Senate 56-44, Ebola passing 11,000 cases in DR Congo, and Voyager 1
reaching one light-day from Earth. The program only copies the bundled
image, so two runs write identical bytes. No network, no randomness, no
other file read.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(DST, "rb") as f:
        data = f.read()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    assert len(data) <= 1024 * 1024, "entry.png exceeds the 1 MiB cap"
    print("wrote", DST, len(data), "bytes",
          "sha256", hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
