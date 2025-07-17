import click
import os
import tempfile
import subprocess
import shutil
import json
from .abbreviator import abbreviate_bib_file
from .format_with_bst import format_bib_with_bst
from .fetch_bst_files import fetch_bst_files

parser = argparse.ArgumentParser(description="Abbreviate journal names in BibTeX files.")
parser.add_argument("bib_file", help="Path to the BibTeX file.")
parser.add_argument("-o", "--output", help="Output file name. If not given, overwrites input.")
parser.add_argument("-c", "--custom", help="Path to custom abbreviation JSON file.")
parser.add_argument("-d", "--default", help="Path to default abbreviation JSON file.")
parser.add_argument("--clean", action="store_true", help="Remove unwanted BibTeX fields like URL, eprint, month.")
parser.add_argument("--bst", help="Path to a .bst file for formatting output.")
parser.add_argument("--fetch-bst", action="store_true", help="Auto-fetch a .bst file if journal name matches known journals.")


def main(bib_file, output, custom, remove_fields, bst, fetch_bst):
    """
    Abbreviate journal names in a .bib file and optionally format it using a .bst file.
    """
    if fetch_bst:
        fetch_bst_files('journals.json', 'bst_styles')
        return

    abbreviate_bib_file(
        input_path=bib_file,
        output_path=output,
        custom_json=custom,
        remove_fields=remove_fields
    )

    if bst:
        temp_dir = tempfile.mkdtemp()
        try:
            format_bib_with_bst(output, bst, temp_dir)
        finally:
            shutil.rmtree(temp_dir)


if __name__ == '__main__':
    main()

