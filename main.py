#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Entry program: writes one resignation line, in the voice of a cron job
that only runs on 29 February, to /output/entry.txt.
Pure stdlib only.
"""

# PART_A — the entry line (117 chars, one line, 1-140).
LINE = (
    "I work one day every four years and you still paged me on the other "
    "1,460, so I am taking the next leap year off too."
)

# PART_B — writer with guard: exactly one line, 1-140 chars, no newline.
import os
from pathlib import Path


def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 140, f"entry length {len(LINE)} out of range"
    assert LINE.strip() == LINE and LINE.strip(), "entry must not be blank"
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # Guard: what was written is byte-identical to the line.
    assert out.read_text(encoding="utf-8") == LINE


if __name__ == "__main__":
    main()
