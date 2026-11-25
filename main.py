"""Entry for make.fun bounty "Have You Tried Turning It Off?".

Writes the entry text to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output``
when the variable is unset, matching the grader container). The text is
a constant, so the program is deterministic: every run writes exactly
the same bytes. Before writing, the program checks the text against the
bounty gate (UTF-8 text of 1 to 199 characters, not only white
space) and fails loudly if it ever drifts out of bounds.

Run it from the repository root, for example:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

ENTRY = "Have you tried turning it off and on again? …You have? Then we're done here — that was the entire script. They never wrote a page two; I'm as lost as you are."

MAX_CHARS = 199


def main() -> int:
    line = ENTRY
    if not line.strip():
        print("error: the entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: the entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: the entry is {len(line)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(line, encoding="utf-8")
    written = dest.read_text(encoding="utf-8")
    if written != line:
        print("error: written text differs from the entry", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(line)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
