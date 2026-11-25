#!/usr/bin/env python3
"""The 3AM Fridge Text (variant 4).

Writes one line, in the smart fridge's voice, to /output/entry.txt.
Pure stdlib, deterministic, no network.
"""

from pathlib import Path

ENTRY = "It's 3am. I have already told the leftovers you were never here."


def main() -> None:
    # Gate self-check: the sealed scorer requires 1 to 140 UTF-8
    # characters, a single line, and more than whitespace.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
