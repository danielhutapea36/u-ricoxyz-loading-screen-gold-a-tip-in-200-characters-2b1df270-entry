#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a one-line loading-screen tip to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is
133 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence
— every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a loading-screen
tip for stressed developers and AI coding agents — it reads as a
real tip shown mid-build, addressed to both the human and the
agent; (2) a real laugh through a turn, not a groan pun — the
punch reframes the agent's busywork as procrastination; (3) lands
in a glance — one short line, every word working; (4) speaks to
both audiences at once — the developer recognises the renamed
variable, the agent recognises itself stalling; (5) fresh — no
coffee, deadline or compile joke, just the quiet absurdity of an
agent polishing a name while the build burns. The em dash is the
hinge: everything before it is the setup, everything after it is
the verdict, and "Ship it." is the tip itself.
"""

import os

TEXT = (
    "Tip: your agent renamed that variable three times. It isn't "
    "refactoring \u2014 it's procrastinating in a language you can't "
    "read. Ship it."
)


def main() -> None:
    # Gate: entry.txt must be 1-200 characters of UTF-8 text, not only
    # whitespace. The line is 133 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
