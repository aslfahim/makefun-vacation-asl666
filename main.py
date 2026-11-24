"""One Emoji, One Dream Vacation -- Surfer entry.

Writes exactly one emoji, U+1F3C4 SURFER (🏄), to entry.txt inside the
output directory. Standard library only; no network, no arguments.
"""

import os
import sys

# The single emoji this entry submits: a surfer riding a wave.
DREAM_EMOJI = "\U0001f3c4"

# The gate requires 1 to 8 characters of non-whitespace UTF-8 text.
MIN_LENGTH = 1
MAX_LENGTH = 8


def resolve_output_dir() -> str:
    """Return the directory entry.txt goes in (env var or /output)."""
    directory = os.environ.get("OUTPUT_DIR", "/output")
    if not directory:
        raise ValueError("OUTPUT_DIR is set but empty")
    return directory


def validate(text: str) -> None:
    """Refuse anything that is not exactly one dream-vacation emoji."""
    if len(text) != 1:
        raise ValueError(f"expected 1 code point, got {len(text)}")
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError("text outside the 1-8 character gate")
    if text != DREAM_EMOJI:
        raise ValueError("text is not the assigned surfer emoji")
    if text.isspace():
        raise ValueError("text must not be whitespace only")


def write_entry(directory: str, text: str) -> str:
    """Write text to entry.txt with no trailing newline; return the path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def verify(path: str, expected: str) -> None:
    """Read the file back and confirm it holds exactly the expected text."""
    with open(path, "rb") as handle:
        raw = handle.read()
    expected_bytes = expected.encode("utf-8")
    if raw != expected_bytes:
        raise ValueError(
            f"verification failed: disk holds {raw!r}, expected {expected_bytes!r}"
        )
    landed = raw.decode("utf-8")  # strict: rejects any malformed UTF-8
    if landed != expected:
        raise ValueError(
            f"verification failed: disk holds {landed!r}, expected {expected!r}"
        )


def main() -> int:
    validate(DREAM_EMOJI)
    directory = resolve_output_dir()
    path = write_entry(directory, DREAM_EMOJI)
    verify(path, DREAM_EMOJI)
    print(f"wrote {DREAM_EMOJI} to {path} (1 code point, 4 bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
