#!/usr/bin/env python3
"""Scan the fortune/quotes file for attributions and verify them via Wikiquote.

Usage: python3 scripts/check_attributions.py

Output is a simple report written to stdout and also saved as
`fortune/attribution_report.txt`.
"""
from pathlib import Path
import re
import subprocess
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
QUOTE_FILE = ROOT / "fortune" / "quotes"
REPORT = ROOT / "fortune" / "attribution_report.txt"

# regex to pick attribution lines
attr_re = re.compile(r"^[\-–—]{1,2}\s*(.+)")
paren_re = re.compile(r"^\((.+)\)$")

records = [r.rstrip() for r in QUOTE_FILE.read_text(encoding="utf-8").split("\n%\n") if r.strip()]
author_records = []

for idx, rec in enumerate(records, start=1):
    lines = [ln.strip() for ln in rec.splitlines() if ln.strip()]
    if not lines:
        continue
    last = lines[-1]
    m = attr_re.match(last)
    if m:
        author = m.group(1).strip()
        quote = "\n".join(lines[:-1])
        author_records.append((idx, quote, author))
    else:
        # maybe paren attribution inside quote
        pm = paren_re.match(last)
        if pm:
            author = pm.group(1).strip()
            quote = "\n".join(lines[:-1])
            author_records.append((idx, quote, author))

# gather unique authors
authors = {}
for idx, quote, author in author_records:
    authors.setdefault(author, []).append((idx, quote))

print(f"Found {len(author_records)} attributed records with {len(authors)} distinct authors.")

report_lines = []

for author, entries in authors.items():
    report_lines.append(f"=== {author} ===")
    # generate wikiquote URL
    name = author.replace(' ', '_')
    url = f"https://en.wikiquote.org/wiki/{urllib.parse.quote(name)}"
    report_lines.append(f"Page: {url}")
    try:
        r = subprocess.run(['curl','-sL',url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
        html = r.stdout.decode('utf-8', errors='ignore')
    except Exception as e:
        report_lines.append(f"  Error fetching page: {e}")
        html = ''
    for idx, quote in entries:
        snippet = quote.strip().replace('\n',' ')
        found = snippet.lower() in html.lower()
        report_lines.append(f"  record {idx}: {'FOUND' if found else 'MISSING'} -> {snippet[:60]}{'...' if len(snippet)>60 else ''}")
    report_lines.append("")

REPORT.write_text("\n".join(report_lines), encoding='utf-8')
print(f"Report written to {REPORT}")
