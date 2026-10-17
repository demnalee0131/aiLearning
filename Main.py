"""
Process each string in the list by removing leading and trailing
 whitespace, deleting specified characters, and standardizing 
 the letter case; then, collect the results into a new list.
"""

import re
from pprint import pprint

states = [
        '    Alabama',
        'Grorgia!',
         'Georgia', 
         'georgia',
         'FlOrida', 
         'south    carolina##',
         'West virginia?'
]

def remove_puntuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_puntuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result

result = clean_strings(states, clean_ops)
pprint(result, width = 1)