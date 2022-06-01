import imp
from statistics import mean
import pandas as pd
import argparse
import os


acronym = input('Acronym: ')
meaning = input('Meaning: ')
df = pd.DataFrame([[acronym, meaning]])
df.to_csv('user_dictionary.csv', mode='a', header=False, index=False)