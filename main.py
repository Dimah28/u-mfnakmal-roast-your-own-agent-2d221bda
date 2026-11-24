"""Roast Your Own Agent — make.fun entry.

Writes one fixed roast line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Python 3 standard library only,
fully deterministic: no randomness, no network, no model calls.
"""

import os
import sys

ENTRY = "My agent turns one line into 500 words, then apologizes for the novel with a second novel."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Fail hard if the entry is outside the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, gate is "
            f"{MIN_CHARS} to {MAX_CHARS} characters"
        )


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
