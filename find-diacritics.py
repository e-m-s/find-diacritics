import csv
import string
import sys
import os.path
import argparse

# Parse arguments
parser = argparse.ArgumentParser(
                    prog='find-diacritics',
                    description='Find records containing image links with non-ASCII characters',
                    epilog='Example: python find-diacritics -d , input.csv')
parser.add_argument('filename')
parser.add_argument('-d', '--delimiter', default=';')
args = parser.parse_args()

# Default values
DELIMITER = args.delimiter;
filename = args.filename

if not os.path.isfile(filename):
    print('File', filename, ' does not exist!')
    print('Enter: python ', sys.argv[0], ' filename.csv')
    exit()


# Otevřeme soubor pro čtení
with open(filename, 'r', encoding='utf-8') as csvfile:

    # Vytvoříme čtečku CSV
    reader = csv.reader(csvfile, delimiter=DELIMITER)

    # Pro každý řádek v souboru
    for row in reader:
        printme = False
        # Zjistíme, zda řádek obsahuje znak s diakritikou
        for itemstring in row:
            if itemstring.startswith('http') or 'emco.cz' in itemstring or '.jpg' in itemstring:
#                print(itemstring)
                for char in itemstring:
                    if not char in string.printable:
                        # Pokud ano, vypíšeme ho
                        printme = True
        if printme:
           print(DELIMITER.join(row))
