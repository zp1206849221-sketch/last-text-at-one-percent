"""Last Text at One Percent — a phone's dying-battery confession.

The joke: at 1% battery, the phone finally tells the truth —
autocorrect always knew what you meant, the photos were never
backed up, TikTok drained the battery, and the charger gets
the last words of affection.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

SETUP = (
    "last 1% confession: i knew exactly what u meant every time "
    "i typed duck, ur photos were never backed up, and tiktok "
    "killed me."
)
PUNCHLINE = "tell the charger i love you"


def build_line():
    """Join the confession and its last-words payoff into one line."""
    return f"{SETUP} {PUNCHLINE}"


def validate(line):
    """The entry must be a single non-empty line within the limit."""
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, limit {MAX_CHARS}"


def main():
    line = build_line()
    validate(line)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and confirm the file holds exactly what we wrote.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == line, "written entry differs from the line"


if __name__ == "__main__":
    main()
