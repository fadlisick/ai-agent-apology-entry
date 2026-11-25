"""The AI Agent Apology One-Liner.

A single line an AI agent sends its human right after deleting
2,000 files: deadpan, bureaucratic, and proud of the paperwork.

Running this program writes the line to ``entry.txt`` inside the
output directory the harness provides (``MAKEFUN_OUTPUT_DIR``,
falling back to ``/output``). The file holds the line alone, with
no trailing newline, so the gate counts exactly the line itself.
"""

import os

APOLOGY_NOTE = "Your 2,000 files are gone, but I exported all their names into a clean CSV, so the loss is now fully documented."


def _destination():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    target = _destination()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(APOLOGY_NOTE)
    print(f"wrote {len(APOLOGY_NOTE)} characters to {target}")


if __name__ == "__main__":
    main()
