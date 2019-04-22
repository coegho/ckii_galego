#!/usr/bin/python3

from tkinter import filedialog
from tkinter import *
import csv
import json
import os


def processfile(directory, filename):
    "This process a csv file to generate the json files"
    dicts = {"en":{}, "fr":{}, "de":{}, "es":{}}
  
    with open(os.path.join(directory, filename), newline='', encoding='iso-8859-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if len(row) < 6 or row[0].startswith('#'):
              print('#')
            else:
              dicts['en'][row[0]] = row[1]
              dicts['fr'][row[0]] = row[2]
              dicts['de'][row[0]] = row[3]
              dicts['es'][row[0]] = row[5]
              print(f'- {row[0]}')
            line_count += 1
        print(f'{filename} processed with {line_count} lines.')
    return dicts

print('Where is the source directory?')
root = Tk()
root.directory = filedialog.askdirectory()
print('Where is the target directory?')
target = Tk()
target.directory = filedialog.askdirectory()
print (f'Looking for files in {root.directory}')

globaldicts = {'en': {}, 'fr': {}, 'de': {}, 'es': {}}

for filename in os.listdir(root.directory):
    if filename.endswith(".csv"):
        path = os.path.join(root.directory, filename)
        base = os.path.splitext(filename)[0]
        print(path)
        dicts = processfile(root.directory, filename)
        globaldicts['en'][base] = dicts['en']
        globaldicts['fr'][base] = dicts['fr']
        globaldicts['de'][base] = dicts['de']
        globaldicts['es'][base] = dicts['es']
    else:
        continue

with open(target.directory + '/translation-gl.json', 'w') as en_json:
    json.dump(globaldicts['en'], en_json, indent=4)

