"""ai-joke-03 entry: one joke about AI coding agents.

The joke is written to entry.txt under $MAKEFUN_OUTPUT_DIR
(or /output by default), one line, no trailing newline.
no network, no randomness, no clock.
Rebuilt after the competition opened, so the entry transcripts fall
inside the submission window.
"""

import os
from pathlib import Path

JOKE = "My agent debugged all night. The bug was my prompt."


def entry_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
