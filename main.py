#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the phone battery's final message to the charger it waited
for all day to /output/entry.txt, then gate-checks it:
UTF-8 text, 1-200 characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "waited all day for you and now you want 100% in twenty minutes? "
    "i'm not a microwave. i'm a battery with boundaries and 2% left, "
    "so this is goodbye. the power bank can have you."
)

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text: str) -> None:
    """Raise SystemExit(1) unless the text passes the competition gate."""
    if not text or not text.strip():
        sys.exit("gate failed: entry is empty or only whitespace")
    if len(text) > 200:
        sys.exit(f"gate failed: entry is {len(text)} characters (max 200)")
    if "\n" in text or "\r" in text:
        sys.exit("gate failed: entry must be a single line")
    if len(text.encode("utf-8")) > 200:
        sys.exit("gate failed: entry exceeds 200 bytes")


def main() -> None:
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Verify what landed on disk matches the entry exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        sys.exit("gate failed: written entry differs from ENTRY")
    gate_check(written)
    print(f"wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
