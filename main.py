"""Famous Last Words: The Funniest Epitaph.

Writes one line to /output/entry.txt: a dying person's last words,
delivered as three parting messages. The first two are the ones you
expect. The third is the confession he took to the grave.
"""

import os

ENTRY = "Tell my wife I loved her. Tell my kids I was proud of them. Tell my boss the Wi-Fi was never actually down."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 150


def validate_entry(text):
    """Check the entry against the gate: 1 to 150 chars, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 150 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def main():
    text = validate_entry(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("read-back mismatch: file does not hold the entry")
    if len(written.encode("utf-8")) != len(text.encode("utf-8")):
        raise ValueError("read-back mismatch: file byte length differs")
    print(text)
    print("%d characters" % len(text))


if __name__ == "__main__":
    main()
