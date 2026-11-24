#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line, a review of planet Earth left by an
alien tourist, to /output/entry.txt. Deterministic, stdlib only,
no network, no arguments.
"""

import os
import sys

LINE = "Earth, day two: the locals apologise to furniture when they bump into it and thank the machines that take their money, yet nobody thanked me once. 2 stars."


def main() -> int:
    # Gate: the entry must be 1-200 characters of real text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
