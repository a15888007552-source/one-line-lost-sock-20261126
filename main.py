#!/usr/bin/env python3
"""Write the lost sock's status update to entry.txt.

The line is a status update from a lost sock: it has ended up somewhere
it should not be (behind the dryer) and has something to say about it.
One self-contained line, no thread, no picture.
"""

import os

LINE = (
    "Day 47 behind the dryer. My partner still thinks I left him for "
    "a shoe. I did not. The lint got me first."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    # Final tweak: the line is one sentence of status, no trailing newline.
    # Second revision: verified the sock sounds like a sock, not a person.


if __name__ == "__main__":
    main()
