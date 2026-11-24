#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — entrypoint.

Writes the final one-line developer excuse to /output/entry.txt.
Deterministic, no network, no environment secrets, no dependencies.

The line: a developer, asked why production broke, answers that the code
was tested thoroughly — against a sample of exactly one user, himself.
Setup ("tested it thoroughly") promises rigour; the twist reveals the test
population was the developer. That is the joke the judge brief rewards:
a twist every developer recognises, in words a developer would actually
say, with nothing left to trim (74 characters).
"""

import os

EXCUSE = "I tested it thoroughly \u2014 against the one user who behaves exactly like me."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in text, "excuse must be a single line"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
