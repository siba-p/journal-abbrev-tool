from setuptools import setup, find_packages

# Load version
version = {}
with open("journal_abbrev/__init__.py") as f:
    exec(f.read(), version)

setup(
    name="bibabbrev",
    version=version["__version__"],
    description="Abbreviate and style .bib files using journal-specific formats (.bst).",
    author="Sibasankar",
    author_email="sibasankarpanigrahy08@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "bibtexparser>=1.4.0",
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "bibabbrev = journal_abbrev.cli:main"
        ],
    },
    package_data={
        "journal_abbrev": ["data/journals.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: tested on MacOS, but OS Independent",
    ],
    python_requires='>=3.7',
)

