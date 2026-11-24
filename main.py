#!/usr/bin/env python3
"""Funniest Autocorrect Fail — one line, under 200 characters.

Running this program with no arguments prints exactly one line: a text
about milk that autocorrect turns into a text about Mike, and the
consequence of that slip. The slip is one word, milk to Mike, and the
payoff is the stranger who comes home: the joke lands on first read.
"""

import os
import sys

LINE = (
    "Texted my wife 'Pick up milk on your way home' \u2014 autocorrect "
    "sent 'Pick up Mike on your way home.' She came home with a "
    "stranger named Mike."
)


def main() -> int:
    line = LINE.strip()
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 199:
        print("entry must be 1-199 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        stored = handle.read()
    if stored != line + "\n":
        print("stored entry does not match", file=sys.stderr)
        return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
