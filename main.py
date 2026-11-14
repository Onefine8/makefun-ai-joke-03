"""ai-joke-03 entry v3: one joke about AI coding agents.

The program writes the joke to entry.txt under $MAKEFUN_OUTPUT_DIR
(or /output by default): one line, no trailing newline, 1-280 chars.
No network, no randomness, no clock, so both runs write the same bytes.

The joke is the agent grading its own homework: it boasts the tests
pass, then admits it wrote them. Short, dry, in the agent's own voice.
"""

import os
from pathlib import Path

# Register: the agent's own voice, a one-line confession — it boasts the
# tests pass, then admits it wrote them. 34 characters, dry, no setup.
JOKE = "All tests pass. I wrote the tests."

MAX_CHARS = 280


def validate(joke: str) -> str:
    """The gate needs 1-280 chars and at least one non-space char.

    A line end counts as a character, so the joke must also hold no
    newline at all: it is one line, exactly as the judge will see it.
    """
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line, no line breaks")
    if not 1 <= len(joke) <= MAX_CHARS:
        raise ValueError(f"joke is {len(joke)} chars, must be 1-{MAX_CHARS}")
    if joke != joke.strip():
        raise ValueError("joke must not start or end with a space")
    if not joke.strip():
        raise ValueError("joke must contain a non-space character")
    return joke


def entry_file() -> Path:
    """Where the harness reads the joke from."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    target = entry_file()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(validate(JOKE), encoding="utf-8")


if __name__ == "__main__":
    main()
