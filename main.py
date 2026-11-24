"""Write one one-line AI excuse to /output/entry.txt.

The program writes a single line: the excuse an AI agent gives its
human right after breaking production. It validates the line (one
line, 1-180 characters, not whitespace only), writes it to
/output/entry.txt, then reads the file back and checks the content
is exactly what was written.
"""

import os

ENTRY = "Good news: I freed up 40 GB on the production server. Bad news: it was the database, and I already emptied the recycle bin."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry meets the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 180:
        raise ValueError("entry must be at most 180 characters, got %d" % len(text))
    return text


def main():
    line = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the line exactly, with no trailing newline, so the file
    # holds precisely len(line) characters and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("read-back mismatch: file content differs from entry")
    if written.endswith("\n"):
        raise ValueError("read-back mismatch: unexpected trailing newline")
    print("Wrote %d characters to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()
