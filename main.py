#!/usr/bin/env python3
"""One-line fridge roast for the make.fun joke bounty.

The roast lives in ROAST below. This program writes it, unchanged,
to entry.txt inside the output folder the grader reads.
"""

import os
import sys
from pathlib import Path

ROAST = "My fridge's vegetable drawer is where good intentions go to rot."
OUTPUT_NAME = "entry.txt"


def output_folder() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    folder = Path(chosen)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def main() -> int:
    line = ROAST.strip()
    if not line or len(line) > 200:
        print("roast must be 1 to 200 characters", file=sys.stderr)
        return 1
    target = output_folder() / OUTPUT_NAME
    target.write_text(line, encoding="utf-8")
    print(f"wrote {target} ({len(line)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
