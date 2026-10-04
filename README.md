# NBA Market Intelligence

This project accompanies the **Week 1 NBA Market Research Report** in English. The complete project can regenerate a four-page PDF, standalone pie charts, and analytical datasets offline.

## Repository contents

This repository currently contains the five top-level project files: `.gitignore`, `config.py`, `main.py`, `README.md`, and `requirements.txt`. The `src/`, `data/`, `outputs/`, and `prompts/` directories shown below belong to the complete local project and have not yet been uploaded. Running the pipeline requires `src/` and the input files in `data/raw/`.

## Quick start

Requires Python 3.10 or later and the complete project files. Open a terminal in the project directory:

```powershell
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

You can also run `.venv\Scripts\python.exe main.py` without activating the environment. After installing the dependencies, the pipeline requires no API key or network connection. All paths are relative to the project directory.

## Complete project structure

```text
nba-market-intelligence/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   │   ├── evidence.json
│   │   ├── sources.json
│   │   └── research_brief.json
│   └── processed/
│       ├── metrics.json
│       ├── metrics.csv
│       ├── analysis.json
│       ├── market_distribution.csv
│       ├── research_plan.json
│       ├── source_inventory.json
│       └── validation.json
├── src/
│   ├── __init__.py
│   ├── planner.py
│   ├── search.py
│   ├── extractor.py
│   ├── analysis.py
│   ├── charts.py
│   └── report.py
├── outputs/
│   ├── charts/
│   │   ├── market_size_pie.svg
│   │   └── market_size_pie.pdf
│   └── nba_report.pdf
└── prompts/
    ├── planner.txt
    ├── extraction.txt
    └── analysis.txt
```

## Module responsibilities

| Module | Implemented functionality |
| --- | --- |
| planner.py | Creates the fixed Week 1 work plan from the research brief |
| search.py | Loads the local source catalog and searches it by keyword |
| extractor.py | Validates fields, units, values, sources, and periods, then organizes factual records |
| analysis.py | Calculates annual average media contract value, sponsorship growth, team revenue ratios, and an illustrative distribution |
| charts.py | Exports SVG and PDF charts with source annotations and draws charts within the report |
| report.py | Generates the PDF using the established English layout, processed values, and sources |

`search.py` searches local sources and does not call an online search engine. `extractor.py` reads manually curated structured evidence and does not scrape websites. The files in `prompts/` are templates for future model integration; the current pipeline does not call a model. Automated online collection, paid database access, and real-time refresh are not configured.

## Data sources and measurement definitions

`data/raw/` contains manually curated facts and a source catalog, rather than downloaded publisher databases or webpage snapshots. The data comes from the original research discussion and public materials checked during PDF preparation. `sources.json` records links, their purpose, and verification dates. Each fact includes a value, unit, period, evidence status, and source identifier.

- Annual revenue: approximately $12.5B in combined revenue for all 30 NBA teams in 2024–25.
- Team valuations: the 2025 Forbes valuation cycle. Valuations and annual revenue must not be added together.
- $77B is the contract value reported by the media; $7B is its annual average over the 11-year term.
- Sponsorship figures are third-party estimates. Audience counts and viewing counts use different measurement definitions.
- The pie chart retains the original report's shares of 56.0%, 20.0%, 14.4%, and 9.6% and is explicitly labeled as an illustration combining different seasons. Ticket revenue is an assumption, and the other category is an arithmetic residual. **These shares do not represent the NBA's actual revenue composition.**

## Updating and reproducing the results

In the complete project, edit `data/raw/evidence.json` and run `python main.py` to update the processed data, calculations, charts, and numerical values in the report. The report retains fixed Week 1 narrative, season references, and conclusions. If the research period, sources, or interpretation changes, review `src/report.py` and `data/raw/sources.json` as well, especially the chart definitions. Updating numerical values does not automatically perform new research or validate the conclusions.

`config.py` controls paths and the preparation date. Running the pipeline overwrites the project's processed datasets, charts, and PDF. Structural checks cover the four-page count, extractable text, required metrics, units, and source associations. The original local deliverables were also rendered and visually reviewed. Repeat the visual review after changing the content.

## Calculation examples

```text
Media annual average = 77 / 11 = 7.0 (USD billion)
Sponsorship growth = (1.80 / 1.62 - 1) * 100 = 11.1%
Lakers / Hornets revenue = 551 / 328 = 1.68x
Illustrative residual = 12.5 - 7.0 - 2.5 - 1.8 = 1.2
```

Charts are generated with ReportLab and the Python standard library, without requiring system fonts, LaTeX, Poppler, or a separate plotting library.
