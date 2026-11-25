"""Entry program for the make.fun bounty "Have You Tried Turning It Off?".

The joke writes itself: the oldest tech-support advice in the world,
delivered as a complete script with no page two. This program writes
that single line to ``entry.txt`` inside the directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable, falling back to
``/output`` when the variable is unset (which matches the grader
container used by make.fun).

The entry text lives in the module-level constant ``ENTRY`` below, so
the program is fully deterministic: every run produces exactly the
same bytes. Before writing, the program validates the text against
the bounty gate -- UTF-8 text of 1 to 199 characters, a single line,
and not only whitespace -- and refuses to write anything that fails.
After writing, it reads the file back and compares it byte for byte
with the constant, so a silent write error can never pass unnoticed.

Run it from the repository root, for example:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
    cat out/entry.txt

Only the Python 3 standard library is used.
"""

import os
import sys
from pathlib import Path

ENTRY = "Have you tried turning it off and on again? …You have? Then we're done here — that was the entire script. They never wrote a page two; I'm as lost as you are."

MAX_CHARS = 199
DEFAULT_OUTPUT_DIR = "/output"


def validate(text: str) -> str | None:
    """Return an error message if *text* fails the gate, else ``None``."""
    if not text.strip():
        return "the entry is empty or only whitespace"
    if "\n" in text or "\r" in text:
        return "the entry must be a single line (no newline characters)"
    if len(text) > MAX_CHARS:
        return f"the entry is {len(text)} characters, over the {MAX_CHARS} limit"
    return None


def main() -> int:
    # Gate check first: never write a file the bounty would reject.
    # Validating the constant (not user input) means a failure here is a
    # bug in this file, so the message tells the maintainer exactly why.
    problem = validate(ENTRY)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or DEFAULT_OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(ENTRY, encoding="utf-8")

    written = dest.read_text(encoding="utf-8")
    if written != ENTRY:
        print("error: the file on disk differs from the entry text", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
