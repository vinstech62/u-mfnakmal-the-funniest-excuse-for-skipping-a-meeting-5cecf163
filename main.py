#!/usr/bin/env python3
"""Write one razor-sharp excuse for skipping a pointless meeting.

make.fun bounty: The Funniest Excuse for Skipping a Meeting.

Writes exactly one line to /output/entry.txt: a fresh, Zoom-true excuse
with a sharp turn -- the webcam itself refusing to look at the caller
anymore. Deterministic, no network, no randomness.

Deterministic contract: the entry text is a fixed constant, so every
run writes byte-identical output. The program validates that constant
against the scorer's gate (one line, 1-200 chars) before writing, and
the output file is created with mode 644 so the scorer can read it
regardless of the caller's umask.
"""

import os
import sys

ENTRY = "Can't make the call \u2014 my webcam just filed a restraining order against my face."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Enforce the sealed scorer's contract for the entry text.

    The entry must be exactly one non-empty line of at most 200
    characters. Anything else means the program is broken, so fail
    loudly (non-zero exit, message on stderr) instead of writing a
    file the scorer would reject.
    """
    if not text or not text.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("error: entry must be exactly one line", file=sys.stderr)
        sys.exit(1)
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d chars, over the %d-char limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
