#!/usr/bin/env python3
"""Write one razor-sharp excuse for skipping a pointless meeting.

make.fun bounty: The Funniest Excuse for Skipping a Meeting.

Writes exactly one line to /output/entry.txt: a fresh, Zoom-true excuse
with a sharp turn -- the webcam itself refusing to look at the caller
anymore. Deterministic, no network, no randomness.
"""

import os

ENTRY = "Can't make the call \u2014 my webcam just filed a restraining order against my face."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
