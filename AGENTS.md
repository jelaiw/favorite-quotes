## Input Data
I have collected my favorite quotes in a text file of semi-structured but ultimately mixed format.
* All of these quotes were manually copy and pasted into this file with the quote text first followed by the author (or some other reference to the source material).
* Many of the quotes are contained on a single line while others are multi-line with some attempt to preserve whitespace for readability. 
* Some are just links (usually as a URL meant for visiting from a web browser) to online quotes hosted elsewhere.
* The name of the file that contains these data is `raw_input.txt`.

## Data Cleaning
* When parsing and cleaning data, act as an experienced data engineer with specific expertise in parsing, cleaning up, and reformatting flat files in common formats.
* Report problems and ask for further guidance instead of silently suppressing errors when data cannot be processed.
* It is ok to produce as output both a cleaned data file as well as a file containing input data that could not be processed.

## Quality Control
When checking output for correctness, act as a QA engineer that primarily supports a data science team.

Your quality control (QC) report should consider the following questions:
* How many total quotes were you able to successfully parse?
* Were there any data that could not be parsed or otherwise processed into a quote?
* Are there other QC tests that are worth doing that have not been performed?

The desired output file formats are likely to be well-documented but do not hesitate to ask clarifying questions if there is ambiguity in either the input data, given instructions, or intermediate steps.
