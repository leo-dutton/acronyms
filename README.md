# Acronym search tool
## Introduction

This is a simple package for searching the acronym dictionary supplied by AZ

## Setup

1. Ensure that you have installed pandas in the desired environment.
2. Add your dictionary of acronyms excel worksheet to the repo, with the name
`acronym_dictionary.xlsx`

## Use
### Search
Simply run the lookup script using the command `python lookup_acronym.py`.

The `-a` or `--acronym` argument can be used to seach for an acronym.
If no argument is given, you will be prompted to input an acronym to search for.

If the acronym is present in the dictionary, the script will print a list of its meaning(s).

### Add
Run the add script with the command `python add_acronym.py`

You will then be prompted to input an acronym, followed by its meaning.

These will be saved to a file called `user_dictionary.csv`