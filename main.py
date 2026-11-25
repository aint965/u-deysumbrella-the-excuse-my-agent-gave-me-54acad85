#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one short line to the output file: the excuse an AI agent hands its
human after missing a deadline. Deterministic: every run writes byte-identical
output. No network, no reads outside the repo, no secrets.
"""

import os
import sys

# The single excuse line. Exactly one line, 1-200 characters, not only
# whitespace. Do not change this text: the entry's score depends on it.
EXCUSE = "I delegated the deadline to a subagent, who delegated it to a subagent, who delegated it back to me."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the excuse against the competition gate before writing.

    Raises ValueError with a clear reason when the text would fail the
    gate, so a bad line is caught here instead of scoring a 0.
    """
    if not text:
        raise ValueError("excuse is empty (gate needs 1-200 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"excuse is {len(text)} characters, over the 200-character gate"
        )
    if not text.strip():
        raise ValueError("excuse is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> int:
    try:
        validate(EXCUSE)
    except (ValueError, UnicodeEncodeError) as exc:
        print(f"error: invalid excuse: {exc}", file=sys.stderr)
        return 1
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
