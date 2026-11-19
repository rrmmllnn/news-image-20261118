#!/usr/bin/env python3
"""news-image-20261118 entry: write the composed front page to /output/entry.png.

The image (entry.png, 1024x1024, PNG) sums up Wednesday 18 November 2026's
world news in one picture. Six stories fill the front page:

1. The Gulf war widens: U.S. jets strike a missile site on Qeshm Island;
   Iran fires drones at U.S. bases in Kuwait and Bahrain; a tanker burns
   in the Strait of Hormuz.
2. The Kerch Bridge road arch collapses into the strait.
3. Xi Jinping and Vladimir Putin meet in Shenzhen ahead of the first
   three-way summit with Trump.
4. Democrats take the U.S. Senate 56-44 after Mary Peltola's win in Alaska.
5. Ebola passes 11,000 cases in DR Congo.
6. Voyager 1 reaches one light-day from Earth.

The footer carries four more: the Gaza ceasefire warning, Cyclone Xavier,
the Siberia plane crash, and Nvidia's record quarter. The panels are drawn
illustrations of the day's events; the headlines and captions state the
day's reported facts.

The program only copies the bundled image, so two runs write identical
bytes. No network, no randomness, no other file read. Pass --verify to
check the bundled image without writing anything; pass --output to choose
where the copy lands.
"""
import argparse
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DEFAULT_DST = "/output/entry.png"
MAX_BYTES = 1024 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

STORIES = [
    "Gulf war widens: U.S. strike on Qeshm Island, Iranian drones on Kuwait and Bahrain, tanker burning in the Strait of Hormuz",
    "Kerch Bridge road arch collapses into the strait",
    "Xi and Putin meet in Shenzhen ahead of the three-way summit with Trump",
    "Democrats take the U.S. Senate 56-44 after Peltola's win in Alaska",
    "Ebola passes 11,000 cases in DR Congo",
    "Voyager 1 reaches one light-day from Earth",
]


def read_png(path):
    """Return the bytes of a file after checking it is a PNG."""
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path} is not a PNG file")
    return data


def png_dimensions(data):
    """Read width and height from the PNG IHDR chunk."""
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def verify(data):
    """Check the bundled image against the competition's caps."""
    if len(data) > MAX_BYTES:
        raise ValueError(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    width, height = png_dimensions(data)
    if (width, height) != (1024, 1024):
        raise ValueError(f"entry.png is {width}x{height}, expected 1024x1024")
    return width, height


def print_stories():
    """List the six stories the front page carries."""
    print("stories on the front page:")
    for i, story in enumerate(STORIES, 1):
        print(f"  {i}. {story}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=DEFAULT_DST,
                        help="where to write the copy (default: %(default)s)")
    parser.add_argument("--verify", action="store_true",
                        help="check the bundled image and exit without writing")
    args = parser.parse_args(argv)

    data = read_png(SRC)
    width, height = verify(data)
    digest = hashlib.sha256(data).hexdigest()
    if args.verify:
        print(f"entry.png OK: {width}x{height}, {len(data)} bytes, sha256 {digest}")
        print_stories()
        return 0
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    shutil.copyfile(SRC, args.output)
    print(f"wrote {args.output} {len(data)} bytes sha256 {digest}")
    print_stories()
    return 0


if __name__ == "__main__":
    sys.exit(main())
