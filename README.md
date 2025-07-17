# 📚 Journal Abbreviation and BibTeX Formatter

A Python CLI tool to **automatically abbreviate journal names** in `.bib` files and **optionally format** them using `.bst` (BibTeX style) files. Ideal for preparing BibTeX files according to specific journal submission standards.

journal-abbrev-tool/
│
├── journal_abbrev/
│   ├── __init__.py
│   ├── abbreviator.py      # Core logic for abbreviation
│   ├── cli.py              # Command-line interface
│   └── data/
│       └── journals.json   # Journal abbreviation and .bst links
│
├── tests/                  # Test cases (optional)
├── setup.py                # Install and dependency config
├── README.md

---

## Features

- Abbreviates journal names in `.bib` files using a comprehensive database (`journals.json`)
- Cleans up unwanted BibTeX fields like `URL`, `eprint`, etc.
- Optional `.bst` formatting using LaTeX-compatible BibTeX style files
- Automatically fetches `.bst` files if listed in `journals.json`

---

## Installation

Clone this repository and install:

```bash
git clone https://github.com/yourusername/journal-abbrev-tool.git
cd journal-abbrev-tool
pip install .

### 🚀 Usage

#### 🔤 Abbreviate journal names in a `.bib` file

```bash
python -m journal_abbrev.cli path/to/input.bib -o path/to/output.bib

python -m journal_abbrev.cli input.bib --clean

Format using a .bst file

python -m journal_abbrev.cli input.bib --bst path/to/style.bst

Auto-fetch .bst style for a specific journal

python -m journal_abbrev.cli input.bib --fetch-bst "Nature"

This will search for the matching .bst in journals.json, download it

Example

@article{doi:10.1021/acsomega.4c03344,
  author  = {Rajput, Satyendra and Panigrahy, Sibasankar and Nayar, Divya},
  title   = {In Silico View of Crowding: Biomolecular Processes to Nanomaterial Design},
  journal = {ACS Omega},
  volume  = {0},
  number  = {0},
  pages   = {null},
  year    = {0},
  doi     = {10.1021/acsomega.4c03344},
  URL     = {https://doi.org/10.1021/acsomega.4c03344},
  eprint  = {https://doi.org/10.1021/acsomega.4c03344}
}

After running:

python -m journal_abbrev.cli input.bib --clean

@article{doi:10.1021/acsomega.4c03344,
  author  = {Rajput, Satyendra and Panigrahy, Sibasankar and Nayar, Divya},
  title   = {In Silico View of Crowding: Biomolecular Processes to Nanomaterial Design},
  journal = {ACS Omega},
  volume  = {0},
  number  = {0},
  pages   = {null},
  year    = {0}
}

