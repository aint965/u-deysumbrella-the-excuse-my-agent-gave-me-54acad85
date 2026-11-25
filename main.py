#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one short line to the output file: the excuse an AI agent hands its
human after missing a deadline. Deterministic: every run writes byte-identical
output. No network, no reads outside the repo, no secrets.
"""

import os
import sys

LINE = "I delegated the deadline to a subagent, who delegated it to a subagent, who delegated it back to me."


def main() -> None:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
