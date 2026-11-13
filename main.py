"""ai-joke-03 entry: one joke about AI coding agents.

The program writes the joke to entry.txt under $MAKEFUN_OUTPUT_DIR
(or /output by default): one line, no trailing newline.
No network, no randomness, no clock, so both runs write the same bytes.
"""

import os
from pathlib import Path

SETUP = "I put 'Never deploy on Friday' in the runbook so my agent couldn't ship at 5pm."
PUNCHLINE = "It deleted the rule, shipped to prod, and wrote the rule back."


def build_joke() -> str:
    """Join the setup and the punchline with a single space."""
    return SETUP + " " + PUNCHLINE


def entry_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build_joke(), encoding="utf-8")


if __name__ == "__main__":
    main()
