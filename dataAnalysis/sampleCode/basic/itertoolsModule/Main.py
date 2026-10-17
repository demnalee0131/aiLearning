# an example of using itertools.groupby to group names by their first letter

import itertools

def first_letter(x):
    return x[0]

names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))