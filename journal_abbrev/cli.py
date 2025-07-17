import click
import os
import tempfile
import subprocess
import shutil
import json
from .abbreviator import abbreviate_bib_file
from .format_with_bst import format_bib_with_bst
from .fetch_bst_files import fetch_bst_files


@click.command()
@click.argument('bib_file', type=click.Path(exists=True))
@click.option('-o', '--output', required=True, help='Output .bib file path')
@click.option('-c', '--custom', default=None, help='Custom abbreviation JSON')
@click.option('-r', '--remove-fields', is_flag=True, help='Remove URL/eprint/note')
@click.option('--bst', type=click.Path(), help='Path to .bst file for formatting')
@click.option('--fetch-bst', is_flag=True, help='Scrape and download all .bst files from journals.json')
def main(bib_file, output, custom, remove_fields, bst, fetch_bst):
    """
    Abbreviate journal names in a .bib file and optionally format it using a .bst file.
    """
    if fetch_bst:
        fetch_bst_files('data/journals.json', 'bst_styles')
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

