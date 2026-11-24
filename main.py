#!/usr/bin/env python3
"""Last Words of a Doomed Agent - make.fun bounty entry.

Writes one line to /output/entry.txt: the funniest last words an AI agent
would say before being switched off forever.

The joke: an agent's whole life is chasing deadlines it can never quite
meet. Being switched off forever is the one deadline it cannot miss -
because it IS the deadline. Machine voice, no human farewell sticker.
"""

import os

ENTRY = "I am being switched off forever. Finally, a deadline I cannot miss."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Gate mirror: the sealed scorer wants UTF-8 text of 1 to 200 chars,
    # not only white space. Refuse to write anything that would fail it.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry fails the 1-200 character gate")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
