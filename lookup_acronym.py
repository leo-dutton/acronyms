from ast import parse
from email import parser
import pandas as pd
import argparse
import os

_MAIN_DICT = 'acronym_dictionary.xlsx'
_USER_DICT = 'user_dictionary.csv'

def load_acronym_dictionaries():
    """Loads the dictionary of acronyms from the excel file. Concats all the 
    sheets into a single df.

    Returns:
        DataFrame: lookup table of acronyms
    """
    acronyms = pd.read_excel(_MAIN_DICT, sheet_name=None, header=None)
    
    dir = os.listdir()
    if _USER_DICT in dir:
        user = pd.read_csv(_USER_DICT, header=None)
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
        print(result['meaning'].values)
    else:       
        print('Acronym not in dictionary')

def get_args() -> str:
    """Gets the acronym parsed in by the command line

    Returns:
        str: acronym to search
    """
    parser = argparse.ArgumentParser(description="A program to lookup acronyms in a dictionary")
    parser.add_argument('-a', '--acronym', help="Searches the dictionary for the acronym supplied")
    args = parser.parse_args()
    search = args.acronym

    return search


if __name__=='__main__':

    search = get_args()
    if not search:
        search = input('Enter the acronym to search for: ')

    lookup_acronym(search)