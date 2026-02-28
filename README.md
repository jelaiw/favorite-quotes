## Input Data
I have collected my favorite quotes in a text file of semi-structured but mixed format.
* All of these quotes were manually copy and pasted into this file with the quote text first _optionally_ followed by the author (or some other reference to the source material).
* Most quotes do have an author or some attribution.
* Many of the quotes are contained on a single line while others are multi-line with some attempt to preserve whitespace for readability. 
* Some are just links (usually as a URL meant for visiting from a web browser) to online quotes hosted elsewhere. These should be included in the cleaned data.
* The name of the file that contains these data is `raw_input.txt`.

## Data Cleaning
* When parsing and cleaning data, act as a data engineer with specific expertise in parsing, cleaning up, and reformatting flat files.
* Report problems and ask for further guidance instead of silently suppressing errors when data cannot be processed.
* It is ok to produce as output both a cleaned data file as well as a file containing input data that could not be processed.

## Scripting
* Prefer Python 3 for scripting. Prefer modern Python conventions, idioms, and testing approaches.
* Only keep scripts that were actually used to create the final output. Source code that was run in an intermediate step but whose output was completely discarded can be removed.
* If there are problems running scripts within the terminal (or other agent execution environment) that is ok. If scripting is still the right approach do not pivot to something else. Tell me and I can help you run the script or troubleshoot the problem.

## Output Format
* The desired output file format is the Linux "fortune" program file format.
* Write all output to a sub-directory named `fortune`.
* Name the main output file `quotes`.

## Quality Control
When checking output for correctness, act as a QA engineer that primarily supports a data science team.

Your quality control (QC) report should consider the following questions:
* How many total quotes were you able to successfully parse?
* Were there any data that could not be parsed or otherwise processed into a quote?
* Is there ambiguity in either the input data or given instructions?
* Was additional ambiguity uncovered during an intermediate step?

Ok to ask clarifying questions or for further guidance.
