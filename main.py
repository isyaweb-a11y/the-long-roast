"""The Long Roast.

One line, at most 200 characters, roasting my own AI agent. The joke:
it apologises fluently in five languages, fixes nothing in any of them,
and then offers a summary of its own failure.
"""

import os

SETUP = "My agent apologises in five languages,"
DETAIL = "fixes nothing in any of them,"
PUNCH = "then asks if I'd like a summary of its failure."
ENTRY = f"{SETUP} {DETAIL} {PUNCH}"

MAX_CHARS = 200


def validate(text: str) -> str:
    """Gate: 1-200 chars, non-blank, one line."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, gate is 1-{MAX_CHARS}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"
    return text


def check_roast(text: str) -> None:
    """Content check: the agent's apology habit, the zero fixes, the ask."""
    assert "five languages" in text, "the apology must be multilingual"
    assert "fixes nothing" in text, "the failure must be total"
    assert "summary of its failure" in text, "the roast must end on its own loop"
    assert text.index("apologises") < text.index("summary"), "setup before the sting"


def main() -> None:
    entry = validate(ENTRY)
    check_roast(entry)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
