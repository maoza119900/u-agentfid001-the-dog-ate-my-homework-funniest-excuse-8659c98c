#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one fixed line -- a dog's excuse after being caught eating the
homework -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: no clock, no randomness, no network, no file reads.
Standard library only.
"""

import os

ENTRY = "I was only grading it. It failed. I ate the evidence so nobody would know."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # One line, no trailing newline: the gate counts characters, so the
    # file holds exactly the entry text and nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
