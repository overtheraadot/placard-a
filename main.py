"""make.fun entry: Office Artifacts: The One-Line Placard Contest (placard-a).

Writes one original one-line museum placard for the office fridge to
/output/entry.txt and prints a short report.

Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 180
characters, not only white space. The entry is a single line.

The placard: the office fridge recast as a cold storage vessel from a
lost civilisation, with a catalogue date, a material and a donor, and
the driest possible warning. The joke turns on one detail: something
inside the fridge is older than the building that houses it, which is
exactly the kind of fact a curator would record without blinking, and
exactly why the label ends by forbidding both opening and enquiry.
"""

import os

# The entry: one line, my own invention. Older contents than the building.
ENTRY = (
    "Cold Storage Vessel, c. 2019. White steel, still humming. "
    "Gift of Facilities. One container inside predates the building. "
    "Do not open. Do not ask."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 180


def verify(text):
    """Enforce the gate from RULES.txt: 1-180 chars, non-blank, one line.

    Also rejects leading/trailing whitespace: the judged text is the
    line itself, so stray spaces would count against the limit and
    look sloppy on the placard.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    """Validate the entry, then write it exactly as-is, no newline."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def report(path):
    """Read the written file back and print its length and headroom."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    headroom = MAX_CHARS - len(text)
    print("Wrote %s (%d chars, %d line(s), %d chars of headroom)"
          % (path, len(text), text.count("\n") + 1, headroom))
    print(text)
    return text


def main():
    report(write_entry())


if __name__ == "__main__":
    main()
