# main.py

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "proposal.txt")

SECTIONS_ORDER = [
    "Introduction",
    "Problem Statement",
    "Objectives",
    "Methodology",
    "Conclusion"
]

MIN_LENGTH = 100
MAX_LENGTH = 2000


def read_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("ERROR: file proposal.txt peyda nashod (bayad kenar file python bashe).")
        sys.exit(1)


def extract_sections(text):
    sections = {}
    current_section = None
    buffer = []

    for line in text.splitlines():
        line = line.strip()

        if line in SECTIONS_ORDER:
            if current_section:
                sections[current_section] = "\n".join(buffer).strip()
            current_section = line
            buffer = []
        else:
            if current_section:
                buffer.append(line)

    if current_section:
        sections[current_section] = "\n".join(buffer).strip()

    return sections


def check_missing_sections(sections, warnings):
    for sec in SECTIONS_ORDER:
        if sec not in sections:
            warnings.append(f'WARNING: bakhsh "{sec}" vojood nadarad.')


def check_section_length(sections, warnings):
    for sec, content in sections.items():
        length = len(content)
        if length < MIN_LENGTH:
            warnings.append(
                f'WARNING: bakhsh "{sec}" kheyli kootahe ({length} character).'
            )
        elif length > MAX_LENGTH:
            warnings.append(
                f'WARNING: bakhsh "{sec}" kheyli bolande ({length} character).'
            )


def check_section_order(text, warnings):
    found_order = []
    for line in text.splitlines():
        line = line.strip()
        if line in SECTIONS_ORDER and line not in found_order:
            found_order.append(line)

    correct_order = sorted(found_order, key=lambda x: SECTIONS_ORDER.index(x))
    if found_order != correct_order:
        warnings.append("WARNING: tartib-e bakhsh-ha mantiqi nist.")


def main():
    print("---- Proposal Checker Started ----")

    warnings = []

    text = read_file()
    sections = extract_sections(text)

    check_missing_sections(sections, warnings)
    check_section_length(sections, warnings)
    check_section_order(text, warnings)

    if warnings:
        for w in warnings:
            print(w)
    else:
        print("OK: hich moshkeli peyda nashod.")

    print("---- Check Finished ----")


if __name__ == "__main__":
    main()
