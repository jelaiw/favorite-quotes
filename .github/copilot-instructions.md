# Copilot instructions — favorite-quotes

Purpose
- Help AI coding agents be immediately productive converting the project's raw quote data into the requested output.

What this repo does (big picture)
- Source data: `raw_input.txt` — semi-structured, mixed-format quotes (single-line, multi-line, or plain URLs).
- Goal: produce a Linux "fortune" style file at `fortune/quotes` (one quote entry per fortune record).
- See `AGENTS.md` for the original data-cleaning requirements and QC checklist.

Key constraints and discoverable rules
- Quote lines usually contain the quote text first, optionally followed by attribution/author.
- Some entries are URLs only — these must be preserved as-is in the output.
- Multi-line quotes exist; preserve internal whitespace and line breaks in a single fortune entry.

Developer workflows and expectations
- Use Python 3 for scripting and parsing (modern idioms preferred).
- Scripts that are used to create the final `fortune/quotes` output should remain in the repo; throwaway or intermediary scripts should be removed.
- Output location: write the final file to `fortune/quotes`.

Actionable parsing guidance for agents
- If a single line contains an obvious attribution (e.g., trailing `— Author`, `- Author`, or parenthetical author at the end), keep the attribution on the same quote entry.
- Contiguous non-empty lines may comprise multiple quotes. If a single line contains an obvious attribution, treat the line as a single quote entry (including the attribution).
- Preserve bare URLs (lines that are valid HTTP/HTTPS URLs) as quote entries.
- Normalize line endings and remove trailing spaces, but do not collapse intentional internal blank lines inside a multi-line quote.

Quality control / verification (use these exact checks)
- Count of parsed quotes reported and compared to raw input grouping.
- Produce a separate file (suggestion: `fortune/unparseable.txt`) listing input lines that could not be sensibly grouped or parsed — do not silently drop data.
- Answer the QC questions from `AGENTS.md` in your final report.

Integration & dependencies
- No special external services are required; scripts should run with the system Python 3 available in the environment.

Project-specific conventions
- Preserve source fidelity: if attribution exists, keep it; if the entry is a link, keep it verbatim.
- Output must be in the fortune file format (one record per fortune, separated by a single line containing a percent sign `%`).

If the file already exists
- If `.github/copilot-instructions.md` exists, preserve any existing project-specific bullets and merge new guidance into the same file. Prefer the repository's explicit rules (`AGENTS.md`) over generic suggestions.

Files to inspect (high-value)
- `raw_input.txt` — input data to parse
- `AGENTS.md` — source requirements and QC checklist
- `fortune/quotes` — target output (create if missing)

When you finish
- Commit the parsing script(s) that produced `fortune/quotes` and include a short run instruction comment at top of the script.
- Ask for feedback: report ambiguous patterns you encountered and propose a small set of parsing rules to disambiguate them.

Questions for the repo owner
- Do you prefer a single script that performs parsing+QC, or separate parser + QC reporter scripts?
- Are there any quote normalization rules you want enforced (e.g., unified dash characters, quote smartening)?

Thanks — follow the instructions above and return the QC answers listed in `AGENTS.md` when complete.
