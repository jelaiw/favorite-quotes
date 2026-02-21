# Copilot Instructions: Favorite Quotes Data Cleaning

## Project Overview
This is a **data cleaning & engineering project**, not a general software project. The goal is to parse semi-structured quote data from `raw_input.txt`, normalize it into a structured format, and produce quality reports alongside cleaned output.

## Input Data Format (Critical)
`raw_input.txt` contains quotes in mixed formats:
- **Single-line quotes**: Quote text followed by author on same line, separated by `--` or `– ` (em-dash)
- **Multi-line quotes**: Poetry/prose spanning multiple lines, with author attribution after blank line(s) on separate line(s)
- **URLs only**: Some entries are just links to external quote sources
- **Author attribution variants**: Author names may appear as:
  - `-- AuthorName` (two hyphens)
  - `– AuthorName` (em-dash)
  - Preceded by "From" or "by" keywords
  - Sometimes includes work title in quotes: `From "Work Title" by AuthorName`

## Parsing Strategy
1. **Recognize quote blocks** by author patterns, not line breaks alone
2. **Handle whitespace** carefully—preserve internal formatting, normalize leading/trailing
3. **Separate concerns**: Quote text ≠ Author/Source
4. **Classify entries**: Parseable quote (text + author), URL-only, or unparseable
5. **Track failures explicitly**: Log what couldn't parse and why (missing author, no quote text, malformed structure)

## Data Engineering Expectations
- **Report, don't suppress**: When data can't be parsed, document the problem explicitly (create an `unparseable.txt` or similar error report)
- **Track statistics**: Count total entries, successfully parsed, failed, URL-only entries
- **QA mindset**: Verify parsing accuracy—sample check decoded output matches original intent
- **Ask clarifying questions**: If edge cases lack clear guidance, ask rather than guess

## Output Requirements
- **Primary output**: `fortune/quotes` – Linux fortune file format—quotes separated by `%` on its own line. Multi-line quotes allowed. Example:
  ```
  Quote text here
  %
  Another quote here
  -- Author Name
  %
  ```
- **Error report**: `fortune/unparseable.txt` – File listing entries that couldn't be parsed with context
- **QC report**: `fortune/qc_report.txt` – Number parsed vs. failed, any anomalies, validation checks performed

## Key Files
- [raw_input.txt](../raw_input.txt) – Input data (184 lines, mixed formats)
- [AGENTS.md](../AGENTS.md) – Project scope & QC requirements reference
- Output files: TBD based on task requirements
