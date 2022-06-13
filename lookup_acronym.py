#!/usr/bin/env python

import pandas as pd
import argparse
import os

_DIR = '/Users/leodutton/Work/AstraZeneca/acronyms'
_MAIN_DICT = 'acronym_dictionary.xlsx'
_USER_DICT = 'user_dictionary.csv'

def load_acronym_dictionaries():
    """Loads the dictionary of acronyms from the excel file. Concats all the 
    sheets into a single df.

    Returns:
        DataFrame: lookup table of acronyms
    """
    acr_file_path = os.path.join(_DIR, _MAIN_DICT)
    acronyms = pd.read_excel(acr_file_path, sheet_name=None, header=None)
    
    dir = os.listdir(_DIR)

    if _USER_DICT in dir:
        user_file_path = os.path.join(_DIR, _USER_DICT)
        user = pd.read_csv(user_file_path, header=None)
        acronyms['user'] = user
    
    
    acronyms = pd.concat(acronyms)
    acronyms.rename(columns={0:'acronym', 1:'meaning'}, inplace=True)
    acronyms['acronym'] = acronyms['acronym'].str.strip()
    return acronyms

def lookup_acronym(search: str):
    """Searches the lookup table of acronyms for a desired string.
    Prints a list of the meaning(s)

    Args:
        search (str): The acronym to be searched for 
    """
    search = search.upper()
    acronyms = load_acronym_dictionaries()

    if search in list(acronyms['acronym'].str.upper()):
        result = acronyms[acronyms['acronym'].str.upper()==search]
        result = result.dropna(axis=1, how='all')
        result = result['meaning'].values
        print(*result, sep='\n')
    else:       
        print('Acronym not in dictionary')

def get_args() -> str:
    """Gets the acronym parsed in by the command line

    Returns:
        str: acronym to search
    """
    parser = argparse.ArgumentParser(description="A program to lookup acronyms in a dictionary")
    parser.add_argument('-s', '--search', help="Searches the dictionary for the acronym supplied")
    parser.add_argument('-a', '--add', help="Searches the dictionary for the acronym supplied")
    args = parser.parse_args()
    search = args.search
    add = args.add

    return search, add

def add_acronym(add: str):
    acronym = add
    y = input(f'Would you like to add {acronym} to the user dictionary? (Y/n)')
    if y.lower() == 'y':
        meaning = input('Meaning: ')
        df = pd.DataFrame([[acronym, meaning]])
        file_path = os.path.join(_DIR, _USER_DICT)
        df.to_csv(file_path, mode='a', header=False, index=False)

if __name__=='__main__':

    search, add = get_args()
    # if not search:
    #     search = input('Enter the acronym to search for: ')
    if search:
        lookup_acronym(search)
    elif add:
        add_acronym(add)
    else:
        print('Please input an acronym to search for, or a new acronym to add')