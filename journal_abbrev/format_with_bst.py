import subprocess
import os

def format_bib_with_bst(bib_path, bst_path, temp_dir):
    tex_path = os.path.join(temp_dir, "temp.tex")
    with open(tex_path, "w") as f:
        f.write(f"\\documentclass{{article}}\n\\begin{{document}}\n\\nocite{{*}}\n"
                f"\\bibliographystyle{{{bst_path}}}\n\\bibliography{{{bib_path}}}\n\\end{{document}}")

    subprocess.run(["pdflatex", tex_path], cwd=temp_dir)
    subprocess.run(["bibtex", "temp"], cwd=temp_dir)


