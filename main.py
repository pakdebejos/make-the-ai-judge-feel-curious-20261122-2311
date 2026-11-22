# main.py — "The Folded Page": a one-text entry for make.fun's
# make-the-ai-judge-feel-curious-20261122-2311.
#
# The program writes exactly one short text — a fixed constant, well inside
# the gate's 280-character cap, with no trailing newline — to entry.txt in
# the output directory. The text is fixed: the entry is the writing, and
# the program is only the hand that sets it down, the same way twice.
# the output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader),
# so both of the grader's runs write byte-identical output. Pure Python
# standard library only; no network.
import os

TEXT = """In the library's returned books, someone folds down the same page — page forty-seven, a different book each time, the same corner creased twice. No one has ever seen who does it. The librarian has stopped unfolding them."""

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
