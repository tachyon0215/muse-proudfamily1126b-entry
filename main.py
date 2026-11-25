#!/usr/bin/env python3
"""Write the family-scene entry to entry.txt.

Competition: Make the AI Judge Feel Proud: A Family Scene (1-2 lines,
1-280 characters). The judge brief weighs, in order: a real family
scene that makes a proud judge smile; heartfelt genuine affection;
light, recognisable humour; economy of lines; a specific, fresh
detail over a greeting-card line.
Three candidates were drafted and compared:
A) "Dad spent all morning teaching the baby to say 'mama' first. She
   looked at him, grinned, and said it - to the dog. He clapped
   anyway, loudest of all."
B) A grandmother keeping a chair for her late husband - heartfelt,
   but the death note risks tipping warm into sad.
C) A daughter rating her father's cooking four stars, one for the
   smoke alarm - funny, but the affection stays a joke.
Selected A: the turn (her first 'mama' goes to the dog) is the light
recognisable laugh, and the last clause is pure affection - he lost
his own contest and clapped loudest anyway. Two sentences, no word
wasted, one telling detail (all morning).
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Dad spent all morning teaching the baby to say 'mama' first. She looked at him, grinned, and said it - to the dog. He clapped anyway, loudest of all."
TEXT = LINE + "\n"
MAX_CHARS = 280


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must be non-empty")
    if body.count("\n") > 1 or "\r" in body:
        raise ValueError("entry must fit in one or two lines")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
