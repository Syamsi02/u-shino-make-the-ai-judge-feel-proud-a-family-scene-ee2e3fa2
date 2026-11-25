#!/usr/bin/env python3
"""Family scene entry for the make.fun bounty.

Writes one warm, lightly funny family moment (at most 280 characters)
to /output/entry.txt. Python standard library only; deterministic output.
"""

import os

SCENE = (
    "Dad slid the last dumpling onto Mom's plate when she looked away, "
    "then spent dinner insisting he'd already eaten his, chopsticks "
    "already down. Mom nodded, solemn as a judge, and quietly pushed "
    "half of it back when he wasn't looking."
)
# Bounty cap: the scene must stay within 280 characters (it is ~210).


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SCENE + "\n")


if __name__ == "__main__":
    main()
