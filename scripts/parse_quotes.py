#!/usr/bin/env python3
"""Small parser to convert `raw_input.txt` into `fortune/quotes`.

Run: python3 scripts/parse_quotes.py

This script implements the repository's discovered rules:
- Groups contiguous non-empty lines into one quote entry.
- Preserves internal line breaks inside each group.
- Leaves bare HTTP/HTTPS URLs as-is.
- Writes `fortune/quotes` (fortune file format) and `fortune/unparseable.txt`.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw_input.txt"
OUT_DIR = ROOT / "fortune"
OUT_DIR.mkdir(exist_ok=True)
OUT_FILE = OUT_DIR / "quotes"
UNPARSABLE = OUT_DIR / "unparseable.txt"

def is_url(line: str) -> bool:
    return bool(re.match(r"^https?://", line.strip()))

def read_groups(text: str):
    # Split on one or more blank lines; preserve internal whitespace inside groups
    parts = re.split(r"\n{2,}", text.strip(), flags=re.MULTILINE)
    groups = [p.rstrip() for p in parts if p.strip() != ""]
    return groups


def is_attribution(group: str) -> bool:
    g = group.strip()
    # Common attribution starters: From, By, em-dash attribution lines, or short '— Name' lines
    if re.match(r'^(From\b|From\s+\u201c|From\s+\")', g, flags=re.IGNORECASE):
        return True
    if re.match(r'^[\u2014\u2013\-–]\s*\w+', g):
        return True
    # contain 'by Name' pattern and short
    if re.search(r'\bby\s+[A-Z][a-z]+', g) and len(g) < 120:
        return True
    return False


def is_poem_like(group: str) -> bool:
    lines = [ln for ln in group.splitlines() if ln.strip()]
    if len(lines) < 2:
        return False
    avg_len = sum(len(ln.strip()) for ln in lines) / len(lines)
    # poems tend to have short lines and several lines
    return avg_len < 60 and len(lines) >= 3

def main():
    if not RAW.exists():
        print(f"Input file not found: {RAW}")
        raise SystemExit(1)

    raw_text = RAW.read_text(encoding="utf-8")
    # Normalize CRLF -> LF and strip trailing spaces
    raw_text = raw_text.replace("\r\n", "\n").rstrip() + "\n"

    groups = read_groups(raw_text)

    unparseable = []
    entries = []

    # Post-process groups to merge poem-like runs followed by an attribution line
    merged = []
    i = 0
    while i < len(groups):
        g = groups[i]
        # If this group looks like an attribution, consider merging with previous poem-like groups
        if is_attribution(g) and merged:
            # look back for contiguous poem-like groups (up to 10 groups back)
            j = len(merged) - 1
            to_merge = [g]
            merged_back = []
            while j >= 0 and len(merged_back) < 10:
                prev = merged[j]
                if is_poem_like(prev):
                    merged_back.insert(0, prev)
                    j -= 1
                else:
                    break
            if merged_back:
                # remove the merged_back elements from merged
                merged = merged[: j + 1]
                merged_entry = "\n\n".join(merged_back + [g])
                merged.append(merged_entry)
                i += 1
                continue

        # Otherwise keep group as-is
        merged.append(g)
        i += 1

    def is_multi_quote_block(group: str) -> bool:
        lines = [ln.strip() for ln in group.splitlines() if ln.strip()]
        if len(lines) < 2:
            return False
        avg_len = sum(len(ln) for ln in lines) / len(lines)
        # If many lines contain an author dash or double-dash, treat as multiple single-line quotes
        score = 0
        for ln in lines:
            if re.search(r"\s[-–—]{1,2}\s+[A-Z\"\(]", ln):
                score += 1
            if " -- " in ln:
                score += 1
        # If there are exactly two lines and both have author-like dashes, split
        if len(lines) == 2 and score >= 2:
            return True
        return avg_len > 40 and score >= max(1, len(lines) // 4)

    # Now build entries from merged groups (splitting multi-quote blocks when detected)
    for g in merged:
        lines = [ln.rstrip() for ln in g.splitlines()]
        if len(lines) == 1 and is_url(lines[0]):
            entries.append(lines[0].strip())
            continue

        if is_multi_quote_block(g):
            for ln in lines:
                ln2 = ln.strip()
                if ln2:
                    # If line contains a trailing URL, split it out
                    m = re.search(r"(https?://\S+)", ln2)
                    if m:
                        url = m.group(1)
                        text = ln2[:m.start()].strip()
                        if text:
                            entries.append(text)
                        entries.append(url)
                    else:
                        entries.append(ln2)
            continue

        cleaned = "\n".join(lines).strip()
        if cleaned == "":
            unparseable.append(g)
        else:
            # If a single-line entry contains an inline URL, split it into quote + url
            if "http" in cleaned:
                m = re.search(r"(https?://\S+)", cleaned)
                if m:
                    before = cleaned[:m.start()].strip()
                    url = m.group(1)
                    if before:
                        entries.append(before)
                    entries.append(url)
                    continue
            entries.append(cleaned)

    # Post-process: merge header + numbered list sequences into a single entry
    final_entries = []
    i = 0
    while i < len(entries):
        cur = entries[i]
        # header ends with ':' and next entries look like numbered rules (Rule 1., Rule 2., or numbered list)
        if cur.rstrip().endswith(":"):
            j = i + 1
            to_merge = [cur]
            while j < len(entries) and re.match(r"^(Rule\s+\d|^\d+\.|^\w+\s\d)", entries[j]):
                to_merge.append(entries[j])
                j += 1
            if len(to_merge) > 1:
                final_entries.append("\n\n".join(to_merge))
                i = j
                continue
        final_entries.append(cur)
        i += 1

    entries = final_entries

    # Write fortune file (records separated by a line containing a single %)
    with OUT_FILE.open("w", encoding="utf-8") as f:
        for i, e in enumerate(entries):
            f.write(e.rstrip() + "\n")
            f.write("%\n")

    # Write unparseable if any
    if unparseable:
        UNPARSABLE.write_text("\n\n".join(unparseable), encoding="utf-8")
    else:
        UNPARSABLE.write_text("", encoding="utf-8")

    # QC report to stdout
    print("QC Report:")
    print(f"- Total input groups: {len(groups)}")
    print(f"- Parsed quotes (entries): {len(entries)}")
    print(f"- Unparseable groups: {len(unparseable)}")
    if unparseable:
        print(f"- See {UNPARSABLE} for details")
    print(f"- Fortune file written: {OUT_FILE}")

if __name__ == '__main__':
    main()
