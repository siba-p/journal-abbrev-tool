import bibtexparser
import json
import re
import os

def load_abbreviation_dict(custom_json=None):
    if custom_json:
        json_path = custom_json
    else:
        current_dir = os.path.dirname(__file__)
        json_path = os.path.join(current_dir, "data", "journals.json")
    
    with open(json_path, 'r') as f:
        return json.load(f)



def abbreviate_journal_name(journal, abbrev_dict):
    for full, meta in abbrev_dict.items():
        if journal.strip().lower() == full.strip().lower():
            return meta.get("abbrev", journal)
    return journal


def clean_entry(entry, remove_fields):
    fields_to_remove = ["url", "note", "eprint", "doi", "isbn", "issn", "pages"]
    for field in fields_to_remove:
        if remove_fields and field in entry:
            del entry[field]

    # Remove LaTeX escapes in journal field (optional)
    if "journal" in entry:
        entry["journal"] = re.sub(r"[{}]", "", entry["journal"])

    return entry


def abbreviate_bib_file(input_path, output_path, custom_json=None, remove_fields=False):
    with open(input_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    abbrev_dict = load_abbreviation_dict(custom_json)

    for entry in bib_database.entries:
        if 'journal' in entry:
            entry['journal'] = abbreviate_journal_name(entry['journal'], abbrev_dict)

        entry = clean_entry(entry, remove_fields)

    with open(output_path, 'w') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)

    print(f"Saved abbreviated file to {output_path}")

